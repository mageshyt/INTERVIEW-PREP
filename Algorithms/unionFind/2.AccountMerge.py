
from typing import List

class UnionFind:
    def __init__(self) -> None:
        self.parent = {}

    def find(self, x: int) -> int:
        self.parent.setdefault(x, x)

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> None:

        xParent = self.find(x)
        yParent = self.find(y)

        if xParent != yParent:
            self.parent[xParent] = yParent

    def is_connected(self, x: int, y: int) -> bool:

        return self.find(x) == self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToAcc = {} # emai -> accounts

        uf = UnionFind()

        for idx,account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    uf.union(emailToAcc[email],idx)
                emailToAcc[email] = idx
        accToEmails = {} # account -> emails

        for email,acc in emailToAcc.items():
            root = uf.find(acc)
            accToEmails.setdefault(root,[])
            accToEmails[root].append(email)

        res = []
        for root,emails in accToEmails.items():
            res.append([accounts[root][0]] + sorted(emails))

        return res


# Time Complexity: O(N)
# Space Complexity: O(N)

print(Solution().accountsMerge(
    [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
))



        
