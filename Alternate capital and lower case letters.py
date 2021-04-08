# Following function takes a string as input and gives out a string with alternate capital and lowercase letters

def myfunc(string):
    str=list(string)
    ns = []
    for i in range(len(str)):
        if i%2 != 0:
            ns.append(str[i].upper())
        else:
            ns.append(str[i].lower())
    return ''.join(ns)