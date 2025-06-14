class Solution:
    def minMaxDifference(self, num: int) -> int:
        arr = list(str(num))
        didChange = None
        for i in range(len(arr)):
            if didChange and arr[i] == didChange:
                arr[i] = '9'
            elif not didChange and arr[i] != '9':
                didChange = arr[i]
                arr[i] = '9'
        maxNum = int(''.join(arr))
        arr = list(str(num))
        didChange = None
        for i in range(len(arr)):
            if didChange and arr[i] == didChange:
                arr[i] = '0'
            elif not didChange and arr[i] != '0':
                didChange = arr[i]
                arr[i] = '0'
        minNum = int(''.join(arr))
        return maxNum - minNum
        
