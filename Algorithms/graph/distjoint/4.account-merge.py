"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.


"""



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
            name=account[0]
            for email in account[1:]:
                # if it has been seen before then we will union the current account with the previous account
                if email in emailToAcc:
                    # x -> y
                    uf.union(emailToAcc[email],idx) # 

                emailToAcc[email] = idx

        accToEmails = {} # account -> emails
        print(emailToAcc)       
        for email,acc in emailToAcc.items():
            parent = uf.find(acc)
            # if the parent is not in the dictionary then we will add it
            accToEmails.setdefault(parent,[])

            accToEmails[parent].append(email)

        print(accToEmails)
        res = []

        for parent,emails in accToEmails.items():
            name=accounts[parent][0] # get the name of the account
            res.append([name] + sorted(emails))

        return res

print("TEST CASES")

print(Solution().accountsMerge(
      [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
))
