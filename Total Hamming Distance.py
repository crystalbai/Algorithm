class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bina = []
        for i, n in enumerate(nums):
            bina.append([])
            while n != 0:
                bina[i].append(n % 2)
                n /= 2
            while len(bina[i]) != 4:
                bina[i].append(0)
            bina[i].reverse()
        res = 0
        for l in range(len(nums)):
            for j in range(l+1, len(nums)):
                res += sum([abs(bina[l][t]-bina[j][t]) for t in range(4) ])
        return res


sol = Solution()
print sol.totalHammingDistance([4,14,2])