def breakingRecords(scores):
    minm = scores[0]
    maxm = scores[0]
    minm_count = 0
    maxm_count = 0
    for i in scores:
        if i > maxm :
            maxm = i
            maxm_count = maxm_count + 1
        if i < minm:
            minm = i
            minm_count = minm_count + 1
    return [maxm_count,minm_count]


n = int(input())
scores = list(map(int, input().rstrip().split()))
result = breakingRecords(scores)
print(*result,sep= ' ')
