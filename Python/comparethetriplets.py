alicelist=list(input().split(' '))
bobslist=list(input().split(' '))
alicecount=0
bobscount=0
for i in range(len(alicelist)):
    if int(alicelist[i])>int(bobslist[i]):
        alicecount=alicecount+1
    elif int(alicelist[i])<int(bobslist[i]):
        bobscount=bobscount+1
print(f'{alicecount} {bobscount}')
