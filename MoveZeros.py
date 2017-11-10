class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        y = 0
        for idx in range(len(nums)):
            if nums[idx]:
                nums[y] = nums[idx]
                y += 1
        nums[y:] = [0]*len(nums[y:])

        return nums

sol = Solution()
print sol.moveZeroes([0, 1, 0, 3, 12])