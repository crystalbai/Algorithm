class Solution(object):
    # def maxSubArrayLen(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     if len(nums) == 0:
    #         return 0
    #     dic = {0:0}
    #
    #     for i in range(0,len(nums),1):
    #         dic[i+1] = nums[i]+dic[i]
    #     for l in range(len(nums),0,-1):
    #         for i in range(len(nums)):
    #             if i+l <= len(nums):
    #                 if dic[i+l]-dic[i] == k:
    #                     if dic[i] == 0:
    #                         return i+l
    #                     return l
    #     return 0
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:-1}
        count = 0; acc = 0
        for i in xrange(len(nums)):
            acc = acc + nums[i]
            if acc not in dic:
                dic[acc] = i
            if acc - k in dic:
                count = max(count, i - dic[acc - k])
        return count
sol = Solution()
# res = sol.maxSubArrayLen([-1],-1)
# res = sol.maxSubArrayLen([-2,-1, 2, 1],1)
res = sol.maxSubArrayLen([1, -1, 5, -2, 3],3)
print res
