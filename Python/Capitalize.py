# string = input()
# lists = string.split()
# print(lists)
# final = []
# for i in lists:
#     if ord(i[0]) >= 97 and ord(i[0]) <= 122:
#         char=list(i)
#         char[0] = char[0].upper()
#         final.append(''.join(char))
#     else:
#         final.append(i)
# print(*final,sep=' ')

#Changed to this code bcz the spaces matter.

string = input()
lists = list(string)
lists[0] = lists[0].upper()
for i in range(2,len(lists)):
    if ord(lists[i]) >= 97 and ord(lists[i]) <= 122 and lists[i-1] == ' ':
        lists[i] = lists[i].upper()
print(''.join(lists))
