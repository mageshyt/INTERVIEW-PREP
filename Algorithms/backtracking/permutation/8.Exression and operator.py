from typing import List
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res=[]

        def backTrack(curr_idx,curr_res,curr_sum,prev):
            if curr_idx==len(num):
                # if the current sum is equal to the target
                if curr_sum==target:
                    res.append(curr_res)
                return

            # start from the current index

            for i in range(curr_idx,len(num)):
                # if the current index is not the start index
                if i!=curr_idx and num[curr_idx]=='0':
                    break

                # get the current number
                curr_num=int(num[curr_idx:i+1])

                # if the current index is the start index
                if curr_idx==0:
                    
                    backTrack(i+1,str(curr_num),curr_num,curr_num)
                else:
                    # add the current number
                    backTrack(i+1,curr_res+'+'+str(curr_num),curr_sum+curr_num,curr_num)

                    # subtract the current number
                    backTrack(i+1,curr_res+'-'+str(curr_num),curr_sum-curr_num,-curr_num)

                    # multiply the current number
                    backTrack(i+1,curr_res+'*'+str(curr_num),curr_sum-prev+prev*curr_num,prev*curr_num)
        

        backTrack(0,'',0,0)

        return res

# Time complexity: O(4^n)

# Example test case
print("TEST CASES")
solution = Solution()
print(solution.addOperators("123", 6))  # Expected output: ["1+2+3", "1*2*3"]
