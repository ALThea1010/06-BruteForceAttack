"""
Assessment1-Programming-Skills-Portfolio Exercise 6: Brute Force Attack
"""


import itertools
import string

# Define the correct password
CORRECT_PASSWORD = 'meow'
MAX_ATTEMPTS = 5

def bruteforce_attack(password):
    chars = string.printable.strip()  # All printable characters
    attempts = 0
    # Brute-force attack simulation
    for length in range(1, len(password) + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return (attempts, guess)
    return (attempts, None)

def brute_force_guesser(target, guess='', counter=0):
    if len(guess) == len(target):
        counter += 1
        if guess == target:
            return True, counter
        return False, counter
    else:
        for c in string.ascii_lowercase:  # Using lowercase letters only
            target_found, counter = brute_force_guesser(target, guess + c, counter)
            if target_found:
                return True, counter
        return False, counter

# Function to simulate password entry system
def password_entry_system():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        user_input = input("Enter the password: ")
        
        if user_input == CORRECT_PASSWORD:
            print("Access granted. Correct password entered.")
            return  # Exit the function on correct password
        else:
            attempts += 1
            remaining_attempts = MAX_ATTEMPTS - attempts
            if remaining_attempts > 0:
                print(f"Incorrect password. You have {remaining_attempts} attempts left.")
            else:
                print("Maximum attempts reached. Authorities have been alerted.")

# Call the password entry system
password_entry_system()
