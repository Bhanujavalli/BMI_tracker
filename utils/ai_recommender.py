def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25.0 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def generate_ai_recommendations(age, gender, bmi_category, bmi_value):
    """
    Simulates an intelligent rule-based AI recommendations engine.
    """
    import random
    
    is_female = (gender.lower() == 'female')
    is_teen = (age < 18)
    is_adult = (18 <= age < 50)
    
    variations = {
        "Underweight": [
            f"With a BMI of {bmi_value}, you are considered Underweight. Your focus should be on building lean muscle mass through a healthy caloric surplus.",
            f"Based on my analysis, at a BMI of {bmi_value}, you are under the recommended weight. Let's focus on structured weight gain.",
            f"Your BMI is {bmi_value} (Underweight). Building lean muscle and achieving a caloric surplus is our top priority."
        ],
        "Normal": [
            f"Great job! Your BMI of {bmi_value} is Normal. Maintaining your balanced diet and current activity level is key.",
            f"Excellent! Your BMI of {bmi_value} indicates you are in a very healthy range. Our goal is to simply solidify these habits.",
            f"Great job maintaining a BMI of {bmi_value}. The AI recommends focusing on longevity, mobility, and peak daytime energy now."
        ],
        "Overweight": [
            f"At a BMI of {bmi_value}, you are considered Overweight. Gradual, sustainable fat loss through a minor caloric deficit is the primary goal.",
            f"Your current BMI is {bmi_value} (Overweight). A gentle, sustainable reduction in daily calories will set you on the right path.",
            f"At {bmi_value} BMI, you are slightly above ideal weight. Let's implement minor dietary tweaks for steady, healthy fat loss."
        ],
        "Obese": [
            f"Your BMI of {bmi_value} indicates Obesity. Prioritize medically supervised, low-impact activities and a monitored caloric deficit.",
            f"At a BMI of {bmi_value}, you are considered Obese. Deep metabolic changes and supervised, joint-safe activity are highly recommended.",
            f"Your BMI is {bmi_value}. Prioritize safe, low-impact movements and strict tracking to regain metabolic control and health."
        ]
    }
    
    # ------------------------------------------------------------------------------
    # UNDERWEIGHT
    # ------------------------------------------------------------------------------
    if bmi_category == "Underweight":
        summary = random.choice(variations["Underweight"])
        risk = "Potential nutritional deficiencies, weakened immune system, and lower energy levels. "
        diet = "• Goal: Healthy Caloric Surplus (+300 to 500 kcal/day)\n• Focus on nutrient-dense meals and liquid calories if you get full quickly."
        
        if is_female:
            risk += "Low body fat can affect hormone regulation and bone density (osteoporosis risk)."
            foods_to_eat = "• Iron-rich foods (spinach, lentils, red meat)\n• Calcium sources (dairy, fortified plant milks)\n• Healthy fats (avocados, nuts)\n• Lean proteins for muscle synthesis"
            foods_to_avoid = "• Empty calories (sugary snacks)\n• Excessive caffeine (can blunt appetite)\n• Highly processed foods"
            if is_teen:
                exercise = "• Focus: Stamina & Strength Foundation\n• Routine: 3 days of beginner-friendly strength training or bodyweight exercises (yoga, pilates)."
                lifestyle = "• Sleep: 8-9 hours for growth and energy.\n• Eat balanced meals without excessive restriction."
                daily_tips = "• Tip: Drink milk or nutrient-dense smoothies alongside your meals.\n• Tip: Have a handful of nuts as a snack between classes or work."
            elif is_adult:
                exercise = "• Focus: Muscle Hypertrophy & Toning\n• Routine: 3-4 days weightlifting focusing on compound movements (squats, deadlifts). Avoid excessive cardio."
                lifestyle = "• Sleep: 7-8 hours for optimal recovery.\n• Manage stress levels which can suppress appetite."
                daily_tips = "• Tip: Incorporate protein shakes if eating solid food is difficult.\n• Tip: Track your meals loosely to ensure you are actually in a surplus."
            else:
                exercise = "• Focus: Joint-Safe Resistance Training & Balance\n• Routine: 2-3 days of light resistance training to prevent bone loss and muscle wasting (sarcopenia)."
                lifestyle = "• Incorporate stretching and prioritize consistent meal timings.\n• Consult a doctor for bone-density screenings."
                daily_tips = "• Tip: Focus on easy-to-digest cooked vegetables and gentle proteins.\n• Tip: Stay hydrated but avoid drinking too much water right before meals."

        else: # Male
            risk += "Risk of decreased muscle mass and overall strength."
            foods_to_eat = "• High-protein sources (chicken breast, eggs, fish)\n• Complex carbs (oats, brown rice, sweet potatoes)\n• Calorie-dense nuts and nut butters"
            foods_to_avoid = "• High-sugar foods\n• Trans fats and heavy fried foods"
            
            if is_teen:
                exercise = "• Focus: Building Strength Basics\n• Routine: Bodyweight exercises (pushups, pullups) or beginner weightlifting 3-4 times a week."
                lifestyle = "• Sleep: 8-9 hours to support natural growth hormones.\n• Consistency is key in eating rather than 'dirty bulking'."
                daily_tips = "• Tip: Eat a hearty breakfast to start your daily caloric intake strong.\n• Tip: Carry mixed nuts or trail mix."
            elif is_adult:
                exercise = "• Focus: Progressive Overload & Muscle Building\n• Routine: 4 days of structured hypertrophy lifting (push/pull/legs). Limit high-intensity cardio."
                lifestyle = "• Sleep: 7-8 hours for muscle recovery.\n• Pair your lifting with adequate protein intake (1.6g-2.2g per kg of bodyweight)."
                daily_tips = "• Tip: Have a protein-rich meal within 2 hours of your workout.\n• Tip: Don't skip meals; meal-prep if necessary."
            else:
                exercise = "• Focus: Safe Strength & Mobility\n• Routine: 3 days of moderate resistance training. Protect your joints by focusing on form over heavy weights."
                lifestyle = "• Ensure heart health is monitored even if underweight.\n• Prioritize joint recovery and consider supplements like Omega-3."
                daily_tips = "• Tip: Add olive oil to your meals for extra calories and heart-health benefits.\n• Tip: Consider a comprehensive health check-up."
                
    # ------------------------------------------------------------------------------
    # NORMAL
    # ------------------------------------------------------------------------------
    elif bmi_category == "Normal":
        summary = random.choice(variations["Normal"])
        risk = "Low risk of weight-related health issues. However, sedentary behavior can still lead to 'skinny fat' (high visceral fat) risks."
        diet = "• Goal: Maintenance & Optimal Nutrition\n• A balanced macronutrient profile (30% protein, 40% carbs, 30% fats)."
        
        foods_to_eat = "• Leafy green vegetables & vibrant fruits\n• Lean proteins and whole grains\n• Healthy fats (nuts, seeds, olive oil)"
        foods_to_avoid = "• Excessive ultra-processed foods\n• Heavy added sugars and high-sodium snacks"
        
        if is_female:
            if is_teen:
                exercise = "• Focus: Variety & Enjoyment\n• Routine: Mix of cardio (dance, sports, cycling) and light bodyweight strength."
                lifestyle = "• Sleep: 8-9 hours for physical and mental wellbeing.\n• Focus on building a healthy relationship with food and your body."
                daily_tips = "• Tip: Stay active by finding a hobby or sport you genuinely enjoy.\n• Tip: Hydrate well, especially during school or college activities."
            elif is_adult:
                exercise = "• Focus: Overall Fitness & Toning\n• Routine: 150 mins moderate cardio + 2 days of full-body strength/yoga per week."
                lifestyle = "• Sleep: 7-8 hours for cellular repair.\n• Aim for 8,000 to 10,000 steps daily."
                daily_tips = "• Tip: Try working at a standing desk or taking short walks during breaks.\n• Tip: Keep added sugars under 25g per day for skin and metabolic health."
                foods_to_eat += "\n• Calcium & Iron sources for women's health."
            else:
                exercise = "• Focus: Longevity, Bone Density & Heart Health\n• Routine: Moderate cardio (brisk walking) 3-4x a week, and 2 sessions of light weight-bearing exercises."
                lifestyle = "• Stress management and regular sleep schedules are vital for hormonal balance.\n• Consider regular screenings for bone density."
                foods_to_eat += "\n• High Calcium, Vitamin D, and Phytoestrogens (soy, flaxseeds) for post-menopausal health."
                daily_tips = "• Tip: Prioritize joint-friendly activities like swimming if you feel stiffness.\n• Tip: Spend 15 minutes a day in the sun for Vitamin D."
                
        else: # Male
            if is_teen:
                exercise = "• Focus: Athletic Foundation\n• Routine: Play team sports, run, or begin basic weightlifting 3-4 times a week."
                lifestyle = "• Stay active and ensure you are eating enough to fuel your activities.\n• Get 8-9 hours of sleep."
                daily_tips = "• Tip: Drink water instead of sodas or energy drinks.\n• Tip: Stretch dynamically before playing sports."
            elif is_adult:
                exercise = "• Focus: Strength & Cardiovascular Endurance\n• Routine: Mix weight training 3x a week with 2 days of cardio (running, cycling)."
                lifestyle = "• Sleep: 7-8 hours.\n• Manage work stress with active hobbies."
                daily_tips = "• Tip: Maintain mobility; stretch your hip flexors and back, especially if you sit a lot.\n• Tip: Aim for 10,000 steps a day."
            else:
                exercise = "• Focus: Heart Health & Muscle Preservation\n• Routine: Regular cardiovascular activity (walking, elliptical) and functional strength training."
                lifestyle = "• Keep an eye on blood pressure and cholesterol even at a normal weight.\n• Focus on mobility to prevent age-related stiffness."
                daily_tips = "• Tip: Avoid eating heavy meals late at night for better sleep and digestion.\n• Tip: Stay consistent with moderate exercise rather than sporadic intense workouts."

    # ------------------------------------------------------------------------------
    # OVERWEIGHT
    # ------------------------------------------------------------------------------
    elif bmi_category == "Overweight":
        summary = random.choice(variations["Overweight"])
        risk = "Elevated risk of developing cardiovascular disease, hypertension, type 2 diabetes, and increased stress on joints."
        diet = "• Goal: Mild Caloric Deficit (-300 to 500 kcal/day)\n• Focus on mindful eating, high-satiety foods, and portion control."
        
        foods_to_eat = "• High-fiber foods (vegetables, legumes, oats)\n• Lean proteins to preserve muscle (chicken breast, fish, tofu)\n• Hydrating foods (cucumber, watermelon)"
        foods_to_avoid = "• Liquid calories (sodas, juices, alcohol)\n• Refined carbohydrates (white bread, pastries)\n• Late-night snacking"
        
        if is_female:
            if is_teen:
                exercise = "• Focus: Fun, Active Movement\n• Routine: Moderate cardio (dancing, swimming, brisk walking) 3-4 days a week. Keep it enjoyable, not punishing."
                lifestyle = "• Focus on how you feel over the number on the scale. Build sustainable habits.\n• Prioritize 8 hours of sleep."
                daily_tips = "• Tip: Drink a glass of water before meals.\n• Tip: Swap sodas for sparkling water or infused fruit water."
            elif is_adult:
                exercise = "• Focus: Fat Loss & Toning\n• Routine: 3-4 days of steady-state cardio (brisk walking, cycling) combined with 2 days of circuit training."
                lifestyle = "• Manage cortisol levels, as high stress can lead to stress-eating and fat retention around the midsection.\n• Aim for 7-8 hours of sleep."
                daily_tips = "• Tip: Meal prep for the week to avoid impulsive fast-food purchases.\n• Tip: Use smaller plates to passively control portions."
            else:
                exercise = "• Focus: Low-Impact Fat Loss & Joint Care\n• Routine: Brisk walking, water aerobics, or elliptical training. Avoid high-impact jumps to protect knees."
                lifestyle = "• Monitor blood sugar and blood pressure.\n• Focus on preserving lean muscle mass with light resistance training."
                daily_tips = "• Tip: Focus on anti-inflammatory foods (berries, fatty fish).\n• Tip: Take a 15-minute walk after lunch and dinner for glycemic control."
                foods_to_eat += "\n• High Calcium and Vitamin D foods for bone protection."
        else: # Male
            if is_teen:
                exercise = "• Focus: Active Lifestyle & Sports\n• Routine: Engage in physical education, intramural sports, or gym routines focusing on overall movement."
                lifestyle = "• Build a routine of physical activity.\n• Avoid crash diets and focus on eating whole, unprocessed foods."
                daily_tips = "• Tip: Limit screen time to encourage more physical movement throughout the day.\n• Tip: Choose grilled items over fried items when eating out."
            elif is_adult:
                exercise = "• Focus: Cardiovascular Health & Fat Burning\n• Routine: Weightlifting 3x a week to increase resting metabolic rate + 2-3 sessions of Zone 2 cardio."
                lifestyle = "• Avoid excessive alcohol, which contributes heavily to visceral fat (belly fat).\n• Ensure adequate sleep."
                daily_tips = "• Tip: Try intermittent fasting (e.g., 16:8) if it fits your lifestyle to help control daily calorie intake.\n• Tip: Stand up and move for 5 minutes every hour."
            else:
                exercise = "• Focus: Low-Impact Cardio & Core Strength\n• Routine: Daily walking, cycling, or swimming. Incorporate core exercises to support back health."
                lifestyle = "• Regular cardiovascular checkups are highly recommended.\n• Be mindful of joint stress; ensure proper footwear."
                daily_tips = "• Tip: Keep your sodium intake low to help manage blood pressure.\n• Tip: Substitute red meat with fish or poultry a few days a week."

    # ------------------------------------------------------------------------------
    # OBESE
    # ------------------------------------------------------------------------------
    else: # Obese
        summary = random.choice(variations["Obese"])
        risk = "High risk for chronic conditions including severe heart disease, sleep apnea, type 2 diabetes, osteoarthritis, and metabolic syndrome."
        diet = "• Goal: Strictly Monitored Caloric Deficit\n• Strategy: Track meals diligently, aim for volume eating (high bulk, low calorie)."
        
        foods_to_eat = "• Volume foods: vast amounts of leafy greens, broccoli, zucchini\n• Lean proteins: egg whites, turkey, white fish\n• High-water-content fruits (berries, melon)"
        foods_to_avoid = "• All ultra-processed foods and fast food\n• High-saturated fats and all trans fats\n• Liquid calories, heavy dressings, and sauces"
        
        if is_female:
            if is_teen:
                exercise = "• Focus: Safe, Gentle Movement\n• Routine: Daily walking or swimming. Avoid activities that cause joint pain."
                lifestyle = "• Engage a pediatrician or registered dietitian for a healthy, unrestrictive path forward.\n• Focus on establishing self-esteem and healthy coping mechanisms."
                daily_tips = "• Tip: Involve your family in cooking healthy meals together.\n• Tip: Start with just 15 minutes of movement a day and slowly increase."
            elif is_adult:
                exercise = "• Focus: Joint-Safe Caloric Burn\n• Routine: Low-impact cardio (stationary bike, elliptical, water aerobics) 4-5 times a week."
                lifestyle = "• Seek support groups or a fitness coach for accountability.\n• Have yourself checked for PCOS or thyroid issues if weight loss is unusually difficult."
                daily_tips = "• Tip: Focus on whole, unprocessed foods and log what you eat for accountability.\n• Tip: Drink a full glass of water when you feel hungry outside of meal times."
            else:
                exercise = "• Focus: Supervised Low-Impact Movement\n• Routine: Gentle walking, chair exercises, or hydrotherapy to protect joints entirely."
                lifestyle = "• Consult your physician before beginning any exercise routine.\n• Monitor for joint pain and stop if you experience acute discomfort."
                daily_tips = "• Tip: Split your meals into 4-5 small portions to keep metabolism active without overeating.\n• Tip: Prioritize sleep, as poor sleep severely hampers fat loss."
                risk += " Very high priority to monitor for osteoarthritis and cardiovascular strain."
        else: # Male
            if is_teen:
                exercise = "• Focus: Unloading Joints & Consistent Activity\n• Routine: Swimming, cycling, or brisk walking. Find activities that don't cause pain."
                lifestyle = "• Work with family to remove junk food from the house.\n• Start building habits without extreme diets."
                daily_tips = "• Tip: Replace sugary drinks with water entirely—this is the biggest first step.\n• Tip: Focus on how much stronger you are getting."
            elif is_adult:
                exercise = "• Focus: Weight Management & Metabolic Health\n• Routine: Blend stationary bike or elliptical work with basic weight training (seated machines) to preserve muscle mass."
                lifestyle = "• Monitor for sleep apnea if you experience loud snoring or chronic daytime fatigue.\n• Consult a doctor for blood panels."
                daily_tips = "• Tip: Reduce alcohol consumption strictly, as it hinders liver function and fat loss.\n• Tip: Aim for progress, not perfection—consistency over intensity."
            else:
                exercise = "• Focus: Cardiovascular Protection & Gentle Movement\n• Routine: Walking in water (hydrotherapy) or recumbent bike to alleviate knee and back load."
                lifestyle = "• Medical supervision is advised for weight loss programs.\n• Focus aggressively on blood pressure management."
                daily_tips = "• Tip: Avoid eating heavy meals late at night.\n• Tip: Work with a dietician to ensure your deficit still provides necessary micronutrients."

    return {
        "risk": risk.strip(),
        "diet": diet.strip(),
        "foods_to_eat": foods_to_eat.strip(),
        "foods_to_avoid": foods_to_avoid.strip(),
        "exercise": exercise.strip(),
        "lifestyle": lifestyle.strip(),
        "daily_tips": daily_tips.strip(),
        "summary": summary.strip()
    }
