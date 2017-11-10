class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        d = {}
        res = ''
        for w in words:
            for l in w:
                if l not in d:
                    d[l] = [0,[]]


        for i_w, w in enumerate(words[:-1]):
            for idx, l in enumerate(words[i_w+1]):
                if idx >= len(words[i_w]):
                    break
                if words[i_w+1][idx]!= words[i_w][idx]:
                    d[l][0]+=1
                    d[words[i_w][idx]][1].append(l)
                    break
        pre = len(d)
        while len(d)!= 0:
            for key in d.copy():
                if d[key][0] == 0:
                    res = res + key
                    for i in d[key][1]:
                        d[i][0] -=1
                    del d[key]

            if len(d) == pre:
                return ""
            pre =len(d)
        return res

sol = Solution()
# print sol.alienOrder([
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ])
print sol.alienOrder(["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"])






