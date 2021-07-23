import webbrowser

print('What is the address?')
address = input()

address = address.split(' ')

search = 'https://google.com/maps/place/' + address[0]

for i in address[1:]:
    search = search + '+' + i

webbrowser.open(search)
