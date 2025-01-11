#password generator

import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    # Create a pool of characters based on user preferences
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation
    
    # Ensure the character pool is not empty
    if not character_pool:
        raise ValueError("At least one character type must be selected.")
    
    # Generate a random password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # User Input: Desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    # User Input: Complexity options
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate Password
    try:
        generated_password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        # Display the Password
        print(f"\nGenerated Password: {generated_password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
