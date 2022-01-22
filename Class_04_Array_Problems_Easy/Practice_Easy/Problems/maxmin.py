array=[3,4,5,6,7,8,9,10]

def maxmin(arraytest):
    list=[]
    list.append(max(arraytest))
    list.append(min(arraytest))

    return list 

print(maxmin(array))