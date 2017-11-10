
import math
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or (len(nums) == 1 and nums[0] != target):
            return -1
        while len(nums) > 0:
            mid = int((len(nums)-1) / 2)
            if nums[mid] == target:
                return mid
            if nums[0] < nums[mid]:
                if target <= nums[mid]:
                    tmp = self.binarySearch(nums[:mid], target)
                    if tmp >=0:
                        return tmp
                tmp = self.search(nums[mid+1:], target)
                if tmp > -1:
                    return mid +tmp+1
                else:
                    return -1
            else:
                if target <= nums[-1]:
                    tmp = self.binarySearch(nums[mid+1:],target)
                    if tmp>=0:
                        return mid+ tmp+1

                return self.search(nums[:mid],target)

        return -1
    def search2(self, nums, target):
        ## find the index of the smallest location
        lo, high = 0, len(nums)-1
        while(lo < high):
            mid = (lo + high) / 2
            if (nums[mid] > nums[high]):
                lo = mid+1
            else:
                high = mid
        shift = lo
        lo = 0; hi = len(nums)-1
        while lo <= hi:
            mid = int((lo+ hi)/2)
            mid_real = (mid+shift) % len(nums)
            if target == nums[mid_real]:
                return mid_real
            if target > nums[mid_real]:
                lo = mid+1
            else:
                hi = mid-1
        return -1



    def binarySearch(self, nums, target):
        first, mid, last = 0, 0, len(nums)-1

        while first <= last:
            mid = int((first + last) / 2);
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    first = mid +1
                else:
                    last = mid - 1
        return -1
sol = Solution()
print sol.search2([7,9,1,3,5], 1)

