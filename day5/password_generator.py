import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to Password generator")
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like : \n"))
num_of_numbers = int(input("How many numbers would you like :\n"))

# Easy Case

# password = ""
# for i in range(0,num_of_letters,1):
#   random_number = random.randint(0,52)
#   password += letters[random_number]

# for i in range(0,num_of_symbols,1):
#   random_number = random.randint(0,8)
#   password += symbols[random_number]

# for i in range(0, num_of_numbers,1):
#   random_number = random.randint(0,9)
#   password += numbers[random_number]

# print(password)

# Hard Case
password_list = []
for i in range(0,num_of_letters,1):
  random_number = random.randint(0,52)
  password_list.append(letters[random_number])

for i in range(0,num_of_symbols,1):
  random_number = random.randint(0,8)
  password_list.append(symbols[random_number])

for i in range(0, num_of_numbers,1):
  random_number = random.randint(0,9)
  password_list.append(numbers[random_number])

print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char
print(password)
