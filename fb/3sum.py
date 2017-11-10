# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         nums = sorted(nums)
#         l = 0
#         while l < len(nums)-2:
#             if l > 0 and nums[l] == nums[l-1]:
#                 l+=1
#                 continue
#             mid = l+1
#             r = len(nums)-1
#             while mid < r:
#
#                 if nums[l] + nums[mid] + nums[r] < 0:
#                     mid +=1
#                 elif nums[l] + nums[mid] + nums[r] > 0:
#                     r -=1
#                 elif nums[l] + nums[mid] + nums[r] == 0:
#                     res.append([nums[l], nums[mid], nums[r]])
#                     while mid < r and nums[r] == nums[r - 1]:
#                         r -= 1
#                     while mid < r and nums[mid] == nums[mid + 1]:
#                         mid+=1
#                     mid +=1; r-=1
#             l+=1
#         return res
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        l , r= 0,len(nums)-1
        while l < r-1:
            while l > 0 and l < r-1 and nums[l] == nums[l - 1]:
                l+=1

            m = l+1
            while m < r:
                if nums[l] + nums[m] + nums[r] == 0:
                    res.append([nums[l] , nums[m] , nums[r]])
                    m+=1
                    r-=1
                    while m < r and nums[m-1] == nums[m]:
                        m +=1
                    while m<r and nums[r+1] == nums[r]:
                        r -=1
                elif nums[l] + nums[m] + nums[r] > 0:
                    r-=1
                elif nums[l] + nums[m] + nums[r] < 0:
                    m+=1
            r = len(nums)-1
            l+=1
        return res

sol = Solution()
nums= [-2,0,0,2,2]
res = sol.threeSum(nums)
print res
