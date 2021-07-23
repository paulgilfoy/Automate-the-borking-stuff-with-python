spam = []
while True:
    print('Enter your shopping list (or enter nothing to stop):')
    items = input()
    if items == '':
        break
    spam = spam + [items]

shoppinglist = spam[0]
for item in spam[1:len(spam)-1]:
    shoppinglist = shoppinglist + ', ' + item
shoppinglist = shoppinglist + ', and ' + spam[-1]
print('My shopping list is ' + shoppinglist)
