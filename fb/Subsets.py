class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        stack = []
        count = 0
        if nums == []:
            return []
        for idx, i in enumerate(nums):
            res.append([i])
            stack.append((count, idx))
            count +=1
        while len(stack) != 0:
            ele = stack.pop(0)
            if ele[1] < len(nums) -1:
                for shift in range(ele[1]+1, len(nums)):
                    tmp = res[ele[0]][:]+[nums[shift]]
                    res.append(tmp)
                    stack.append([count, shift])
                    count+=1

        res = res +[[]]
        return res

sol = Solution()
print sol.subsets([1,2,3])


