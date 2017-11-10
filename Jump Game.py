class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = nums[-1]
        m = 1
        for idx, i in enumerate(nums[:-1]):
            m = max(m, idx+1+i)
        return m>n


