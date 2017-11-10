class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums_str = sorted([str(i) for i in nums], cmp = self.cmp)
        res = ''.join(nums_str)
        res = res.lstrip('0')
        return res or '0'

    def cmp(self, a, b):
        if a + b < b + a:
            return 1
        else:
            return -1
sol = Solution()
print sol.largestNumber([0,0])