class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        l = 0
        while l < len(nums)-2:
            if l > 0 and nums[l] == nums[l-1]:
                l+=1
                continue
            mid = l+1
            r = len(nums)-1
            while mid < r:

                if nums[l] + nums[mid] + nums[r] < 0:
                    mid +=1
                elif nums[l] + nums[mid] + nums[r] > 0:
                    r -=1
                elif nums[l] + nums[mid] + nums[r] == 0:
                    res.append([nums[l], nums[mid], nums[r]])
                    while mid < r and nums[r] == nums[r - 1]:
                        r -= 1
                    while mid < r and nums[mid] == nums[mid + 1]:
                        mid+=1
                    mid +=1; r-=1
            l+=1
        return res

sol = Solution()
nums= [-1,0,1,2,-1,-4]
res = sol.threeSum(nums)
print res
