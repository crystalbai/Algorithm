class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [[0, 0]]
        r = [[0, 0]]
        num_z = 0
        num_one = 0
        for i in nums:
            if i == 0:
                num_one += 1
            else:
                num_z += 1
            l.append([num_z, num_one])
        num_z = 0
        num_one = 0
        for i in nums[::-1]:
            if i == 0:
                num_one += 1
            else:
                num_z += 1
            r.append([num_z, num_one])
        total = l[-1]
        res = 0
        for i in range(len(nums) + 1):
            for j in range( len(nums) + 1-i):
                tmp0, tmp1 = total[0] - l[i][0] - r[j][0], total[1] - l[i][1] - r[j][1]
                if tmp0 == tmp1:
                    res = max(res, tmp0 + tmp1)
        return res


sol = Solution()
print sol.findMaxLength([0,0,1,1,1])