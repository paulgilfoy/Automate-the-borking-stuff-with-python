import time
name = ''
while name == '':
    print('Please type your name')
    name = input()
print('Thank You')
password1 = ''
while password1 == '':
    print('Please choose your password')
    password1 = input()
password2 = ''
while password2 != password1:
    print('Please confirm your password')
    password2 = input()
print('Password accepted')
time.sleep(1)
print('Please continue')
time.sleep(1)
print('Welcome to Zion')


    
