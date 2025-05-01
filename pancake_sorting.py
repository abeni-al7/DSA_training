class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k = []
        fixed = len(arr)
        while fixed > 0:
            maxind = 0
            for i in range(fixed):
                if arr[i] > arr[maxind]:
                    maxind = i
            arr[:maxind+1] = arr[:maxind+1][::-1]
            arr[:fixed] = arr[:fixed][::-1]
            k.append(maxind+1)
            k.append(fixed)
            fixed -= 1
        return k
