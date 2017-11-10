class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        t = list(nums)
        for i in range(len(nums)):
            nums[i] = t[i-k]

sol = Solution()
a = [1,2]
sol.rotate(a,1)
print a