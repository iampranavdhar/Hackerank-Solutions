testcases=int(input())
for i in range(testcases):
    n = int(input())
    a=1
    for i in range(1,n+1):
        if(i%2==0 and i!=0):
            a=a+1
        elif(i%2!=0):
            a=a*2
    print(a)
