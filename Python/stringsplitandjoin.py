string=input()
string=string.split(" ")
print(*string,sep='-')

#or
#----------------------------------------

def split_and_join(line):
    # write your code here
    words=line.split(' ')
    return "-".join(words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)