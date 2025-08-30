import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True, exclude_chars=""):
    if not (use_letters or use_numbers or use_symbols):
        raise ValueError("At least one character set must be selected!")

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Remove excluded characters
    for ch in exclude_chars:
        characters = characters.replace(ch, "")

    if not characters:
        raise ValueError("No characters left to generate password. Adjust your settings.")

    return ''.join(random.choice(characters) for _ in range(length))

# ✅ User Input Handling
try:
    length = int(input("Enter password length (min 4): "))
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    use_letters = input("Include letters? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_letters, use_numbers, use_symbols,)
    print("\n✅ Generated Password:", password)

except Exception as e:
    print("Error:", e)
