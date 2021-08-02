# Password Generator
import random
print("Welcome to Password Generator")

total_letters = int(
    input("How many letters would you like in your password?\n"))
total_digits = int(input("How many digits would you like in your password?\n"))
total_symbols = int(
    input("How many symbols would you like in your password?\n"))


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []
for char in range(1, total_letters + 1):
    random_letter = random.choice(letters)
    password_list.append(random_letter)

# print(password_list)

for num in range(1, total_digits + 1):
    random_digit = random.choice(numbers)
    password_list.append(random_digit)
# print(password_list)

for symbol in range(1, total_symbols + 1):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password = password + char 
print(f"Your password is {password}")
