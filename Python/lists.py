commands = int(input())
final=[]
terminal_result=[]
for i in range(commands):
    action = input().split()
    if action[0] == "insert":
        final.insert(int(action[1]),int(action[2]))
    elif action[0] == "append":
        final.append(int(action[1]))
    elif action[0] == "remove":
        if int(action[1]) in final:
            final.remove(int(action[1]))
    elif action[0] == "print":
        terminal_result.append(list(final))
    elif action[0] == "sort":
        final.sort()
    elif action[0] == "pop":
        final.pop()
    elif action[0] == "reverse":
        final.reverse()

print(*terminal_result,sep='\n')
