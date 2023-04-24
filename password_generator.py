# Random Password Generator
# project status = Finished
# importing the random module 
import random

# welcoming message
print("welcome to random password generator")

# all the things that is included in the password 
strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symbols = ['?', '!', ':', '*', '$', '@', '+', '-', '&', '_', '/', '\\', '∆', '¶', '×', '÷', 'π', '√', '•', '|', '`', '~', '£', '¢', '€', '¥', '^', '°', '=', '\\', '%', '©', '®', '™', '✓', '#']

# asking the user to the length of letters/nums/symbols

letter = int(input("how many letters do you want in the password ? "))

num = int(input("how many numbers do you want in the password ? "))

symbol = int(input("how many special symbols do you want in the password ? "))

# asking the user if he wants a small or captial letters in the password

captial_or_small = input("do you want captial or small letters ?")

if captial_or_small.lower() == 'captial':
	strings = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	
else:
	None
	
random_letter = random.choices(strings, k=letter)


random_num = random.choices(nums, k=num)

random_symbol = random.choices(symbols, k=symbol)

random_password = random_letter +  random_num + random_symbol
random.shuffle(random_password)

print('' .join(random_password))
