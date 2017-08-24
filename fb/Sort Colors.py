class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return []
        count = [0] * 3
        for i in nums:
            count[i]+=1
        res = [0] * count[0]+[1]*count[1]+[2]* count[2]
        nums[:] = res[:]

sol = Solution()
list = [0,2,1,0,0,2,1,1]
sol.sortColors([])
print list