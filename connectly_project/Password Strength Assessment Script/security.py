import re

def evaluate_password_strength(password):
    # Check for weak password criteria
    if len(password) < 8:
        return "Weak"
    if password.islower() or password.isupper():
        return "Weak"
    
    # Check for moderate password criteria
    if 8 <= len(password) < 12:
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password)):
            return "Moderate"
    
    # Check for strong password criteria
    if len(password) >= 12:
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in "!@#$%^&*()-_+=" for c in password)):
            return "Strong"
    
    # If no criteria matched, return Weak
    return "Weak"

# Input from user
password = input("Enter your password: ")
strength = evaluate_password_strength(password)
print(f"Your password strength is: {strength}")
