# 0x02-minimum_operations

##Task

<h2>0. Minimum Operations</h2>
<p>In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
</p>

<h2>Solution</h2>

<p>This implementation starts with an if statement to check if n is less than or equal to 1. If it is, then it returns 0, since it is impossible to achieve n H characters with just one character.</p>

<p>Next, the function loops through all the integers from 2 to n (inclusive). For each integer i, it checks if n is divisible by i. If it is, then it recursively calls minOperations with n divided by i as the argument, and adds i to the result of the recursive call. This represents copying all the characters, pasting i-1 times, and then copying and pasting i-1 more times.</p>

<p>Finally, if none of the integers from 2 to n are factors of n, then the function returns n, since the only way to get n H characters is to copy and paste H n-1 times.</p>

<h3>This algorithm has a time complexity of O(sqrt(n)), since it only needs to check integers up to the square root of n.</h3>
