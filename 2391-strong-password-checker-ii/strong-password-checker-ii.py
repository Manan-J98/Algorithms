class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        length = lCase = uCase = digit = sp = adj = False
        SPECIAL = set("!@#$%^&*()-+")
        if len(password) >= 8:
            length = True
        for i in range(len(password)):
            if password[i].islower():
                lCase = True
            if password[i].isupper():
                uCase = True
            if password[i].isdigit():
                digit = True
            if password[i] in SPECIAL:
                sp = True
            if (i < len(password) - 1) and password[i] == password[i+1]:
                adj = True
        
        return length and lCase and uCase and digit and sp and not adj