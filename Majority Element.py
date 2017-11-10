class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        max_time = 0
        d = {}
        res = 0
        for idx, i in enumerate(nums):
            if i in d:
                d[i] += 1
                if d[i] > max_time:
                    max_time = d[i]
                    res = i
            else:
                d[i] = 1
                if max_time == 0:
                    max_time = d[i]
                    res = i

            if max_time > len(nums) / 2 + 1 or idx == len(nums)-1:
                return res
sol = Solution()
print sol.majorityElement([0,2,2,2,1,1,1,1])