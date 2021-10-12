n,k = map(int,input().split())
array = list(map(int,input().split()))
cnt = 0
max_hurdle = max(array)
if max_hurdle > k:
    cnt = cnt + (max_hurdle - k)
print(cnt)
