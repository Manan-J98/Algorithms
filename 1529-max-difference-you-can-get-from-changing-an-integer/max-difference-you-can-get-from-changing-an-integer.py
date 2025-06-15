class Solution:
    def maxDiff(self, num: int) -> int:
        number = list(str(num))

        # --- Max Value ---
        didChange = None
        for i in range(len(number)):
            if not didChange and number[i] != "9":
                didChange = number[i]
                number[i] = "9"
            elif didChange and number[i] == didChange:
                number[i] = "9"
        maxVal = int(''.join(number))

        # --- Min Value ---
        number = list(str(num))
        didChange = None
        changedTo = None
        for i in range(len(number)):
            if not didChange:
                if i == 0:
                    if number[i] != "1":
                        didChange = number[i]
                        changedTo = "1"
                        number[i] = "1"
                else:
                    if number[i] != "0" and number[i] != "1":
                        didChange = number[i]
                        changedTo = "0"
                        number[i] = "0"
            elif number[i] == didChange:
                number[i] = changedTo
        minVal = int(''.join(number))

        return maxVal - minVal
