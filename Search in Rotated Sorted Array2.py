class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        first, last = 0, len(nums)-1

        while first <= last:
            mid = int((first + last) / 2)
            if nums[mid] == target:
                return  True
            if nums[first] < nums[mid]:
                if target>= nums[first] and target <= nums[mid]:
                    last = mid-1
                else:
                    first = mid+1
            elif nums[first] > nums[mid]:
                if target >= nums[mid] and target <= nums[last]:
                    first = mid + 1
                else:
                    last = mid -1
            else:
                first += 1
        return False

sol = Solution()
print sol.search([1,3,5],1)

