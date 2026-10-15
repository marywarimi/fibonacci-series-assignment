# fibonacci-series-assignment
Group assignment on fibonacci algorithms,data structures and customer loyalty rewards 

## Group Members:
Mary warimi     :CT204/124268/25
Pauline Njoroge :CT204/124267/25
Antony Gachoya  :CT204/124274/25
Vincent Hiuhu   :CT204/124333/25

## 1. Project Overview

This project explores different algorithms for generating the Fibonacci sequence and applies them to a customer loyalty reward system.

A software company wants to reward customers according to the number of years they have remained loyal. The reward points follow the Fibonacci sequence, where each number is the sum of the two preceding numbers.

The project implements and compares three approaches:

1. Recursive approach
2. Iterative approach using an array (Python list)
3. Dynamic programming using memoization

The project also models the loyalty reward system and measures the execution time of each approach for `n = 30`.

## 2. Problem Statement

The company requires a reward system that calculates customer loyalty points accurately and efficiently. The system should be suitable for future expansion to support thousands of customers.

The challenge is to identify an appropriate algorithm by comparing correctness, time complexity, space complexity, and execution time.

## 3. Project Objectives

- Implement the Fibonacci sequence using recursion.
- Generate the Fibonacci sequence iteratively and store the results in a Python list.
- Optimize Fibonacci computation using dynamic programming and memoization.
- Develop a customer loyalty reward system that accepts the number of loyal years and displays the corresponding reward points.
- Compare the execution times of the three approaches for `n = 30`.
- Recommend the most suitable approach for the company's reward system.

## 4. Understanding the Fibonacci Sequence

The Fibonacci sequence is a series of numbers in which each number after the first two is obtained by adding the previous two numbers.

The sequence used in this project is:

`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...`

Mathematically:

- F(0) = 0
- F(1) = 1
- F(n) = F(n - 1) + F(n - 2), for n ≥ 2

For example:

F(5) = F(4) + F(3) = 3 + 2 = 5.

The Fibonacci sequence provides a useful case study for understanding recursion, arrays, dynamic programming, and algorithm efficiency.

## 5. Implementation and Analysis

### Task 1: Recursive Approach

**Implementation**

```python
def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print("Fibonacci number at index 6:", fibonacci_recursive(6))
```

**How it works**

The recursive function calls itself to calculate the two preceding Fibonacci numbers. The process continues until it reaches a base case, where `n` is either 0 or 1.

The base cases prevent the function from calling itself indefinitely.

**Expected output**

```text
Fibonacci number at index 6: 8
```

**Time complexity:** O(2ⁿ), an upper bound for the running time of the naive recursive implementation.

**Space complexity:** O(n), because recursive calls are stored on the call stack.

**Advantages**

- Simple and closely follows the mathematical definition.
- Easy to understand and implement.

**Limitations**

- Recalculates the same Fibonacci numbers repeatedly.
- Execution time grows rapidly as n increases.
- Not suitable for large inputs or a high-volume reward system without optimization.

The recursive approach demonstrates the importance of analyzing algorithm efficiency before choosing an implementation for a real-world application.

### Task 2: Iterative Approach Using an Array

**Implementation**

```python
def fibonacci_iterative(n):
    if n == 0:
        return [0]

    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib

print("Fibonacci series up to index 6:", fibonacci_iterative(6))
```

**How it works**

The function starts with the first two Fibonacci numbers stored in a Python list. A loop calculates each subsequent number using the previous two values and appends the result to the list.

The list acts as an array-like data structure that stores the generated sequence.

**Expected output**

```text
Fibonacci series up to index 6: [0, 1, 1, 2, 3, 5, 8]
```

**Time complexity:** O(n), because each Fibonacci number is generated once up to index n.

**Space complexity:** O(n), because the list stores the sequence from index 0 through index n.

**Advantages**

- Avoids the repeated calculations found in naive recursion.
- Efficiently generates the entire sequence.
- Stores intermediate results for later use.
- Easy to understand and maintain.

**Limitations**

- Requires additional memory to store the entire sequence.
- Uses more space than an iterative implementation that stores only the last two numbers when only the nth Fibonacci number is required.

**Comparison with recursion**

The iterative approach has linear time complexity, whereas naive recursion has exponential time complexity. Therefore, iteration becomes substantially more efficient as the input grows.

### Task 3: Dynamic Programming Using Memoization

**Implementation**

