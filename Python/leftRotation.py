n,d=map(int,input().split())
arr = list(map(int,input().split()))
for i in range(d):
    temp=arr[0]
    arr.remove(temp)
    arr.insert(len(arr),temp)
print(*arr,sep=' ')