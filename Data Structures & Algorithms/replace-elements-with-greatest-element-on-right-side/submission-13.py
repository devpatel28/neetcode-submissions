class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        Max = -1
        for i in range(len(arr) - 1, -1, -1):
            maxLoop = max(arr[i], Max)
            arr[i] = Max
            Max = maxLoop
        return arr