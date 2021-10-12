sights = int(input())
ids = input().split()
uniques = []
finalresult = []
maxx = -1
for i in ids:
    if i not in uniques:
        uniques.append(i)
for j in uniques:
    if maxx < ids.count(j):
        maxx = ids.count(j)
        finalresult = []
        finalresult.append(j)
    if maxx == ids.count(j):
        if all(x > j for x in finalresult):
            finalresult = []
            finalresult.append(j)
print(*finalresult)

# Soln form View Editot=rial:
from collections import Counter
n = input()
arr = Counter(map(int, input().split()))
print(arr.most_common(1)[0][0])
