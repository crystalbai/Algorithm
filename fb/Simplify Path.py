class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = path.split('/')
        st = []
        out = 0
        if len(path) == 0:
            return ''
        if all (i in {'','.','..'}for i in l):
            return '/'
        for i in l:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if len(st) > 0:
                    st.pop()
                else:
                    out +=1
            else:
                st.append(i)
        ans = ''
        # for i in range(out):
        #     ans = ans + '/..'
        for i in st:
            ans = ans + '/' + i
        return ans
sol = Solution()
print sol.simplifyPath('/../')