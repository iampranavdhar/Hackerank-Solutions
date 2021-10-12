numbers=[5,2,5,2,2]
for i in range(len(numbers)):
    xlist=[]
    for j in range(numbers[i]):
        m='x'
        xlist.append(m)
    print(*xlist,sep='')

# we can directly write as:
#numbers=[5,2,5,2,2]
#for i in numbers
#print('x'*i)
