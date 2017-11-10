class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        res = 0
        while len(s) != 0:
            seed = s.pop()
            tmp_len = 1
            l = seed - 1
            r = seed + 1
            cur_len = len(s)
            pre_len = -1
            while cur_len != pre_len:
                pre_len = cur_len
                if l in s:
                    tmp_len += 1
                    s.remove(l)
                    l -= 1

                if r in s:
                    tmp_len += 1
                    s.remove(r)
                    r += 1

                res = max(tmp_len, res)
                cur_len = len(s)
        return res



sol = Solution()
print sol.longestConsecutive([100,4,200,1,3,2])