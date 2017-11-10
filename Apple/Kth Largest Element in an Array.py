class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        if l < 2:
            return nums[0]
        nums[0], nums[int((len(nums))/2)] = nums[int((len(nums))/2)] , nums[0]
        pivot = nums[0]
        last_small = 0

        for i in range(1, len(nums)):
            if nums[i] < pivot:
                last_small += 1
                nums[last_small], nums[i] = nums[i], nums[last_small]

        nums[last_small], nums[0] = nums[0], nums[last_small]
        if k == l - last_small:
            return pivot
        if k < l - last_small:
            nums = nums[last_small+1:]
            return self.findKthLargest(nums, k)

        else:
            nums = nums[:last_small]
            return self.findKthLargest(nums, k - (l - last_small))

sol= Solution()
print sol.findKthLargest([7,6,5,4,3,2,1],
5)