class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # setup Nodes
        root = TrieNode()
        for word in dictionary:
            ptr = root
            for char in word:
                if char not in ptr.children:
                    ptr.children[char] = TrieNode()
                ptr = ptr.children[char]
            ptr.isEndOfWord = True

        res = []
        for word in sentence.split(" "):
            ptr = root
            temp = ""
            for char in word:
                if char in ptr.children and ptr.children[char].isEndOfWord:
                    temp += char
                    break
                elif char in ptr.children:
                    ptr = ptr.children[char]
                    temp += char
                else:
                    temp = word
                    break
            res.append(temp)
        return " ".join(res)
                

                