def passwordStrenght(pas):
    has_lower = any(c.islower() for c in pas)
    has_upper = any(c.isupper() for c in pas)
    has_digit = any(c.isdigit() for c in pas)
    has_special = any(not c.isalnum() for c in pas)

    strength = sum([has_digit,has_lower,has_special,has_upper])

    if len(pas) < 6 or strength < 1:
        print("week") 
    elif strength < 3:
        print("medium")
    else:
        print("strong")

passwordStrenght("lourdu02@")