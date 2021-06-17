'''
Merge Sort

Like QuickSort, Merge Sort is a Divide and Conquer algorithm. 
It divides the input array into two halves, calls itself for the two halves, 
and then merges the two sorted halves. The merge() function is used for merging 
two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] 
and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. 
See the following C implementation for details.

MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)


'''
# program to for implementation of mergesort
# def mergesort(arr):
#     if len(arr) > 1:
#         # finding the mid of the array
#         mid = len(arr)//2

#         # dividing the array elements 
#         l = arr[:mid]

#         # into 2 halves
#         r = arr[mid:]

#         # sorting the first half
#         mergesort(l)

#         # sorting second half
#         mergesort(r)

#         i = j = k = 0

#         # copy dat to temp arrays l[] and r[]
#         while i < len(l) and j < len(r):
#             if l[i] < r[j]:
#                 arr[k] = l[i]
#                 i += 1
#             else:
#                 arr[k] = r[j]
#                 j += 1
#             k += 1

#         while i < len(l):
#             arr[k] = l[i]
#             i += 1
#             k += 1

#         while j < len(r):
#             arr[k] = r[j]
#             j += 1
#             k += 1

# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print()

# # Driver Code
# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]
#     print("Given array is", end="\n")
#     printList(arr)
#     mergesort(arr)
#     print("Sorted array is: ", end="\n")
#     printList(arr)

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        mergesort(l)
        mergesort(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=' ')
    