if __name__ == '__main__':
    s = input()
    lst = list(s)
    alnum = 0
    alpha = 0
    digit = 0
    lower = 0
    upper = 0
    for i in lst:
        if(i.isalnum() == True):
            alnum += 1
        if(i.isalpha() == True):
            alpha += 1
        if(i.isdigit() == True):
            digit += 1
        if(i.islower() == True):
            lower += 1
        if(i.isupper() == True):
            upper += 1
    if (alnum > 0):
        print("True")
    else:
        print("False")
    if (alpha > 0):
        print("True")
    else:
        print("False")
    if (digit > 0):
        print("True")
    else:
        print("False")
    if (lower > 0):
        print("True")
    else:
        print("False")
    if (upper > 0):
        print("True")
    else:
        print("False")
    