# Problem and Instructions

Consider an array of integers, **arr = [arr[0], arr[1], ..., arr[n-1]]**. We define the absolute difference between two elements, **a[i]** and **a[j]** (where **i ≠ j**), to be the absolute value of **a[i] - a[j]**.
Given an array of integers, find and print the minimum absolute difference between any two elements in the array. For example, given the array **arr = [-1, 2, 4]** we can create **3** pairs of numbers: **[-2, 2], [-2, 4]** and **[2, 4]**. The absolute differences for these pairs are **|(-2) -2| = 4, |(-2) - 4| = 6** and **|2 -4| = 2**. The minimum absolute difference is **2**.

**Function Description**</br>
Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.
minimumAbsoluteDifference has the following parameter(s):

- n: an integer that represents the length of arr
- arr: an array of integers

**Input Format**</br>
The first line contains a single integer **n**, the size of **arr**.
The second line contains **n** space-separated integers **arr[i]**.

**Constraints**

- 2 ≤ n ≤ 10<sup>5</sup>
- - -10<sup>9</sup> ≤ arr[i] ≤ 10<sup>9</sup>

**Output Format**</br>
Print the minimum absolute difference between any two elements in the array.

**Sample Input 0**

```
3
3 -7 0
```

**Sample Output 0**

```
3
```

**Explanation 0**</br>
With **n = 3** integers in our array, we have three possible pairs: **(3, -7), (3, 0) and (-7, 0)**. The absolute values of the differences between these pairs are as follows:

- |3 - - 7| -> 10
- |3 - 0| -> 3
- |-7 - 0| -> 7

Notice that if we were to switch the order of the numbers in these pairs, the resulting absolute values would still be the same. The smallest of these possible absolute differences is **3**.

**Sample Input 1**

```
10
-59 -36 -13 1 -53 -92 -2 -96 -54 75
```

**Sample Output 1**

```
1
```

**Explanation 1**</br>
The smallest absolute difference is **| -54 - - 52| = 1**.

**Sample Input 2**

```
5
1 -3 71 68 17
```

**Sample Output 2**

```
3
```

**Explanation 2**</br>
The minimum absolute difference is **|71 - 68| = 3**.
