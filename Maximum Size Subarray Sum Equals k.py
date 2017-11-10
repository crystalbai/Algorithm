class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_d = {0: [0]}
        s = 0
        for i in range(len(nums)):
            s = s + nums[i]
            if s not in sum_d:
                sum_d[s] = [i + 1]
            else:
                sum_d[s].append(i+1)
        m = 0
        for key in sum_d:
            if key-k in sum_d:
                if m < max(sum_d[key]) - min(sum_d[key-k]):
                    m = max(sum_d[key]) - min(sum_d[key-k])
        return m




sol = Solution()
print sol.maxSubArrayLen([-2, -1, 2, 1], 1)
print sol.maxSubArrayLen([1,-1,5,-2,3],3)
print sol.maxSubArrayLen([1, -1, 5, -2, 3],3)