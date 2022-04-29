# CMPS 2200 Assignment 5

## Answers

**Name:** Mikey Sison

Place all written answers from `assignment-05.md` here for easier grading.

- **1a.**

The greedy algorithm would select the largest coin size that would fit in given dollar amount. The algorithm would then
select the next largest, then the next largest, so on and so forth until reaching the dollar amount.

- **1b.**
  Work = O(log n)
  Span = O(log n)


- **2a.**
  Denominations: $5, $4, $1.
- To make $8, greedy method would take 5 + 1 + 1 + 1 = 8, using 4 bills, when in reality, you could just use 2 $4 bills.
- A Greedy algorithm would fail to account for scenarios where the second or third largest * x would yield the lowest
  number of coins.


- **2b.**

---

if Dk can be used
((n - Dk, k) + 1)

if Dk cant be used
(n, k - 1)

min(f(n - Dk, k) + 1, f(n, k[1:])),
where n = amount of money and k is the number of given denominations.

- Given the set of denominations, S = {5, 4, 1}, a memoized table would look like this:
  Memoized table
-

|$    |  5    | 4    |  1 | min value to lookup|
|-------|-------|------|------|----|
|0      |   0  | 0     | 0     |  0  |
|1      |   0  | 0     | 1     |  1  |
|2      |   0  | 0     | 2     |  2  |
|3      |   0  | 0     | 3     |  3  |
|4      |   0  | 1     | 4     |  1  |
|5      |   1  | 2     | 5     |  1  |
|6      |   2  | 3     | 6     |  2  |
|7      |   3  | 4     | 7     |  3  |
|8      |   4  | 2     | 8     |  2  |
|9      |   2  | 3     | 9     |  2  |
|10     |   2  | 4     | 10    |  2  |
|11     |   3  | 5     | 11    |  3  |

So, with a memoized version of the DAG, 
similar to the knapsack problem, would have a work of O(n*k) and span of O(n).
