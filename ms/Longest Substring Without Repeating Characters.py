class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        d = {}
        max_l = 1
        res = s[0]
        i = 0
        start = 0
        while i < len(s):
            if s[i] in d:
                start = max(d[s[i]] + 1, start)
                if max_l < i - start+1:
                    max_l = i - start+1

                    res = s[d[s[i]]:i]
            d[s[i]] = i
            i += 1
            max_l = max(max_l, i - start)
        return max_l

sol = Solution()
print sol.lengthOfLongestSubstring('pwwkew')