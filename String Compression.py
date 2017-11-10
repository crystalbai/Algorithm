class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res = []
        cnt = 1
        for idx in range(len(chars)):
            if idx == 0 or chars[idx] != chars[idx - 1]:
                if cnt != 1:
                    res.append(str(cnt))
                cnt = 1
                res.append(chars[idx])
            else:
                cnt += 1
        if cnt != 1:
            res.append(str(cnt))
        res = ''.join(res)
        chars[:len(res)] = res[:]
        return len(res)


sol = Solution()
chars = ["a","a","b","b","c","c","c"]
print sol.compress(chars)
print chars