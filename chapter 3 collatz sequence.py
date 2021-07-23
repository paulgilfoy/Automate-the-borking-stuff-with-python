import time

def collatz(number):
    while number != 1:
        if int(number) % 2 == 0:
            number = number // 2
            print(str(number))
        elif int(number) % 2 == 1 :
            number = 3 * number + 1
            print(str(number))


print('Hello.')
time.sleep(0.4)
print('This is my even and odd game. I hope you enjoy')
print('Enter number:')
number = input()
number = int(number)
collatz(number)

print('wasnt that interesting?')
time.sleep(5)
print('again?')
