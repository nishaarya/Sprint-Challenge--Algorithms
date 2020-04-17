#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) It looks like that it is running linearly, as it is based on the n variable. It is iterating exactly n times. So therefore, the runtime is O(n)


b) I think that it is O(n log n). Because it is running as O(n) however, it then has a higher time complexity. 


c) I believe this is O(n) that runs on a basic recursive function, as the algorithm is telling you exactly what to return.

## Exercise II

n == num of stories in the building.
n/2 = this is the start of the middle of the building
num_eggs = unlimited
f == floor number (in order)

Binary search of approaching the middle index can give a better run time then just throwing it from the first floor and see if it breaks and eventually working your way up.

So we start from the middle and run a loop to see if the egg breaks
If it doesnt break, return the floor (f)
If it breaks, we can ignore the top half
We then can start working on the lower half strating from the middle
We then repeat these steps until the egg doesnt break

O(log n) runtime. 
