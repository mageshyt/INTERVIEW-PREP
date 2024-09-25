from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = [1,2,4,8] # 4 bits
        minutes = [1,2,4,8,16,32] # 6 bits

        res = []

        def backTrack(turnedOn,start,hour,minute):
            if turnedOn==0:
                if hour>11 or minute>59:
                    return
                res.append(f"{hour}:{minute:02d}")
                return

            for i in range(start,len(hours)+len(minutes)):
                if i<len(hours):
                    backTrack(turnedOn-1,i+1,hour+hours[i],minute)
                else:
                    backTrack(turnedOn-1,i+1,hour,minute+minutes[i-len(hours)])

        backTrack(turnedOn,0,0,0)

        return res

# Time complexity: O(2^n)
# Space complexity: O(n)
print("TEST CASES")
print(Solution().readBinaryWatch(1)) # ["1:00","2:00","4:00","8:00","0:01","0:02","0:04","0:08","0:16","0:32"]
