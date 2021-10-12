def swap_case(s):
    new = ''
    for i in s:
        if ord(i)>= 65 and ord(i) <=  90:
            new += i.lower()
        elif ord(i) >= 97 and ord(i) <= 122:
            new += i.upper()
        else:
            new += i
    return new 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)