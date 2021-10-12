from itertools import combinations
list1 = input().split()
n = int(list1[1])
for i in range(1,n+1):
    temp=list(combinations(list1[0],i))
    temp2=[]
    final=[]
    for i in range(len(temp)):
        temp2.append(list(temp[i]))








        
    # for i in range(len(temp2)):
    #     string = ''
    #     for j in range(len(temp2[i])):
    #         string += temp2[i][j]
    #     final.append(string)
    # final.sort()
    # print(*final,sep='\n')