## Brute Force : O(n^2)

def BruteForce(nums):
    maxSum=nums[0]
    n=len(nums)

    for i in range(n):
        currSum=0
        for j in range(i,n):
            currSum+=nums[j]
            maxSum=max(currSum,maxSum)
    return maxSum


## Kadane's Algorithm

def kadanes(nums):
    maxSum=nums[0]
    currSum=0

    for n in nums :
        currSum=max(currSum,0)

        currSum+=n
        maxSum=max(currSum,maxSum)

    return maxSum


nums=[4,-1,2,-7,3,4]
print("Brute Force",BruteForce(nums))
print("Kadanes",kadanes(nums))
