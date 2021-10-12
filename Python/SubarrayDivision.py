bars = int(input())
bar_numb = list(map(int,input().split()))
summ,barlen = input().split()
summ = int(summ)
barlen = int(barlen)
count = 0
for i in range(len(bar_numb)-barlen+1):
    add = 0
    for j in range(barlen):
        add += bar_numb[i+j]
    if add == summ:
        count += 1
print(count)
