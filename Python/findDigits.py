testcases = int(input())
for i in range(testcases):
    num = input()
    digits = []
    count = 0
    for i in range(len(num)):
        if(int(num[i]) != 0):
            digits.append(num[i])
    for i in digits:
        if int(num)%int(i) == 0:
             count+=1
    print(count)
