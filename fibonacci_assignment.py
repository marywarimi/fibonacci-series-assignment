 
# TASK 1: RECURSIVE APPROACH

def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Test the function
print("Fibonacci number at index 6:", fibonacci_recursive(6))



# TASK 2: ITERATIVE APPROACH USING AN ARRAY

def fibonacci_iterative(n):
    if n == 0:
        return [0]

    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib


# Test the function
print("Fibonacci series up to index 6:", fibonacci_iterative(6))



# TASK 3: DYNAMIC PROGRAMMING USING MEMOIZATION

def fibonacci_memoized(n, memo=None):
    if memo is None:
        memo = {0: 0, 1: 1}

    if n not in memo:
        memo[n] = (
            fibonacci_memoized(n - 1, memo)
            + fibonacci_memoized(n - 2, memo)
        )

    return memo[n]


# Test the function
print("Fibonacci number using memoization:", fibonacci_memoized(6))



# TASK 4: CUSTOMER LOYALTY REWARD SYSTEM

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


# Get input from the customer
years = int(input("\nEnter the number of loyal years: "))

if years < 1:
    print("Please enter at least 1 loyal year.")
else:
    rewards = loyalty_rewards(years)

    print("\nCustomer Loyalty Reward Points")
    print("Rewards array:", rewards)

    for year, points in enumerate(rewards, start=1):
        print(f"Year {year}: {points} points")



# TASK 5: PERFORMANCE ANALYSIS

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
