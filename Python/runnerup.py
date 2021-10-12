n=int(input())
if n>=2 and n<=10:
    scores=list(map(int,input().split()))
    uniques=[]
    for score in scores:
        if score not in uniques:
            uniques.append(score)
    uniques.sort()
    if len(uniques)>=2:
        print(uniques[-2])
    else:
        print(uniques[0])




