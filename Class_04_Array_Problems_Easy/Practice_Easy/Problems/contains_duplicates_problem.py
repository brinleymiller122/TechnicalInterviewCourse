# Given an array of integers, find if the array contains any duplicates
# Your function should return false if every element is distinct.
# This problem came from leetcode.com

input_array = [1, 2, 3, 3, 4]
# Output = True

#brute force

def duplicates(n):
    counter=0
    for icount in range(len(n)-1, 0, -1):
        result=""
        if n[icount] == n[counter]:
            result=True
            break
        else: 
            counter += 1
    return result

print(duplicates(input_array))

#better 

def dup(n):
    if len(n) == len(set(n)):
        return False
    else: 
        return True

print(dup(input_array))




