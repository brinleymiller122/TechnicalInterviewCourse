array=[1,2,3,5,6]

def missing(array):
    for icount in range(0,len(array)):

        if (array[icount+1]-array[icount]) == 1:
            continue
        else:
            print(array[icount] + 1  )

print(missing(array)) 
        