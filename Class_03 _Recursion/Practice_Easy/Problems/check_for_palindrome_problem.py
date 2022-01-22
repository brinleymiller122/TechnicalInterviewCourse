# Write a function that checks if a string is a palindrome using recursion

def palindrome(string):
    list=[]
    for icount in range(len(string), 0, -1):
        list.append(icount)
        if icount == string[icount]:
            
