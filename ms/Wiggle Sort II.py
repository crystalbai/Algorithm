class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        s, t = (len(nums) + 1) >> 1, len(nums) - 2
        for i in xrange(s):
            if i % 2 == 1:
                nums[i], nums[t] = nums[t], nums[i]
                t -= 2

sol =   Solution()
a=[1,5,1,1,6,4]
sol.wiggleSort(a)
print a