'''
Efficiency of an algorithm depends on two parameters:

1. Time Complexity

2. Space Complexity

Time Complexity: Time Complexity is defined as the number of times a particular instruction set is executed 
rather than the total time is taken. It is because the total time taken also depends on some external factors 
like the compiler used, processor’s speed, etc.

Space Complexity: Space Complexity is the total memory space required by the program for its execution.


Both are calculated as the function of input size(n).

One important thing here is that in spite of these parameters the efficiency of an algorithm also depends upon the nature and size of the input. 

Following is a quick revision sheet that you may refer at last minute 

Algorithm       	        Time Complexity	 
 	                Best	    Average	    Worst	 
Selection Sort	    Ω(n^2)	    θ(n^2)	    O(n^2)	 
Bubble Sort	         Ω(n)	    θ(n^2)	    O(n^2)	 
Insertion Sort	     Ω(n)	    θ(n^2)	    O(n^2)	 
Heap Sort	        Ω(n log(n))	θ(n log(n))	O(n log(n))	 
Quick Sort	        Ω(n log(n))	θ(n log(n))	O(n^2)	 
Merge Sort	        Ω(n log(n))	θ(n log(n))	O(n log(n))	 
Bucket Sort	        Ω(n+k)	    θ(n+k)	    O(n^2)	 
Radix Sort      	Ω(nk)	    θ(nk)	    O(nk)	 


'''