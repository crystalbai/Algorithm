class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        stack = []
        count = 0
        nums = sorted(nums)
        if nums == []:
            return []
        for idx, i in enumerate(nums):
            if idx == 0:
                res.append([i])
                stack.append((count, idx))
                count += 1
            if idx > 0 and i != nums[idx-1]:
                res.append([i])
                stack.append((count, idx))
                count +=1
        while len(stack) != 0:
            ele = stack.pop(0)
            if ele[1] < len(nums) -1:
                for shift in range(ele[1]+1, len(nums)):

                        tmp = res[ele[0]][:]+[nums[shift]]
                        if tmp != res[-1]:
                            res.append(tmp)
                            stack.append([count, shift])
                            count+=1

        res = res +[[]]
        return res

sol = Solution()
print sol.subsetsWithDup([1,2,2,2,3,3])
