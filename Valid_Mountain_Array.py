class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        dec = False
        for i in range(len(arr)-1):
            if i == 0 and arr[i+1] <= arr[i]:
                return False
            if dec:
                if arr[i+1] >= arr[i]:
                    return False
            else:
                if arr[i+1] < arr[i]:
                    dec = True
                elif arr[i+1] == arr[i]:
                    return False
        return dec
