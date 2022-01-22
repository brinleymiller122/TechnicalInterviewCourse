# Write a function that reverses a string using recursion

def reverse(string):
    list=[]

    for icount in range(len(string), 0, -1):
        list.append(icount)
      
        
    return list 
print(reverse("Hello"))
    
    