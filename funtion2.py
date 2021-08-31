def countdown(num):
    newlist = []
    for i in range(num, -1 ,-1):
        newlist.append(i)
    return newlist

print(countdown(5))

def pandr(num,num2):
    print(num)
    return(num2)

print(pandr(1,2))

def fplusl(list):
    return list[0] + len(list)

print(fplusl([1,2,3,4,5]))

def vgthans(list):
    count = 0
    temp = []
    for i in list:
        if i >= list[2]:
            count+=1
            temp.append(i)
    if count < 2:
        return bool(False)
    else:
        print(count)
        return temp

print(vgthans([5,2,3,2,1,4]))

def tltv(length,value):
    funny = []
    for i in range(0,length):
        funny.append(value)
    return funny

print(tltv(4,7))
