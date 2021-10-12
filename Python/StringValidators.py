string = input()

for i in string:
    if i.isalnum() == True:
        print('True')
        break
else:
    print('False')
for i in string:
    if i.isalpha() == True:
        print('True')
        break
else:
    print('False')
for i in string:
    if i.isdigit() == True:
        print('True')
        break
else:
    print('False')
for i in string:
    if i.islower() == True:
        print('True')
        break
else:
    print('False')
for i in string:
    if i.isupper() == True:
        print('True')
        break
else:
    print('False')