from typing import List
class Solution:
    def letterCombinations(self,digits:str)-> List[str]:
        if len(digits)==0:
            return []

        phone={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        res=[]

        self.helper(digits,0,phone,"",res) # digits, index, phone, path, result

        return res
    def helper(self,digits,index,phone,path,res):
        if index==len(digits):
            res.append(path)
            return

        for letter in phone[digits[index]]:
            self.helper(digits,index+1,phone,path+letter,res)

# Time complexity: O(4^n)
# Space complexity: O(n)
print("TEST CASES")
print(Solution().letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
