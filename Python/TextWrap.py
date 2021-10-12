string = input()
list(string)
final = []
num = int(input())
left = len(string)% num
for i in range(0,len(string)-left,num):
    wraped = ''
    for j in range(num):
        wraped += string[i+j]
    final.append(wraped)
left_word = ''
for j in range(len(string)-left,len(string)):
    left_word += string[j]
final.append(left_word)
print(*final,sep='\n')




