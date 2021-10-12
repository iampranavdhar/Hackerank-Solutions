def count_substring(string, sub_string):
    words = []
    for i in range(len(string)-len(sub_string)+1):
        words.append(string[i:(i+len(sub_string))])
    return words.count(sub_string)
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)