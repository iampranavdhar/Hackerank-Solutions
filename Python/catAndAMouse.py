testcases =int(input())
result = []
for i in range(testcases):
    x,y,z = map(int,input().split())
    if abs(z-x) > abs(z-y):
        result.append('Cat B')
    elif abs(z-x) < abs(z-y):
        result.append('Cat A')
    elif abs(z-x) == abs(z-y):
        result.append('Mouse C')
print('\n'.join(result))