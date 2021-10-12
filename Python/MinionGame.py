# string = input()
# stuart=[]
# kevin = []
# vowels = 'AEIOU'
# for i in range(1,len(string)+1):
#     for j in range(len(string)):
#         if len(string[j:j+i]) == i :
#             if string[j:j+i][0] in vowels:
#                 kevin.append(string[j:j+i])
#             else:
#                 stuart.append(string[j:j+i])
#         else:
#             continue
# if len(stuart) > len(kevin):
#     print(f'Stuart {len(stuart)}')
# elif len(stuart) < len(kevin):
#     print(f'Kevin {len(kevin)}')
# else:
#     print('Draw') 

#This above one fails when there is lenghty word input.

#Correct code can be:
string = input()
vowels = ['A', 'E', 'I', 'O', 'U']
kevin = 0
stuart = 0
for i in range(len(string)):
    if string[i] in vowels:
        kevin = kevin + (len(string)-i)
    else:
        stuart = stuart + (len(string)-i)
if stuart > kevin:
    print('Stuart '+ str(stuart))
elif kevin > stuart:
    print('Kevin ' + str(kevin))
else:
    print('Draw')
