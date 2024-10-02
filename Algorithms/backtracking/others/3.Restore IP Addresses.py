from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # we can't have more than 12 digits to form an IP address
        res=[]
        if len(s)>12:
            return res
        def backTrack(idx,path):
            # base cases
            if idx == len(s) and len(path)==4:
                res.append('.'.join(path))
                return

            if len(path) == 4:
                return

            for i in range(1,4):
                if idx+i > len(s):
                    break
                num = s[idx:idx+i]
                # check it dont have leading zeros and it is less than 256
                if (num[0]=='0' and len(num)>1) or int(num)>255:
                    continue

                backTrack(idx+i,path+[num])

        backTrack(0,[])

        return res

# Time complexity: O(3^4)
# Space complexity: O(3^4)

print(Solution().restoreIpAddresses("25525511135"))
