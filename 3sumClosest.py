class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = nums[0] + nums[1] + nums[2]

        for l in range(len(nums)-2):
            mid = l + 1; r = len(nums)-1

            while mid < r:
                tmp_sum = nums[l] + nums[mid] + nums[r]
                if abs(target - res) > abs(target - tmp_sum):
                    res = tmp_sum
                if target - tmp_sum > 0:
                    mid+=1
                else:
                    r-=1
        return res

sol = Solution()
l = [0,2,1,-3]
res = sol.threeSumClosest(l, 1)
print res


