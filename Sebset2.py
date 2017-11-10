import copy
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        cur = [[]]
        nums.sort()
        for i in xrange(len(nums)):
            cur_layer = []
            while len(cur) != 0:
                tmp = cur.pop(0)
                res.append(tmp + [nums[i]])
                cur_layer.append(tmp + [nums[i]])
            if i <len(nums)-1 and nums[i +1] == nums[i]:
                cur = copy.deepcopy(cur_layer)
            else:
                cur = copy.deepcopy(res)
        return res
sol = Solution()
print sol.subsetsWithDup([1,2,2])