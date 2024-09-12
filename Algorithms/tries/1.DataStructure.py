# Tries
class TriedNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Tries:
    def __init__(self):
        self.root = TriedNode()

    def insert(self,word):
        curr= self.root

        for ch in word:
            # if the char is not present the curr node children then add it

            if ch not in curr.children:
                curr.children[ch] = TriedNode()

            curr = curr.children[ch]

        curr.isEnd = True

    def search(self,word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False

            curr = curr.children[ch]

        return curr.isEnd


    def startsWith(self,prefix):
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False

            curr = curr.children[ch]

        return True

# Testing

t = Tries()

t.insert("apple")

print(t.search("apple")) # True
print(t.search("app")) # False
print(t.startsWith("app")) # True
t.insert("app")
print(t.search("app")) # True
