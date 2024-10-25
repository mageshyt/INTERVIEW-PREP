


from typing import List
from collections import defaultdict,deque

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        adj=defaultdict(list)
        in_degree={c:0 for word in dict for c in word}

        for i in range(n-1):
            word1,word2=dict[i],dict[i+1]

            # find the first character that is different
            for j in range(min(len(word1),len(word2))):
                if word1[j]!=word2[j]:
                    # add the edge from word1[j] to word2[j]
                    adj[word1[j]].append(word2[j])
                    in_degree[word2[j]]+=1
                    break
        print(in_degree)
        # find the nodes with 0 indegree
        q=deque()

        for node in in_degree:
            if in_degree[node]==0:
                q.append(node)

        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    q.append(neighbor)

        return "".join(res) if len(res)==len(in_degree) else ""





print(Solution().findOrder(["baa","abcd","abca","cab","cad"],5,4)) # "wertf"
