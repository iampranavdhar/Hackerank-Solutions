n,k,q=map(int,input().split())
elements = list(map(int,input().split()))
for i in range(k):
    temp=elements[-1]
    elements.remove(temp)
    elements.insert(0,temp)
for i in range(q):
    index = int(input())
    print(elements[index])
