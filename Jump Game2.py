class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        g_max = 0
        step = 0
        i = 0
        last = 0
        cur = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i>last:
                last = g_max
                step+=1
            g_max = max(g_max, nums[i]+i)
        return step
sol = Solution()
print sol.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3])
