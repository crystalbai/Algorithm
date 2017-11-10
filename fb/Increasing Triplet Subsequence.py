class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = float('inf'), float('inf')
        for i in nums:
            if i < first:
                first = i
            elif i < second:
                second = i
            else:
                return True
        return False

sol = Solution()
print sol.increasingTriplet([1, 7, 5])
