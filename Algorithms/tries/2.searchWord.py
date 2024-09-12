

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()


    def addWord(self, word: str) -> None:
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]

        curr.isEnd=True

    def search(self, word: str) -> bool:

        # Recursive function to search the word

        def dfs(root,i):
            curr=root

            for j in range(i,len(word)):
                ch=word[j]

                # case 1 if the ch is '.'

                if ch=='.':
                    for child in curr.children:
                        if dfs(curr.children[child],j+1):
                            return True
                    return False

                # case 2 if the ch is not '.'

                else:
                    if ch not in curr.children:
                        return False
                    curr=curr.children[ch]

            return curr.isEnd

        return dfs(self.root,0)

print("Word Dictionary")

# Test case 1
wordDictionary = WordDictionary()

wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) # return True
print(wordDictionary.search("b..")) # return True

