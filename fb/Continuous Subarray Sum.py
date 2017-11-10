class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # start, end = 0,len(nums)
        acc = 0
        dict = []
        for i in xrange(len(nums)):
            acc = acc + nums[i]
            dic_cur = dict
            dict = []
            for key in dic_cur:
                if (acc - key) % k == 0 and acc != key:
                    return True
                else:
                    dict.append(acc - key)
            dict.append(acc)
        return False

sol = Solution()
print sol.checkSubarraySum([23, 2, 6, 4, 7], 6)


