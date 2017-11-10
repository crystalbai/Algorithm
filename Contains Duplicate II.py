class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(max(0, i - k), min(len(nums), i + k)):
                if nums[i] == nums[j] and i!=j:
                    return True
        return False


sol = Solution()
print sol.containsNearbyDuplicate([1,2,3,4,1],2)