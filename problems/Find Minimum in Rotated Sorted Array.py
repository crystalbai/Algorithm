class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) / 2
            if (mid-1 >= 0 and (nums[mid] < nums[mid -1]) and (mid+ 1 < len(nums) and nums[mid] < nums[mid+1])):
                return nums[mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]


sol = Solution()
print sol.findMin([3,1,2])