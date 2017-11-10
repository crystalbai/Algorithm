class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        d = {}
        st = []
        for l in logs:
            s = l.split(':')
            if s[1] == 'start':
                if s[0] in d:
                    d[s[0]].append(int(s[2]))

                else:
                    d[s[0]] = [int(s[2])]
                if len(st) != 0:
                    tmp = d[st[-1]].pop()
                    d[st[-1]].append(int(s[2]) - int(tmp))

                st.append(s[0])
            if s[1] == 'end':
                tmp = d[s[0]].pop()
                d[s[0]].append(int(s[2]) - (int(tmp)-1))
                st.pop()
                if len(st) > 0:
                    d[st[-1]].append(int(s[2])+1)
        res = []
        l = [str(i) for i in range(n)]
        for key in l:
            res.append(sum(d[key]))
        return res


sol = Solution()
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
print sol.exclusiveTime(1, logs)