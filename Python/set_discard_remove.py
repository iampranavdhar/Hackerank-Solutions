numbOfElements = int(input())
s = set(list(map(int,input().split())))
numbOfCommands = int(input())
for i in range(numbOfCommands):
    command  = input().split()
    if len(command) == 1:
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    else:
        s.discard(int(command[1]))
print(sum(s))
