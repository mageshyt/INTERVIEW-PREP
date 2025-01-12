def find_max_value(size, queries):
    diff = [0] * (size + 1)
    
    for start, end, value in queries:
        diff[start - 1] += value
        if end < size:
            diff[end] -= value
    max_value = 0
    current_sum = 0
    for i in range(size):
        current_sum += diff[i]
        max_value = max(max_value, current_sum)
    
    return max_value

size=int(input())
queryCount=int(input())

queries = []

for _ in range(queryCount):
    queries.append(list(map(int, input().split())))

print(find_max_value(size, queries))
# Exercise-2 Input
size_2 = 10
queries_2 = [
    [3, 10, 3],
    [4, 5, 9],
    [2, 9, 11],
]
print(find_max_value(size_2, queries_2))  # Output: 23
