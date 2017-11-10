class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        l = [1]* len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    l[i] = max(l[j] + 1, l[i])
        return max(l)
sol = Solution()
print sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])