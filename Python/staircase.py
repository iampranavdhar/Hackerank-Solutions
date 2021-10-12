n=int(input())
for i in range(n):

#--------------------------------------------------------------------------------------------------------------
# We can't use this code:
#   print(' '*(n-i))
#   print('#'*(i+1))
#--------------------------------------------------------------------------------------------------------------
    spaces=' '*(n-(i+1)) #here also we can't use i directly n-0=n but we want n-1 so we use n-(i+1)
    hashes='#'*(i+1) #here we can't write as ('#'*i) as i starts from zero
    print(f'{spaces}{hashes}')