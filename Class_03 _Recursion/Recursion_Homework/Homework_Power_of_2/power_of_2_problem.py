# Given an integer n, return True if it is a power of 2. 
# An integer n is a power of two, if there exists an integer x such that n == 2^x

# Examples:

# Input: n = 4
# Output: True
# 2^2 = 4

# Input : n = 16
# Output : True
# 2^4 = 16

# Input : n = 13
# Output : False

import math

def power(n):
    result=""
    if (n ==0 or n==2):
        result= False
    elif (math.sqrt(n) == type(int)):
        if (math.sqrt(n*2) == type(float)):
            result= True
    elif (math.sqrt(n) == type(float)):
        if (math.sqrt(n*2) == type(int)):
            result= True
    else:   
        result= False
        
    return result
    
print(power(16))