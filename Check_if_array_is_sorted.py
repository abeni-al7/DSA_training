#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        l, r = 0, 1
        while r < n:
            if arr[r] < arr[l]:
                return False
            l += 1
            r += 1
        return True
