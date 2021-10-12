n,k = map(int,input().split())
billamt = list(map(int,input().split()))
amtcharged = int(input())
summ = sum(billamt)
returnamt = amtcharged - ((summ - billamt[k])/2)
if returnamt == 0:
    print("Bon Appetit")
else:
    print(int(returnamt))