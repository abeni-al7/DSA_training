class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = []
        current = 0
        for num in nums:
            current += num
            self.prefix.append(current)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        rightSum = self.prefix[right]
        if left == 0:
            leftSum = 0
        else:
            leftSum = self.prefix[left - 1]

        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
