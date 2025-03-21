class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        index = 0
        while index < len(command):
            if command[index] == "G":
                res += "G"
                index += 1
            elif command[index] == "(" and command[index+1] != "a":
                res += "o"
                index += 2
            else:
                res += "al"
                index += 4
        return res