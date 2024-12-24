
def printSubsequences(nums,sum):
    res = []

    def helper(idx,arr,sum):
        if idx >= len(nums):
            if sum == 0:
                print(arr)
            return

        # take
        helper(idx+1,arr+[nums[idx]],sum-nums[idx])

        # not take

        helper(idx+1,arr,sum)

    helper(0,[],sum)

printSubsequences([1,2,1],2)

# modified question print one subsequence whose sum is k

def printOneSubsequences(nums,sum):
    res = []

    def helper(idx,arr,sum):
        if idx >= len(nums):
            if sum == 0:
                print(arr)
                return True
            return False

        # take
        take=helper(idx+1,arr+[nums[idx]],sum-nums[idx])

        if take:
            return True

        # not take

        return helper(idx+1,arr,sum)

    helper(0,[],sum)

printOneSubsequences([1,2,1],2)


# count number of subsequence whose sum is k

def countSubsequences(nums,sum):
    res = []

    def helper(idx,sum):
        if idx >= len(nums):
            if sum == 0:
                return 1
            return 0

        # take
        take=helper(idx+1,sum-nums[idx])

        # not take

        notake=helper(idx+1,sum)

        return take+notake

    return helper(0,sum)


print(countSubsequences([1,2,1],2)) # 2
