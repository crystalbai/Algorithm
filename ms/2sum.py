class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = [(v, i) for i, v in enumerate(nums)]
        tmp.sort(key=lambda x: x[0])
        nums_sorted, indices = zip(*tmp)

        i, j = 0, len(nums_sorted) - 1
        while i < j:
            if nums_sorted[i] + nums_sorted[j] < target:
                i += 1
            elif nums_sorted[i] + nums_sorted[j] > target:
                j -= 1
            else:
                return sorted([indices[i], indices[j]])
sol = Solution()
print sol.twoSum([150,24,79,50,88,345,3], 200)