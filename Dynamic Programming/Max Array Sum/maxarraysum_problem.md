# Problem and Instruction

Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.

For example, given an array **arr = [-2, 1, 3, -4, 5]** we have the following possible subsets:

```
Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8
```

Our maximum subset sum is **8**.

**Function Description**</br>
Complete the _maxSubsetSum_ function in the editor below. It should return an integer representing the maximum subset sum for the given array.

maxSubsetSum has the following parameter(s):

- arr: an array of integers

**Input Format**</br>
The first line contains an integer, **n**.</br>
The second line contains **n** space-separated integers **arr[i]**.

**Constraints**

- 1 ≤ n ≤ 10<sup>5</sup>
- -10<sup>4</sup> ≤ arr[i] ≤ 10<sup>4</sup>

**Output Format**</br>
Return thr maximum sum descriped in the statement.

**Sample Input 0**

```
5
3 7 4 6 5
```

**Sample Output 0**

```
13
```

**Explanation 0**</br>
Our possible subsets are **[3, 4, 5], [3, 4], [3, 6], [3, 5], [7, 6], [7, 5]** and **[4, 5]**. The largest subset sum is **13** from subset **[7, 6]**.

**Sample Input 1**

```
5
2 1 5 8 4
```

**Sample Output 1**

```
11
```

**Explanation 1**</br>
Our subsets are **[2, 5, 4], [2, 5], [2, 8], [2, 4], [1, 8], [1, 4]** and **[5, 4]**. The maximum subset sum is **11** from subset the first subset listed.

**Sample Input 2**

```
5
3 5 -7 8 10
```

**Sample Output 2**

```
15
```

**Explanation 2**</br>
Our possible subsets are **[3, -7, 10], [3, 8], [3, 10], [5, 8], [5, 10]** and **[-7, 10]**. The maximum subset sum is **15** from the fifth subset listed.
