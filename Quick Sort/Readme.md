# Quick Sort #
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Quick Sort algorithm to sort the array.
If you're unfamiliar with Quick Sort,watch this video which will give the conceptual overview of the Quick sort [Link to the Video](https://www.linkedin.com/posts/mayank-dubey11_datastructures-divideandconquer-quicksort-activity-6760558483151589376-dEZZ) 
### Sample Input ###
array = [8, 5, 2, 9, 5, 6, 3]
### Sample Output ###
[2, 3, 5, 5, 6, 8, 9]

### Idea: ###
<li>The idea is to select random element (pivot element) and after every iteration the pivot will be placed at it's correct index.</li>
<li>Now array is divided in two parts left of pivot and right of pivot (divide and conquer).</li>
<li>Apply same procedure on those two parts.</li>

### Time complexity ###
Best case - O(N log N) <br>
Average case - O(N log N) <br>
Worst case - O(N^2) <br>

### Space complexity ###
O(1)



# Example #
![](images/quicksort1.jpg)
![](images/quicksort2.jpg)
![](images/quicksort3.jpg)
![](images/quicksort4.jpg)
![](images/quicksort5.jpg)
