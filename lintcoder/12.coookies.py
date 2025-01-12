import heapq

def min_steps_to_sweetness(target, candies):
    heapq.heapify(candies)
    steps = 0

    while len(candies) > 1:
        least_sweet = heapq.heappop(candies)
        second_least_sweet = heapq.heappop(candies)

        new_sweetness = least_sweet + 2 * second_least_sweet
        heapq.heappush(candies, new_sweetness)

        steps += 1

        if candies[0] >= target:
            return steps
        

    return -1 if candies[0] < target else steps


target=int(input())
candies=list(map(int, input().split()))

print(min_steps_to_sweetness(target, candies))


