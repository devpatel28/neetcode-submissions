class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        Max = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(arr[i], Max)
            arr[i] = Max
            Max = newMax

        return arr