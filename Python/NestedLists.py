N=int(input())
allnames=[]
allmarks=[]
uniquemarks=[]
finalnames=[]
for i in range(N):
    name=input()
    marks=float(input())
    allmarks.append(marks)
    allnames.append(name)
for i in allmarks:
    if i not in uniquemarks:
        uniquemarks.append(i)
uniquemarks.sort()
secondmark=uniquemarks[1]
for i in range(len(allmarks)):
    if allmarks[i]==secondmark:
        finalnames.append(allnames[i])
finalnames.sort()
print(*finalnames,sep='\n')

#Logic
#I am pushing to sep lists and then i am 
#removing duplicates of marks and sending 
#to uniq lists and then from that i am 
#taking the second least score and i am 
#seeing in which index is it present in 
#the allmarks list and then printing 
#names according to that corresponding index.


