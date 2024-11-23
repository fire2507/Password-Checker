import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    feedback = []

    if length_criteria:
        feedback.append("Password length is sufficient.")
    else:
        feedback.append("Password length should be at least 8 characters.")

    if uppercase_criteria:
        feedback.append("Password contains uppercase letters.")
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if lowercase_criteria:
        feedback.append("Password contains lowercase letters.")
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if number_criteria:
        feedback.append("Password contains numbers.")
    else:
        feedback.append("Password should contain at least one number.")

    if special_char_criteria:
        feedback.append("Password contains special characters.")
    else:
        feedback.append("Password should contain at least one special character.")

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    strength = "Very Weak"
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    
    print("Password Strength: ", strength)
    print("Feedback:")
    for message in feedback:
        print("-", message)
password = input("Enter a password to assess: ")
assess_password_strength(password)
