class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        bit = [0]*32
        count = 0
        while n!= 0:
            bit[count] = n%2
            n = n/2
            count+=1
        for i in bit:
            res = res*2 + i
        return res

sol = Solution()
print sol.reverseBits(43261596)