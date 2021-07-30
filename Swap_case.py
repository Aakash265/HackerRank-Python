def swap_case(s):
    lst = []
    for i in range(len(s)):
        if (s[i].isupper() == True):
            temp = s[i].lower()
            lst.append(temp)
        elif (s[i].islower() == True):
            temp = s[i].upper()
            lst.append(temp)
        else:
            lst.append(s[i])
    result = "".join(lst)
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)