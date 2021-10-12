array=list(input().split())
lists=[]
minmaxlist=[]
for i in range(len(array)):
    sum=0
    for j in range(len(array)):
        if j != i:
            sum=sum+int(array[j])
    lists.append(sum)
minvalue=min(lists)
maxvalue=max(lists)
print(f"{minvalue} {maxvalue}")

    