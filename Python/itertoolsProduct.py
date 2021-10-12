from itertools import product
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
final=list(product(list1,list2))
print(*final,sep=' ')