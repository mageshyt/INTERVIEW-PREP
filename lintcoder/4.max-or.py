"""
Maximum OR
Given a 0-indexed integer array nums of length n and an integer k, you are allowed to perform an operation on any element by multiplying it by 2. The goal is to find the maximum possible value of the bitwise OR operation performed on all elements in the nums array after applying the operation at most k times.

Note that the bitwise OR operation (|) between two integers a and b results in a new integer where each bit is set if it is set in either a or b.

Important Note:
Ensure that you save your solution before progressing to the next question and before submitting your answer.

Example

INPUT
[12,9]
1
OUTPUT
30

Exercise-1

Input : 
12 9
2

Output :
57
Exercise-2

Input:
3 2 4
2

Output:
19
"""

def max_or(nums, k):
    maxOr = 0

    for num in nums:
        maxOr |= num


    cache = {}

    def dfs( k,i,currXor):
        if k == 0:
            return currXor

        if (i, k) in cache:
            return cache[(i, k)]

        # choice 1: double the number
        double = dfs(k - 1, i + 1, currXor | (nums[i] << k - 1))

        # choice 2: do not double the number

        noDouble = dfs(k - 1, i + 1, currXor)

        cache[(i, k)] = max(double, noDouble)

        return cache[(i, k)]


    return dfs(k, 0, maxOr)

# Example usage
nums = [12,9]
k = 2
print(max_or(nums, k))  # Output: 30


def maximum_or(nums, k):
    n = len(nums)
    
    # Step 1: Precompute prefix and suffix OR arrays
    prefix = [0] * n
    suffix = [0] * n
    
    # Compute prefix OR
    for i in range(1, n):
        prefix[i] = prefix[i - 1] | nums[i - 1]
    
    # Compute suffix OR
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] | nums[i + 1]
    
    # Step 2: Compute the maximum OR after applying the operation on each element
    max_or = 0
    for i in range(n):
        # Remove nums[i] and multiply it by 2^k
        modified_num = nums[i] << k
        
        # Combine prefix OR, modified number, and suffix OR
        current_or = prefix[i] | modified_num | suffix[i]
        
        # Update the maximum OR found
        max_or = max(max_or, current_or)
    
    return max_or

# Test cases
print(maximum_or([12, 9], 1))  # Expected output: 30
print(maximum_or([12, 9], 2))  # Expected output: 57
print(maximum_or([3, 2, 4], 2))  # Expected output: 19
