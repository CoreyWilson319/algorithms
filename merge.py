list = [9, 2, 4, 3, 1, 6, 5, 8, 7]

# Merge sort is recursive
# Need to divide and conquer
# def merge_sort(list, results=[]):
#     center = int(len(list) / 2)
#     first = list[:center]
#     last = list[center:]
#     if len(list) > 1:
#         merge_sort(first)
#         merge_sort(last)
#     else:
#         if first[0] > last[0]:
#             results.append(first[0])
#         else:
#             results.append(last[0])

#     return results


# print(merge_sort(list))


# Started with merge
# Kept items as a single array

def split(arr):
    print('splitting: ', arr)
    midpoint = len(arr) // 2
    arr1 = arr[:midpoint]
    arr2 = arr[midpoint:]
    
    if len(arr1) <= 1 and len(arr2) <= 1:
        return merge(arr1, arr2)


    split_arr1 = split(arr1)
    split_arr2 = split(arr2)

    return merge(split_arr1, split_arr2)








def merge(arr1, arr2):
    output = []
    start_length_arr1 = len(arr1)
    start_length_arr2 = len(arr2)
    target_output_length = start_length_arr1 + start_length_arr2

    # OR:
    # while len(arr1) > 0 or len(arr2) > 0:
    while len(output) < target_output_length:
        print('__________')
        print('arr1: ', arr1)
        print('arr2: ', arr2)
        print('output: ', output)

        if len(arr1) == 0:
            output += arr2
            arr2 = []

        elif len(arr2) == 0:
            output += arr1
            arr1 = []

        elif arr1[0] < arr2[0]:
            output.append(arr1[0])
            arr1 = arr1[1:]

        else:
            output.append(arr2[0])
            arr2 = arr2[1:]

    return output

print(split([1, 9, 6, 4, 3, 5, 7, 2, 8]))
# print(split([1, 2, 3, 4, 5, 6, 7]))
# print(merge([2], [4]))
# print(merge([4], [2]))
# print(merge([1,3, 5, 9, 10], [2,4, 6, 8]))
