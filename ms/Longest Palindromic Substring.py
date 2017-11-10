class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = 1
        max_len = 1
        s_res = s[0]
        for idx in range(len(s) - 1):
            s_tmp = s[idx+1:]
            # idx2 is length-1
            if s[idx] in s_tmp:
                idx2 = s_tmp.index(s[idx])
            else:
                continue
            if idx2 - idx+1 <= max_len:
                continue
            while self.check_palindrome(s, idx, idx2 + 1 + idx):
                max_len = idx2 - idx+1
                s_res = s[idx:idx2+2+idx]
                s_tmp = s[idx2+2+idx:]
                if s[idx] in s_tmp:
                    idx2 += s_tmp.index(s[idx])+1
                else:
                    break
        return s_res

    def check_palindrome(self, s, idx, idx2):
        i, j = idx, idx2
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

sol = Solution()
print sol.longestPalindrome('bababd')