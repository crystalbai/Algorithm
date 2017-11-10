class Solution(object):
    def getLongestMatch(self, a, b, loc_a, loc_b):
        a_cur = a[loc_a:]
        b_cur = b[loc_b:]
        print len(a_cur)
        print len(b_cur)
        m = 0
        if a_cur == b_cur:
            return len(a_cur)
        if len(a_cur) == 0 or len(b_cur) == 0:
            return 0
        idx_a = 0
        while idx_a < len(a_cur) and a_cur[idx_a] not in b_cur:
            idx_a += 1
        if idx_a < len(a_cur):
            idx_b = b_cur.index(a_cur[idx_a])
        else:
            return 0
        m = max(self.getLongestMatch(a_cur,b_cur, idx_a+1, idx_b+1)+1,m)
        m = max(self.getLongestMatch(a_cur,b_cur, idx_a+1, 0),m)
        return m

sol = Solution()
print sol.getLongestMatch(['a','b','c','d','e','f'], ['a','c','e','d','g','b'],0,0)
s1 = ['a' for x in xrange(1000)]
s2 = ['a' for x in xrange(2)]
print sol.getLongestMatch(s1, s2, 0, 0)