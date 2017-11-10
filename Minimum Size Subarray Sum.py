class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        n = len(nums)
        res = n + 1
        s_tmp = 0
        for r in range(n):
            s_tmp += nums[r]
            while s_tmp >= s:
                res = min(res, r - l + 1)
                s_tmp -= nums[l]
                l += 1
        return res if res != n + 1 else -1

sol = Solution()
print sol.minSubArrayLen(7,[2,3,1,2,4,3])