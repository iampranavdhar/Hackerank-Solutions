def merge_the_tools(string, k):
    n = len(string)
    for i in range(0,n-k+1,k):
        word=''
        temp = string[i:i+k]
        for j in temp:
            if j not in word:
                word += j
        print(word)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)