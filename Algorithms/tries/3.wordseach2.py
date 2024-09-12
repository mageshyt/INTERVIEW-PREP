class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()


    def insert(self, word: str) -> None:
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]

        curr.isEnd=True





class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie=Trie()

        for word in words:
            trie.insert(word)

        ROWS,COLS=len(board),len(board[0])

        res=set() 

        def dfs(i,j,root,word):
            if root.isEnd:
                res.add(word)

            if i<0 or i>=ROWS or j<0 or j>=COLS:
                return

            temp=board[i][j]

            if temp not in root.children:
                return

            board[i][j]="#"

            for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
                dfs(i+x,j+y,root.children[temp],word+temp)

            board[i][j]=temp


        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,trie.root,"")


        return list(res)



        return list(result)
print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])) # ["eat","oath"]
