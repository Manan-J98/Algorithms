class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        avg = sum(arr[0:k])/k
        print(avg)
        res = 1 if avg >= threshold else 0
        i, j = 1, k
        while j < len(arr):
            avg = (((avg * k) - arr[i-1]) + arr[j]) / k
            print("new", avg)
            if avg >= threshold:
                res += 1
            i += 1
            j += 1
        return res
