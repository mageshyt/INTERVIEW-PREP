
# Time : O(n!)
def permutationRecursive(nums):
    return helper(0,nums)

def helper(start,nums):
    if start == len(nums):
        return [nums[:]]
    res = []
    print("START>>",start)
    print("NUMS>>",nums)
    for i in range(start,len(nums)):
        nums[start],nums[i] = nums[i],nums[start]
        res += helper(start+1,nums)
        nums[start],nums[i] = nums[i],nums[start]
    return res


print(permutationRecursive([1,2,3]))
