import numpy as np
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in reversed(range(nums.__len__())):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)

        print nums

sol = Solution()
nums = [0,0,1]
sol.moveZeroes(nums)
print nums
