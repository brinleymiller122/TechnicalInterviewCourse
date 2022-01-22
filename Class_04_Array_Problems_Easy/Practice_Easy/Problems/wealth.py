input_accounts=[[2,8,7],[7,1,3],[1,9,5]]

def wealth(array):
    richest=0
    
    for item in array:
        total=0
        for icount in range(0,len(item)):
            total +=item[icount]
        if total > richest:
            richest=total

    return richest
        
print(wealth(input_accounts))