```python
def fibonacci_memoized(n, memo=None):
    if memo is None:
        memo = {0: 0, 1: 1}

    if n not in memo:
        memo[n] = (
            fibonacci_memoized(n - 1, memo)
            + fibonacci_memoized(n - 2, memo)
        )

    return memo[n]

print("Fibonacci number using memoization:", fibonacci_memoized(6))
```

**How it works**

Memoization is a dynamic programming technique that stores the results of previously solved subproblems.

The dictionary `memo` initially contains the two base cases. Whenever the function calculates a new Fibonacci number, it stores the result in the dictionary. If the value is requested again, the function retrieves the stored result instead of calculating it again.

**Expected output**

```text
Fibonacci number using memoization: 8
```

**Time complexity:** O(n), because each Fibonacci value is calculated at most once during a fresh computation.

**Space complexity:** O(n), because the dictionary stores intermediate results and recursive calls require stack space.

**Advantages**

- Eliminates repeated calculations.
- Improves performance compared with naive recursion.
- Demonstrates how previously computed results can be reused.

**Limitations**

- Requires memory for the dictionary and recursive call stack.
- Very large inputs can encounter Python's recursion-depth limit.

**Space-time trade-off**

Memoization uses additional memory to store computed values, but this reduces the time required to calculate the Fibonacci number. This is an example of trading extra space for improved execution time.

Unlike the iterative list approach, this implementation returns only the requested Fibonacci number rather than the entire sequence.

### Task 4: Customer Loyalty Reward System

**Implementation**

```python
def loyalty_rewards(years):
    rewards = []

    for i in range(years):
        if i == 0:
            rewards.append(0)
        elif i == 1:
            rewards.append(1)
        else:
            rewards.append(rewards[i - 1] + rewards[i - 2])

    return rewards


years = int(input("\nEnter the number of loyal years: "))

if years < 1:
    print("Please enter at least 1 loyal year.")
else:
    rewards = loyalty_rewards(years)

    print("\nCustomer Loyalty Reward Points")
    print("Rewards array:", rewards)

    for year, points in enumerate(rewards, start=1):
        print(f"Year {year}: {points} points")
```

**How it works**

The system asks the customer to enter the number of years they have remained loyal.

It then generates the Fibonacci-based reward points and stores them in a list called `rewards`. Each list position corresponds to a loyalty year, and the program displays the points for each year.

The program rejects inputs below one year.

**Example input**

```text
Enter the number of loyal years: 7
```

**Expected output**

```text
Customer Loyalty Reward Points
Rewards array: [0, 1, 1, 2, 3, 5, 8]
Year 1: 0 points
Year 2: 1 points
Year 3: 1 points
Year 4: 2 points
Year 5: 3 points
Year 6: 5 points
Year 7: 8 points
```

**Data structure used:** Python list.

**Time complexity:** O(years), because each year's reward is calculated once.

**Space complexity:** O(years), because the list stores the reward points for every year.

**Application significance**

This task demonstrates how a mathematical sequence can be translated into a practical business rule. The resulting list allows the system to retain and display each year's reward points.

In a real business, the company would also need to define whether the first loyalty year should earn zero points or a positive starting reward, as well as how points are redeemed and stored for individual customers.

### Task 5: Performance Analysis

**Implementation**

The program uses Python's `time.perf_counter()` to measure the elapsed execution time of each algorithm.

The input size is set to `n = 30`.

```python
import time

n = 30

# Measure recursive approach
start = time.perf_counter()
recursive_result = fibonacci_recursive(n)
recursive_time = time.perf_counter() - start

# Measure iterative approach
start = time.perf_counter()
iterative_result = fibonacci_iterative(n)[-1]
iterative_time = time.perf_counter() - start

# Measure memoization approach
start = time.perf_counter()
memoized_result = fibonacci_memoized(n)
memoized_time = time.perf_counter() - start

# Display results
print("\n--- PERFORMANCE ANALYSIS (n = 30) ---")

print("Recursive result:", recursive_result)
print("Iterative result:", iterative_result)
print("Memoized result:", memoized_result)

print(f"Recursive time: {recursive_time:.8f} seconds")
print(f"Iterative time: {iterative_time:.8f} seconds")
print(f"Memoization time: {memoized_time:.8f} seconds")
```

**Purpose of the experiment**

The experiment measures the time taken by each algorithm to calculate the Fibonacci number at index 30. The iterative implementation generates the sequence up to that index, while the recursive and memoized implementations return the number at that index.

