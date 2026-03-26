def validate_body_metrics(user, new_age, new_height):
    """
    Validates if the incoming age and height changes are realistic.
    Returns (True, None) if valid.
    Returns (False, Error_Message) if invalid / suspicious.
    """
    if new_height <= 0 or new_age <= 0:
        return False, "Height and age must be strictly positive values."
        
    # Validation 1: Height should not fluctuate wildly once set for an adult
    # Requirement: "If user first entered height = 153 cm... Later if same user enters height = 170 cm... system should detect this as suspicious"
    height_diff = abs(user.height - new_height)
    if user.age >= 18 and height_diff > 3.0:
         return False, f"Validation Error: Suspicious data entry. Adult height naturally does not change significantly. Your previous height was {user.height} cm. Please update your profile if this is an error."
    elif height_diff > 15.0:
         return False, f"Validation Error: Height change of {height_diff} cm from previous log ({user.height} cm) is unrealistic."
        
    # Validation 2: Age should not decrease or increase unrealistically compared to creation
    if new_age < user.age:
        return False, "Validation Error: Age cannot decrease over time."
    if (new_age - user.age) > 2:
        return False, "Validation Error: Age increased too rapidly compared to your last update."
        
    return True, None

def check_weight_change_warning(last_weight, new_weight):
    """
    Returns a warning message if the weight changes unrealistically fast.
    Expected to be a soft warning flashed in UI, not a hard block.
    """
    if last_weight is None or new_weight is None:
        return None
        
    diff = abs(float(last_weight) - float(new_weight))
    
    if float(diff) > 5.0:
        return f"Warning: Your weight has changed significantly ({round(float(diff), 1)} kg) in a short time period. Please verify your input."
        
    return None
