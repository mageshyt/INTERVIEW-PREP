from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        def backTrack(nums,k):
            if not nums:
                return ""
            print("NUMS>>",nums)
            n = len(nums)

            fact = factorial(n-1)
            index = (k-1)//fact # 0 based index 
            print("FACT,INDEX>>",fact,index)

            # remove the element at INDEX from nums
            new_nums = nums[:index]+nums[index+1:] # O(n)
            return nums[index] + backTrack(new_nums,k-index*fact)


        return backTrack("".join([str(i) for i in range(1,n+1)]),k)


    # without recursion Time : O(n*n)
    def getPermutation2(self, n: int, k: int) -> str:
        fact = [1] 
        # compute factorial for n-1 numbers
        for i in range(1,n):
            fact.append(fact[-1]*i)
        
        nums = [str(i) for i in range(1,n+1)] # O(n)
        k -= 1 # because 0 based index 
        res = "" 
        for i in range(n):

            index = k//fact[n-1-i]
            res += nums[index]
            nums.pop(index) # remove the element at INDEX
            k %= fact[n-1-i] # update k  

        return res

# Time : O(n)
# print(Solution().getPermutation(4,17))
print(Solution().getPermutation2(4,17))
