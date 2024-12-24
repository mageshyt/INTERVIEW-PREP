

def printSubsequences(nums):
    res = []

    def helper(idx,arr,res):
        if idx >= len(nums):
            print(arr)
            return res.append(arr)

        # take
        helper(idx+1,arr+[nums[idx]],res)

        # not take

        helper(idx+1,arr,res)

    helper(0,[],res)
    print(res)

printSubsequences([3,1,2])
