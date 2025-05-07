def main():
    # get the name
    sName = input("Enter full name such as John Smith: ")

    # getting the initials
    FIRST_SPACE = 0
    while FIRST_SPACE < len(sName) and sName[FIRST_SPACE] != ' ':
        FIRST_SPACE += 1
    sInitials = sName[0].upper() + sName[FIRST_SPACE + 1].upper()

    # keep asking for a pass
    while True:
        sPassword = input("Enter new password: ")
        errors = []  # storing errors, will append errors.

        # checking the pass length
        count = 0
        for char in sPassword:
            count += 1
        if count < 8 or count > 12:
            errors.append("Password must be between 8 and 12 characters.")

        # checking if the password starts with "pass" or "Pass"
        if sPassword[:4].lower() == "pass":
            errors.append("Password can't start with Pass.")

        # validating if pass has at least 1 uppercase letter
        HAS_UPPER = False
        for char in sPassword:
            if 'A' <= char <= 'Z':
                HAS_UPPER = True
                break  
        if not HAS_UPPER:
            errors.append("Password must contain at least 1 uppercase letter.")

        # validating if pass has at least 1 lowercase letter
        HAS_LOWER = False
        for char in sPassword:
            if 'a' <= char <= 'z':
                HAS_LOWER = True
                break
        if not HAS_LOWER:
            errors.append("Password must contain at least 1 lowercase letter.")

        # validating if pass has at least 1 number
        HAS_DIGITS = False
        for char in sPassword:
            if '0' <= char <= '9':
                HAS_DIGITS = True
                break
        if not HAS_DIGITS:
            errors.append("Password must contain at least 1 number.")

        # checking if pass has at least 1 special character
        special_chars = "!@#$%^"
        HAS_SPECIAL = False
        for char in sPassword:
            if char in special_chars:
                HAS_SPECIAL = True
                break
        if not HAS_SPECIAL:
            errors.append("Password must contain at least 1 of these special characters: ! @ # $ % ^")

        # checking if pass has user initials
        if sInitials.lower() in sPassword.lower():
            errors.append("Password must not contain user initials.")

        # checking for repeated characters
        CHAR_COUNTS = {}
        for char in sPassword:
            LOWER_CHAR = char.lower()
            if LOWER_CHAR in CHAR_COUNTS:
                CHAR_COUNTS[LOWER_CHAR] += 1
            else:
                CHAR_COUNTS[LOWER_CHAR] = 1

        REPEATED_CHARS = [f"{char}: {count} times" for char, count in CHAR_COUNTS.items() if count > 1]

        if REPEATED_CHARS:
            errors.append("These characters appear more than once:")
            errors.extend(REPEATED_CHARS)

        # displaying errors and resetting loop. 
        if errors:
            print("\n".join(errors))
        else:
            print("Password is valid and OK to use.")
            break  # exit if passed all checks



main()
# it wasent on the assignment instructions but i used dictionary/sets to help me out with this
