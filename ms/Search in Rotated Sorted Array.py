import math
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0,len(nums)-1
        while l <= r:
            h = int((l+r)/2)
            if nums[h] == target:
                return h
            # if the first part is ordered
            if nums[l] <= nums[h] and target >= nums[l] and target < nums[h]:
                r = h-1
            elif nums[l] <= nums[h] and not(target >= nums[l] and target < nums[h]):
                l = h+1
            #the second part is ordered
            elif nums[l] >= nums[h] and target > nums[h] and target <= nums[r]:
                l = h+1
            else:
                r = h-1
        return -1

sol = Solution()
print sol.search([3,1],
1)