**Expected mathematical result**

All three approaches should produce the same Fibonacci number:

`F(30) = 832040`

**Recording and interpreting the results**

The execution times depend on the computer, Python environment, and system workload. The actual measured values should be copied from the program's output rather than assumed in advance.

| Algorithm | Result at index 30 | Measured execution time |
|---|---:|---|
| Recursive | 832040 | 0.41938530 seconds |
| Iterative | 832040 | 0.00001540 seconds |
| Memoization | 832040 | 0.00002270 seconds |

**Discussion**

- The recursive implementation is expected to be the slowest because it repeatedly solves the same subproblems.
- The iterative implementation is expected to be very fast because it calculates each term once using a loop.
- Memoization is also expected to be much faster than naive recursion because it reuses stored results.

Small differences between iterative and memoized execution times may vary between runs. For a more reliable comparison, the experiment can be repeated several times and the average execution time calculated.

## 6. Complexity Comparison

| Approach | Time complexity | Auxiliary space complexity | Main characteristic |
|---|---|---|---|
| Recursion | O(2ⁿ) | O(n) | Simple but repeats calculations |
| Iteration with list | O(n) | O(n) | Generates and stores the full sequence |
| Memoization | O(n) | O(n) | Stores computed values for reuse |
| Loyalty reward generation | O(years) | O(years) | Stores points for every loyalty year |

The complexities describe how the algorithms scale as the input grows. They are theoretical estimates and are not substitutes for measured execution times.

The iterative and memoized approaches both have linear time complexity, but they differ in how results are computed and stored. The iterative approach is particularly suitable when the complete sequence is required, while memoization is useful when a recursive formulation is preferred.

## 7. Recommendation for the Company

The **iterative approach** is recommended for the company's customer loyalty reward system.

The reasons are:

1. **Efficiency:** It generates the Fibonacci sequence in O(n) time, avoiding the exponential running time of naive recursion.
2. **Predictable resource usage:** Its time and memory requirements grow linearly with the number of years when the complete sequence is stored.
3. **Simplicity:** The loop-based implementation is straightforward to understand, test, and maintain.
4. **Scalability:** The approach can be extended to calculate rewards for many customers without the repeated computation associated with naive recursion.

If the company only needs to calculate the reward for a specific year, an optimized iterative algorithm that stores only the previous two Fibonacci values would reduce auxiliary space to O(1).

For a production system supporting thousands of customers, the company should also use appropriate customer records, database storage, input validation, and testing. The Fibonacci algorithm alone does not provide the full architecture needed for a scalable business application.

Memoization remains a useful alternative when repeated requests for the same Fibonacci values occur and the stored results can be reused.

## 8. How to Run the Program

**Prerequisites**

- Python 3 installed on the computer.
- A code editor such as Visual Studio Code.

**Steps**

1. Clone or download the project repository.
2. Open the project folder in Visual Studio Code.
3. Open the Python file containing the five tasks.
4. Run the file using Python.
5. Enter a positive number of loyalty years when prompted.
6. Observe the reward points and performance measurements in the terminal.

The performance analysis uses `n = 30` independently of the number of years entered into the loyalty reward system.

## 9. Testing and Validation

The following checks can be used to verify the implementation:

- Confirm that F(0) = 0 and F(1) = 1.
- Confirm that all three algorithms return 8 for index 6.
- Confirm that all three algorithms return 832040 for index 30.
- Verify that the iterative approach generates `[0, 1, 1, 2, 3, 5, 8]` up to index 6.
- Test the loyalty system with 1, 2, and 7 years.
- Confirm that entering zero or a negative number produces the validation message.
- Check that all three performance results are mathematically equal before comparing their execution times.

## 10. Conclusion

This project demonstrates three approaches to solving the Fibonacci problem and applies the sequence to a customer loyalty reward system.

The recursive approach is useful for understanding the mathematical definition but becomes inefficient because of repeated calculations. The iterative approach generates the sequence efficiently using a list, while memoization improves recursive computation by storing previously calculated results.

Based on time complexity, implementation simplicity, and suitability for generating a complete sequence, the iterative approach is the most appropriate starting point for the company's reward system. An optimized implementation and suitable customer-data architecture would further improve its suitability for large-scale deployment.

The project illustrates the importance of selecting appropriate algorithms and data structures when designing efficient software systems.