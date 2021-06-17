'''
Selection Sort

Selection Sort

The selection sort algorithm sorts an array by repeatedly finding the minimum element 
(considering ascending order) from unsorted part and putting it at the beginning. 
The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element 
(considering ascending order) from the unsorted subarray 
is picked and moved to the sorted subarray.

Following example explains the above steps:

arr[] = 64 25 12 22 11

# find the minimum element in arr[0....4]
# and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4]
// and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4]
// and place it at beginning of arr[3...4]
11 12 22 25 64 


'''
# import sys

# a = [64, 25, 12, 22, 11]

# for i in range(len(a)):

#     # find the minimum element in remaining unsorted array
#     min_idx = i
#     for j in range(i+1, len(a)):
#         if a[min_idx] > a[j]:
#             min_idx = j

#     # swap the found minimum element with
#     # the first element
#     a[i], a[min_idx] = a[min_idx], a[i]

# # driver code to test above
# print("sorted array")
# for i in range(len(a)):
#     print(a[i],end=' ')


# traverse trough all array elements

a = [111,10,29,20,43,9,5]

for i in range(len(a)):
    min_idx = i
    for j in range(i+1,len(a)):
        if a[min_idx] > a[j]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]

print("sorted array")
for i in range(len(a)):
    print(a[i],end=' ')
 
'''
Time Complexity: O(n2) as there are two nested loops.

Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.



'''
 