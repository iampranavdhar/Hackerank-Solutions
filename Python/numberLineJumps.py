x1,v1,x2,v2 = list(map(int,input().split()))
if  (v1-v2) != 0 and (x2-x1)/(v1-v2) > 0 and (x2-x1)/(v1-v2) == (x2-x1)//(v1-v2):
    print('YES')
else:
    print('NO')

