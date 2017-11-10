class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        for idx,n in enumerate(nums):
            res_tmp = self.permute(nums[:idx]+nums[idx+1:])
            res = res + [ x+[n] for x in res_tmp]
        return res

sol = Solution()
print sol.permute([3,2,1])