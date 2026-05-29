from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import db, BMIRecord, ProgressPhoto
import os
from werkzeug.utils import secure_filename
from utils.ai_recommender import calculate_bmi, get_bmi_category, generate_ai_recommendations
from utils.validators import validate_body_metrics, check_weight_change_warning

views = Blueprint('views', __name__)

@views.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('views.dashboard'))
    return render_template('index.html')

@views.route('/dashboard')
@login_required
def dashboard():
    records = BMIRecord.query.filter_by(user_id=current_user.id).order_by(BMIRecord.recorded_at.desc()).all()
    latest_record = records[0] if records else None
    
    # Prepare data for Chart.js
    records_asc = list(reversed(records))
    dates = [r.recorded_at.strftime('%b %d') for r in records_asc]
    weights = [r.weight for r in records_asc]
    bmis = [r.bmi_value for r in records_asc]
    
    health_score = None
    predictive_bmis = []
    
    if latest_record:
        # Simple health score logic
        ideal_bmi = 21.7
        divergence = abs(latest_record.bmi_value - ideal_bmi)
        health_score = max(0, int(100 - (divergence * 4.5))) # lose ~4.5 points per BMI point away
        
    if len(bmis) > 1:
        # Linear regression calculation for trend
        n = len(bmis)
        x = list(range(n))
        y = bmis
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(i*j for i, j in zip(x, y))
        sum_x2 = sum(i**2 for i in x)
        denom = (n * sum_x2 - sum_x**2)
        
        if denom != 0:
            m = (n * sum_xy - sum_x * sum_y) / denom
            c = (sum_y - m * sum_x) / n
            for i in range(n):
                predictive_bmis.append(round(m * i + c, 2))
            
            # Add one future prediction point
            predictive_bmis.append(round(m * n + c, 2))
            dates.append("Predicted (Next)")
        else:
            predictive_bmis = bmis.copy()
            predictive_bmis.append(bmis[-1])
            dates.append("Predicted (Next)")

    return render_template('dashboard.html', 
                           records=records, 
                           latest_record=latest_record,
                           chart_dates=dates,
                           chart_weights=weights,
                           chart_bmis=bmis,
                           predictive_bmis=predictive_bmis,
                           health_score=health_score)

@views.route('/add_bmi', methods=['GET', 'POST'])
@login_required
def add_bmi():
    if request.method == 'POST':
        weight = request.form.get('weight', type=float)
        
        if not weight:
            flash('Please enter your weight.', category='danger')
            return redirect(url_for('views.add_bmi'))
            
        height = current_user.height
        age = current_user.age
        
        # Soft validation for weight change
        latest_record = BMIRecord.query.filter_by(user_id=current_user.id).order_by(BMIRecord.recorded_at.desc()).first()
        last_weight = latest_record.weight if latest_record else None
        
        warning_msg = check_weight_change_warning(last_weight, weight)
        if warning_msg:
            flash(warning_msg, category='warning')
            
        bmi_value = calculate_bmi(weight, height)
        category = get_bmi_category(bmi_value)
        
        # AI Recommendation Engine Module rules applied here
        ai_advice = generate_ai_recommendations(age, current_user.gender, category, bmi_value)
        
        # Streak Calculation Logic
        from datetime import datetime, timedelta
        
        today = datetime.utcnow().date()
        date_last = current_user.last_log_date.date() if current_user.last_log_date else None
        
        if date_last == today:
            pass # Same day, streak remains
        elif date_last == today - timedelta(days=1):
            current_user.current_streak += 1 # Consecutive day
        else:
            current_user.current_streak = 1 # Broken streak or first time
            
        current_user.last_log_date = datetime.utcnow()
        
        new_record = BMIRecord(
            user_id=current_user.id,
            weight=weight,
            height_used=height,
            bmi_value=bmi_value,
            category=category,
            health_risk=ai_advice['risk'],
            diet_recommendation=ai_advice['diet'],
            foods_to_eat=ai_advice['foods_to_eat'],
            foods_to_avoid=ai_advice['foods_to_avoid'],
            exercise_plan=ai_advice['exercise'],
            lifestyle_advice=ai_advice['lifestyle'],
            daily_tips=ai_advice['daily_tips'],
            health_summary=ai_advice['summary']
        )
        
        db.session.add(new_record)
        db.session.commit()
        
        flash('BMI Record logged successfully! AI Analysis generated.', category='success')
        return redirect(url_for('views.result', record_id=new_record.id))

    return render_template('bmi_form.html')

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        new_age = request.form.get('age', type=int)
        new_height = request.form.get('height', type=float)
        new_gender = request.form.get('gender')
        
        if not new_age or not new_height or not new_gender:
            flash('All fields are required.', category='danger')
            return redirect(url_for('views.profile'))
            
        is_valid, err_msg = validate_body_metrics(current_user, new_age, new_height)
        if not is_valid:
            flash(err_msg, category='danger')
            return redirect(url_for('views.profile'))
            
        current_user.age = new_age
        current_user.height = new_height
        current_user.gender = new_gender
        db.session.commit()
        
        flash('Profile settings updated successfully.', category='success')
        return redirect(url_for('views.dashboard'))
        
    return render_template('profile.html', user=current_user)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@views.route('/upload_photo', methods=['POST'])
@login_required
def upload_photo():
    if 'photo' not in request.files:
        flash('No file part', category='danger')
        return redirect(url_for('views.profile'))
    file = request.files['photo']
    if file.filename == '':
        flash('No selected file', category='danger')
        return redirect(url_for('views.profile'))
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        import time
        filename = f"{current_user.id}_{int(time.time())}_{filename}"
        
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        new_photo = ProgressPhoto(user_id=current_user.id, filename=filename)
        db.session.add(new_photo)
        db.session.commit()
        
        flash('Progress photo uploaded successfully!', category='success')
    else:
        flash('Invalid file type (png, jpg, jpeg, gif allowed).', category='danger')
        
    return redirect(url_for('views.profile'))

@views.route('/result/<int:record_id>')
@login_required
def result(record_id):
    record = BMIRecord.query.get_or_404(record_id)
    if record.user_id != current_user.id:
        flash('Unauthorized block.', category='danger')
        return redirect(url_for('views.dashboard'))
        
    return render_template('result.html', record=record)

@views.route('/history')
@login_required
def history():
    records = BMIRecord.query.filter_by(user_id=current_user.id).order_by(BMIRecord.recorded_at.desc()).all()
    return render_template('history.html', records=records)

@views.route('/report')
@login_required
def report():
    records = BMIRecord.query.filter_by(user_id=current_user.id).order_by(BMIRecord.recorded_at.asc()).all()
    latest_record = records[-1] if records else None
    return render_template('report.html', user=current_user, records=records, latest_record=latest_record)

@views.route('/admin')
@login_required
def admin_panel():
    if getattr(current_user, 'is_admin', False) is False:
        flash('Unauthorized access.', category='danger')
        return redirect(url_for('views.dashboard'))
        
    from models import User, BMIRecord
    users = User.query.all()
    user_data = []
    
    for user in users:
        record_count = BMIRecord.query.filter_by(user_id=user.id).count()
        user_data.append({
            'user': user,
            'record_count': record_count
        })
        
    return render_template('admin.html', user_data=user_data)
