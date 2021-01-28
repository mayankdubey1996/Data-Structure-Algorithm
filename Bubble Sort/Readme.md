# Bubble Sort #
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort algorithm to sort the array.
If you're unfamiliar with Bubble Sort,watch this video which will give the conceptual overview of the Bubble sort [Link to the Video](https://www.linkedin.com/posts/mayank-dubey11_datastructures-complexity-sorting-activity-6758786813793443840-U5KQ) 
### Sample Input ###
array = [8, 5, 2, 9, 5, 6, 3]
### Sample Output ###
[2, 3, 5, 5, 6, 8, 9]

### Idea: ###
Compare element(j-1) with next element (j) <br>
if array[j-1] is greater than array[j]: <br>
swap array[j-1] with array[j] 
### Time complexity ###
Best case - O(N) <br>
Average case - O(N^2) <br>
Worst case - O(N^2) <<br>

### Space complexity ###
O(1)

# Example #
![](images/bubblesort1.png)
![](images/bubblesort2.png)

