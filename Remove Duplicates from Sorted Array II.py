class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        y = 1
        if len(nums)<=2:
            return len(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count+=1
            else:
                count =1
            if count <= 2:
                nums[y] = nums[i]
                y+=1
        return y
sol = Solution()
print sol.removeDuplicates([1])