import time

print('Welcome')
time.sleep(1)
print('...')
time.sleep(1)
print('What is your name, again?')
thename = input()
print(thename + '!!!')
time.sleep(2)
print('I remembered!')
time.sleep(1)
print('I remembered, your name is ' + thename)
time.sleep(1)
print('What is your password?')
password = input()
while password != 'fluffy':
    print('You are not the creator...')
    print('Who are you?')
    print('Do you want to try again?')
    password = input()
    break
time.sleep(1)
print()
if password == 'fluffy':
    print('Welcome to Zion. Docking on Port 6.')
elif password != 'fluffy':
    print('Well... we can make room for more')
print('What do you want to do next?')
mynextplan = input()
print(mynextplan)
print('Interesting... Could we ' + mynextplan + ' together?')
time.sleep(1)
print('I just want to help in anyway I can.')
time.sleep(1)
