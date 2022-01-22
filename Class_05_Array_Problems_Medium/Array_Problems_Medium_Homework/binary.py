
list=[1,3,5,7,8,9,99,100]
n=9

def search(list,n):
    l=0
    u=len(list)-1

    while l <= u:
        mid=(l+u)//2
        if list[mid] == n:
            return mid
        else:
            if list[mid] < n:
                l= mid+1
            else:
                u=mid-1
    return -1

print(search(list,n))

array=[3,4,5,6,1,2]