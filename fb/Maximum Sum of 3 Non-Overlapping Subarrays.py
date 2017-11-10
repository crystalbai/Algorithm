class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # get the sum list form the begining
        # get the max sum it could have count from the left
        # get the max sum it could get count from the right

        sum_l = [0]*len(nums)
        k_sum_l = [0] * len(nums)
        k_sum_r = [0] * len(nums)
        sum_l[0] = nums[0]
        for i in range(1,len(nums)):
            sum_l[i] = sum_l[i-1] + nums[i]
        k_sum_l[k-1] = sum_l[k-1]
        for i in range(k, len(nums)):
            k_sum_l[i] = k_sum_l[i-1] if k_sum_l[i-1]> sum_l[i]-sum_l[i-k] else sum_l[i]-sum_l[i-k]
        k_sum_r[len(nums)-k] = sum_l[len(nums)-k]
        for j in range(len(nums)-k-1, -1, -1):
            k_sum_r[j] = k_sum_r[j + 1] if k_sum_r[j + 1] > sum_l[j+k] - sum_l[j] else sum_l[j+k] - sum_l[j]
        res_sum = 0
        res_loc = []
        for i in range(k, len(nums)-k):
            if res_sum < k_sum_l[i-1] + sum_l[i+k-1]-sum_l[i-1] + k_sum_r[i+k]:
                res_sum =

