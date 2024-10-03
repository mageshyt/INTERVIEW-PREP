
from typing import *

def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    # Write your code here.
    def backTrack(idx,tot):
        if tot==k:
            return True
        if idx >= n or tot > k:
            return False

        if backTrack(idx+1,tot+a[idx]):
            return True
        

        if backTrack(idx+1,tot):
            return True

        return False

    return backTrack(0,0)

print(isSubsetPresent(4, 13, [4,3,5,2])) # True
