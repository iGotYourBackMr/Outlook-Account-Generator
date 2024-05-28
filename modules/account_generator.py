import random
import string
from datetime import datetime

first_names = ["John", "Jane", "Michael", "Emily", "Chris", "Sarah", "David", "Anna", "James", "Laura"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

def generate_random_string(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_username():
    username_length = random.randint(6, 12)
    characters = string.ascii_lowercase + string.digits
    first_char = random.choice(string.ascii_lowercase)
    rest_of_username = generate_random_string(username_length - 1, characters)
    return first_char + rest_of_username

def generate_random_password():
    password_length = random.randint(8, 16)
    characters = string.ascii_letters + string.digits + string.punctuation
    return generate_random_string(password_length, characters)

def generate_random_birth_date():
    start_date = datetime.strptime('1950-01-01', '%Y-%m-%d')
    end_date = datetime.strptime('2024-12-31', '%Y-%m-%d')
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime('%m/%d/%Y')

def generate_random_first_name():
    return random.choice(first_names)

def generate_random_last_name():
    return random.choice(last_names)
