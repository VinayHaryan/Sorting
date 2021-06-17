'''
Insertion Sort

Insertion sort is a simple sorting algorithm that works similar 
to the way you sort playing cards in your hands. 
The array is virtually split into a sorted and an unsorted part. 
Values from the unsorted part are picked and placed at the correct 
position in the sorted part.

Algorithm 
To sort an array of size n in ascending order: 
1: Iterate from arr[1] to arr[n] over the array. 
2: Compare the current element (key) to its predecessor. 
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

Another Example: 
12, 11, 13, 5, 6
Let us loop for i = 1 (second element of the array) to 4 (last element of the array)
i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12 
11, 12, 13, 5, 6
i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13 
11, 12, 13, 5, 6
i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position. 
5, 11, 12, 13, 6
i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position. 
5, 6, 11, 12, 13 

'''

# program for implementation of inserstion sort
# def inserstionsort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]

#         # move elements of arr[0..i-1] that are
#         # greater than key, to one position ahead
#         # of their current position
#         j = i -1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key

# arr = [12, 11, 13, 5, 6]
# inserstionsort(arr)
# for i in range(len(arr)):
#     print ("% d" % arr[i],end=' ')

def inserstionsort(arr):
    for i in range(1,len(arr)):
        key = arr[i]

        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key

# driver mode to test above
arr = [12, 11, 13, 5, 6]
inserstionsort(arr)
for i in range(len(arr)):
    print(arr[i],end=' ')


'''
Time Complexity: O(n*2) 
Auxiliary Space: O(1)

Boundary Cases: Insertion sort takes maximum time to sort if elements 
are sorted in reverse order. And it takes minimum time (Order of n) 
when elements are already sorted.

Algorithmic Paradigm: Incremental Approach


Sorting In Place: Yes
Stable: Yes
Online: Yes
Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.
What is Binary Insertion Sort? 
We can use binary search to reduce the number of comparisons in normal insertion sort. Binary Insertion Sort uses binary search to find the proper location to insert the selected item at each iteration. In normal insertion, sorting takes O(i) (at ith iteration) in worst case. We can reduce it to O(logi) by using binary search. The algorithm, as a whole, still has a running worst case running time of O(n2) because of the series of swaps required for each insertion. Refer this for implementation.
How to implement Insertion Sort for Linked List? 
Below is simple insertion sort algorithm for linked list. 

1) Create an empty sorted (or result) list
2) Traverse the given list, do following for every node.
......a) Insert current node in sorted way in sorted or result list.
3) Change head of given linked list to head of sorted (or result) list. 

'''