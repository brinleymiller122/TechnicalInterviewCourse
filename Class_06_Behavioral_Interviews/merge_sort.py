def merge_sort(list):
    if len(list) > 1:
        middle=len(list)//2
        left=list[:middle]
        right=list[middle:]

        merge_sort(left)
        merge_sort(right)

        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if left[i] <= left[j]:
                list[k]=left[i]
                i +=1
            else:
                list[k]=right[j]
            k +=1

        while i < len(left):
            list[k]= left[i]
            i+=1
            k+=1

        while j < len(right):
            list[k]=right[j]
            j += 1
            k += 1


#comment
#     merge_sort2 (list, 0, len(list)-1)

# def merge_sort2(list, first, last):
#     if first < last: 
        
#         merge_sort2(list, first, middle)
#         merge_sort2(list, middle+1, last)
#         merge(list, first, middle, last)

# def merge(list, first, middle, last):
#     L=list[first:middle]
#     R=list[middle:last+1]
#     L.append(99999999999)
#     R.append(99999999999)
#     i=0
#     j=0
#     for k in range(first,last+1):
#         if L[i] <= R[j]:
#             list[k]=L[i]
#             i += 1
#         else:
#             list[k]=R[j]
#             j +=1

list[44,77,2,8,9,100,33,22,99]
print(merge_sort(list))
