input_array=[3,4,5,6,1,2]


def search(list):
    lower=0
    upper=len(list)-1

   
    while lower <= upper:
        mid= (lower+upper)//2
        if (list[mid] > list[upper]):
            lower=mid+1
        else:
            upper=mid

        
    return list[upper-1]

print(search(input_array))

