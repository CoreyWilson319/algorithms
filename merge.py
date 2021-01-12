list = [9, 2, 4, 3, 1, 6, 5, 8, 7]

# Merge sort is recursive
# Need to divide and conquer
def merge_sort(list, results=[]):
    center = int(len(list) / 2)
    first = list[:center]
    last = list[center:]
    if len(list) > 1:
        merge_sort(first)
        merge_sort(last)
    else:
        if first[0] > last[0]:
            results.append(first[0])
        else:
            results.append(last[0])
        
    return results



print(merge_sort(list))