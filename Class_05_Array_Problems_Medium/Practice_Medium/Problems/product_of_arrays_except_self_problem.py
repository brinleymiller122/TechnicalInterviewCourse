# Given an array nums of n integers where n > 1, return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i]
# Note: Please solve it without division
# This problem came from leetcode.com

input_array = [1, 2, 3, 4]
# Output = [24, 12, 8, 6]

def product(list):
    newlist=[]
    for index, product in enumerate(list):
        while (len(list)-1) != index:
            total=1
            total= total * product(index)
        
        newlist.append(total)

    return newlist

print(product(input_array))