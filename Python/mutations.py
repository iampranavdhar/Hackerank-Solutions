string = input()
conditions = input().split()
string = list(string)
string[int(conditions[0])] = conditions[1]
string = ''.join(string)
print(string)