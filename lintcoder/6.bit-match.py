"""
Bit Matching:
We define f(X,Y) as number of matching bits in binary representation of X and Y. For example, (3, 5) = 1, since binary representation of 3 and 5 are 011 and 101, so matching bit count of f(3, 5) = 8.
You are given an array A of N integers, A1, A2 ,…, AN. Find sum of matching bit f(Ai, Aj) for all ordered pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer.

Note: Binary conversion is valid in the range from 000 to 111.

Example with explanation:

if the input is
1 3

then output is
10

because the binary representation of 3 is 011, and the binary equivalent of 1 is 001.
(1 1),(1 3),(3 1),(3 3) gives 3+2+2+3 = 10

if the input is
2 4 6

the output is
19

because the combinations of the given input are:

(2,2) gives 010 010, so the matching count is 3.
(2,4) gives 010 100, with a matching count of 1.

Similarly, we need to find all combinations:
(2,6), (4,2), (4,4), (4,6), (6,2), (6,4), (6,6).

So, the total value is
3+1+2+1+3+2+2+2+3=19

Constraints:

Input integer numbers should be equal to or below 7. If the condition is NOT satisfied, print "Invalid Input".

Sample exercise 1:

Input:
2 4 6

Output:
19

Sample exercise 2:

Input:
1 3

Output:
10
"""
def count_matching_bits(X, Y):
    match=0

    for i in range(3):
        if (X & (1 << i)) == (Y & (1 << i)):
            match += 1

    return match

def bit_matching_sum(A):
    n = len(A)
    total = 0

    for i in range(n):
        for j in range(n):
            print("PAIR(I,J):",A[i],A[j])
            total += count_matching_bits(A[i], A[j])

    return total

# Sample exercises
print(bit_matching_sum([2, 4, 6]))  # Output: 19
print(bit_matching_sum([1, 3]))     # Output: 10
