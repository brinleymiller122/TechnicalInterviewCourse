# Write a function that sums all natural numbers that lead up to a given value using recursion
#I dont understand this 
def sum(num):
    if num ==1 or num ==0:
        return num

    return(sum(num-1) + num)

print(sum(5))