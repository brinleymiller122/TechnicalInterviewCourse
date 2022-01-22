#binary search 

def search(list,n):
    l=0
    u=len(list)-1

    while l <= u:
        mid = (l+u)//2
        if list[mid]== n:
            return True
        else:
            if list[mid] > n:
                u=mid-1
            else: 
                l=mid+1
list=[1,55,66,77,88,99,100,120]
n=78

if search(list,n):
    print("FOUND")
else:
    print("Not FOund")

            