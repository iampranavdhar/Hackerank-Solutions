n=int(input())
diagonalelements=[]
crossdiagonalelements=[]
for i in range(n):
    lists=list(input().split()) #the pronlem is the list name can not be change by which we can write as list1,list2,... so we have to gather those req elements to a list and the sum it up.
    a=lists[i]
    diagonalelements.append(a)
    b=lists[-i-1]               #this is bcz i had to get last,and then sec last in 2nd line and so on
    crossdiagonalelements.append(b)

# Now we have to change those lists(diagonalelements and cross..) to int characters.. to add..
for j in range(len(diagonalelements)):
    diagonalelements[j]=int(diagonalelements[j])
for k in range(len(crossdiagonalelements)):
    crossdiagonalelements[k]=int(crossdiagonalelements[k])

# Now adding those lists..

diagonalsum=sum(diagonalelements)
crossdiagonalsum=sum(crossdiagonalelements)

# Printing result....

print(abs(diagonalsum-crossdiagonalsum))

    
