# Bubble Sort #
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort algorithm to sort the array.
If you're unfamiliar with Bubble Sort,watch this video which will give the conceptual overview of the Bubble sort [Link to the Video](https://www.linkedin.com/posts/mayank-dubey11_datastructures-complexity-sorting-activity-6758786813793443840-U5KQ) 
### Sample Input ###
array = [8, 5, 2, 9, 5, 6, 3]
### Sample Output ###
[2, 3, 5, 5, 6, 8, 9]

### Idea: ###
Do len(array):
	Compare element(j-1) with next element (j) 
	if array[j-1] is greater than array[j]:
		swap array[j-1] with array[j]  

# Example #
![](images/bubblesort1.png)
![](images/bubblesort2.png)
