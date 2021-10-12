numb = int(input())
arr = input().split()
unique = []
pairs = 0
for i in arr:
    if(i not in unique):
        unique.append(i)
for i in unique:
    if arr.count(i)%2 == 0:
        pairs+=(arr.count(i)/2)
    else:
        pairs+=((arr.count(i)-1)/2)
print(int(pairs))

