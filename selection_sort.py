#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        minindex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        return minindex
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            minimum = self.select(arr, i)
            arr[i], arr[minimum] = arr[minimum], arr[i]
