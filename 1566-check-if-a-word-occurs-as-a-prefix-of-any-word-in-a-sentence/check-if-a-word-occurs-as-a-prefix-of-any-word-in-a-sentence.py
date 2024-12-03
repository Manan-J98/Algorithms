class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        fp = 0
        for index, string in enumerate(sentence.split(" ")):
            while fp < len(string) and fp < len(searchWord) and string[fp] == searchWord[fp]:
                print(string[fp], searchWord[fp])
                fp += 1
                if fp == len(searchWord):
                    return index+1
            fp = 0
        return -1
