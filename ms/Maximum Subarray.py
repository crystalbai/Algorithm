class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_be = 0
        sub = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                sub += nums[i]
            else:
                if nums[i] > -sub:
                    sum_be = sum_be + nums[i]+sub
                else:
                    sub = 0
                    sum_be = 0
        return sum_be

sol = Solution()
print sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])