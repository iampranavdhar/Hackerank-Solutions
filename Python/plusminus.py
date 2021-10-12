n=int(input())
result=[]
array=list(input().split())
positivecount=0
negativecount=0
zerocount=0
for i in range(n):
    if int(array[i])>0:
        positivecount=positivecount+1
    elif int(array[i])<0:
        negativecount=negativecount+1
    elif int(array[i])==0:
        zerocount=zerocount+1

if positivecount>0:
    m=format(positivecount/n,'.6f')
    result.append(m)
if positivecount==0:
    c=format(0,'.6f')
    result.append(c)

if negativecount>0:
    l=format(negativecount/n,'.6f')
    result.append(l)
if negativecount==0:
    d=format(0,'.6f')
    result.append(d)

if zerocount>0:
    e=format(zerocount/n,'.6f')
    result.append(e)
if zerocount==0:
    f=format(0,'.6f')
    result.append(f)

print(*result,sep='\n')
      