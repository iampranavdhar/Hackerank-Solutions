testcases = int(input())
finalresults={}
for i in range(testcases):
    lists = input().split()
    summ=0
    for i in range(1,4):
        summ+=float(lists[i])
    avgg=summ/3
    finalresults[lists[0]] = avgg
avg_needed = input()
print('%.2f'%finalresults[avg_needed])