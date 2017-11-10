class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for l in strs:
            key_l = ''.join(sorted(l))
            if key_l not in d:
                d[key_l] = [l]
            else:
                d[key_l].append(l)
        res = []
        for key in d:
            res.append(d[key])
        return res

sol = Solution()
print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])