from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from models import User, db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.dashboard'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user, remember=True)
            flash('Logged in successfully.', category='success')
            return redirect(url_for('views.dashboard'))
        else:
            flash('Invalid username or password.', category='danger')

    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('views.dashboard'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        age = request.form.get('age', type=int)
        gender = request.form.get('gender')
        height = request.form.get('height', type=float)

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists.', category='danger')
        elif not age or age <= 0 or not height or height <= 0:
            flash('Valid age and height are required.', category='danger')
        elif len(password) < 6:
            flash('Password must be at least 6 characters.', category='danger')
        else:
            new_user = User(
                username=username, 
                password_hash=generate_password_hash(password, method='scrypt'),
                age=age,
                gender=gender,
                height=height
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfully!', category='success')
            return redirect(url_for('views.dashboard'))

    return render_template('register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', category='success')
    return redirect(url_for('auth.login'))
