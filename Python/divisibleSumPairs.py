n,k = input().split()
n = int(n)
k = int(k)
count = 0
numbers = list(map(int,input().split()))
for i in range(len(numbers)-1):
    for j in range(i+1,len(numbers)):
        if (numbers[i] + numbers[j]) % k == 0:
            count += 1
print(count)