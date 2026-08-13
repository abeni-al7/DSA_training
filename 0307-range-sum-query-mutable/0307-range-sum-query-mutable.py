class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.seg = [0] * (4 * self.n)
        self.arr = nums
        self.build(0, 0, self.n - 1)
    
    def build(self, node, l, r):
        if l == r:
            self.seg[node] = self.arr[l]
            return

        mid = (l + r) // 2
        self.build(2*node+1, l, mid)
        self.build(2*node+2, mid + 1, r)
        self.seg[node] = self.seg[2*node + 1] + self.seg[2*node + 2]
    
    def update_helper(self, node, l, r, ind, val):
        if l == r:
            self.arr[ind] = val
            self.seg[node] = val
            return
        
        mid = (l + r) // 2
        if ind <= mid:
            self.update_helper(2*node + 1, l, mid, ind, val)
        else:
            self.update_helper(2*node + 2, mid+1, r, ind, val)
        
        self.seg[node] = self.seg[2*node + 1] + self.seg[2*node + 2]
    
    def query(self, node, l, r, ql, qr):
        if ql > qr:
            return 0
        
        if l == ql and r == qr:
            return self.seg[node]
        
        mid = (l + r) // 2
        left_sum = self.query(2*node+1, l, mid, ql, min(mid, qr))
        right_sum = self.query(2*node+2, mid+1, r, max(ql, mid+1), qr)
        return left_sum + right_sum
        
    def update(self, index: int, val: int) -> None:
        self.update_helper(0, 0, self.n - 1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(0, 0, self.n - 1, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)