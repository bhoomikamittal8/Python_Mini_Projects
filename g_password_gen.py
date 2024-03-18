letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

import random

print("Welcome to Password Generator!")
let = int(input("How many Letters would you like in your Password?\n"))
sym = int(input("How many Symbols would you like in your Password?\n"))
numb = int(input("How many Numbers would you like in your Password?\n"))

password_list = []
for char in range(1, let + 1):
    password_list += random.choice(letters)

for char in range(1, sym + 1):
    password_list += random.choice(symbols)

for char in range(1, numb + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is: {password}")
