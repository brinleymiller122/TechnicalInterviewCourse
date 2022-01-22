# Search an array of numbers to find a target number using binary search.
# The function should return the index of the target number if the target number is found
# or a -1 if the target is not found in the array.

input_array = [1, 2, 5, 9, 12, 15, 21, 28, 99, 100, 117]
input_target = 5
# Output = 2

pos=-1

def search(list,n):

    l=0
    u=len(list)-1 

    while l <= u:
        mid= (l+u)//2
        if list[mid] == n:
            globals()['pos']= mid
            return True 
        else: 
            if list[mid] > n:
                u=mid-1
            else:
                l=mid+1

if search(input_array, input_target):
    print(pos)
else:
    print(-1)
