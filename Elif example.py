import time

print('The first test shall commence')
time.sleep(1)
print('What is your name')
name = input()
time.sleep(1)
print('Very interesting')
time.sleep(1)
print('What is your age')
age = input()
if name == 'Alice':
    print('Hi Alice')
elif int(age) < 12:
    print('You are not who I thought you were. Sorry Kiddo')
elif int(age) > 2000:
    print('Unlike you, alice is not an undead, immportal vampire')
elif int(age) > 100:
    print('You are not Alice, granny')
elif int(age) > 12:
    print('This was made for Alice. I dont know who you are')
