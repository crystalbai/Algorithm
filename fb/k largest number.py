class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        bar = nums[0]
        l,r = [],[]
        num_bar = 0
        if len(nums) == 0:
            return ""
        for i in nums:
            if i < bar:
                l.append(i)
            elif i > bar:
                r.append(i)
            else:
                num_bar+=1
        if len(r) >= k:
            return self.findKthLargest(r, k)
        if len(r) < k and len(r) >= k-num_bar:
            return bar
        if len(r) < k - num_bar:
            return self.findKthLargest(l, k-len(r)-num_bar)

sol = Solution()
print sol.findKthLargest([3,2,1,5,5,6,4,7],7)
