import random 

print('Welcomee to password generator')

chars ='asdfghjklqwertyuiopzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*().,'

number = input('Amouont of passwords you want  ')
number = int(number)

length = input('Input your password length.')
length = int(length)

print('\n these are passwords')

for pwd  in range(number):
    passwords = ''
    for c in range(length):
         passwords += random.choice(chars)
    print(passwords)
