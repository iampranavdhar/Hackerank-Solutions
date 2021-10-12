testcases = int(input())
for i in range(testcases):
    n,m,s = map(int,input().split())
    if (m-(n-s) <= 0):
        print((s+(m-1)))
    else:
        left=m-(n-(s-1))
        num=left%n
        if(num==0):
            print(n)
        else:
            print(num)
#Own :)

# Here what i am doing is first counting the left sweets after starting from the specific numb and then as it starts from starting itself getting the seets that are left after completely dividing those

        
    
    

