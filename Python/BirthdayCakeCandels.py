#----------------------------------------------
# n= int(input())
# candles = list(map(int,input().split()))
# maxx = max(candles)
# count = 0
# for i in range(len(candles)):
#     if candles[i] == maxx:
#         count = count + 1
# print(count)

#--------------------------------------------------

n= int(input())
candles = list(map(int,input().split()))
maxx = max(candles)
print(candles.count(maxx))
