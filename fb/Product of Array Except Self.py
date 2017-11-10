class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bf = [0]*len(nums)
        af = [0]*len(nums)
        p_b = 1
        p_a = 1
        res = []
        if len(nums) == 0:
            return []
        for i in range(len(nums)):
            p_b = p_b*nums[i]
            bf[i] = p_b
            p_a = p_a * nums[-i-1]
            af[-i-1]= p_a
        for i in xrange(len(nums)):
            tmp = 1
            if i -1 >=0:
                tmp = tmp * bf[i-1]
            if i+1 < len(nums):
                tmp = tmp* af[i+1]
            res.append(tmp)
        return res

sol = Solution()
print sol.productExceptSelf([1,2,3,4])


            