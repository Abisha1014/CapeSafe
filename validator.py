import re

COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "password123",
    "hello123",
}

MIN_LENGTH = 8
SPECIAL_CHARACTERS = r"[!@#$%^&*(),.?\":{}|<>_\-+=~`\[\]\\/;']"


def check_length(password: str) -> bool:
    return len(password) >= MIN_LENGTH


def check_uppercase(password: str) -> bool:
    return any(char.isupper() for char in password)


def check_lowercase(password: str) -> bool:
    return any(char.islower() for char in password)


def check_number(password: str) -> bool:
    return any(char.isdigit() for char in password)


def check_special_character(password: str) -> bool:
    return bool(re.search(SPECIAL_CHARACTERS, password))


def check_common_password(password: str) -> bool:
    return password.lower() not in COMMON_PASSWORDS


def validate_password(password: str):
  
    checks = [
        (check_length(password), f"Password must be at least {MIN_LENGTH} characters long."),
        (check_uppercase(password), "Password must contain at least one uppercase letter."),
        (check_lowercase(password), "Password must contain at least one lowercase letter."),
        (check_number(password), "Password must contain at least one number."),
        (check_special_character(password), "Password must contain at least one special character."),
        (check_common_password(password), "Password is too common / easily guessed."),
    ]

    failed_rules = [message for passed, message in checks if not passed]
    is_valid = len(failed_rules) == 0

    return is_valid, failed_rules

MAX_ATTEMPTS = 3

def main():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        password = input("Enter a password to validate: ")
        is_valid, failed_rules = validate_password(password)

        if is_valid:
            print("\n Valid password!")
            return

        attempts += 1
        print("\n Invalid password!")
        if attempts == 1:
            print("\n Incorrect password. Please try again.")
        elif attempts == 2:
            print("\n Incorrect password. 1 attempt remaining.")
        elif attempts == 3:
            print("\n Too many failed attempts. Account temporarily locked for security. Please try again later.")


if __name__ == "__main__":
    main()