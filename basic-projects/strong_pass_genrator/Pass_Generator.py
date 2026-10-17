import random

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','$','%','&','*','(',')']

print("WELCOME! TO THE STRONG PASSWORD GENERATOR\n")
letter=int(input("How many letter you want in password_list\n"))
num=int(input("How many numbers you want in password_list\n"))
symb=int(input("How mant symbols do you want in password_list\n"))

# easy level
# password_list=""
# for char in range(1,letter+1):
#     password_list+=random.choice(alphabets)
# for char in range(1,num+1):
#     password_list+=random.choice(numbers)
# for char in range(1,symb+1):
#     password_list+=random.choice(symbols)
# print(password_list)

# Hard  level
password_list=[]
for char in range(1,letter+1):
    password_list+=random.choice(alphabets)
for char in range(1,num+1):
    password_list+=random.choice(numbers)
for char in range(1,symb+1):
    password_list+=random.choice(symbols)
# print(password_list)
random.shuffle(password_list)
# print(password_list)
password=""
for char in password_list:
    password += char
print(f"Your Password is : {password}")
