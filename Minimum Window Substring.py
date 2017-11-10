class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ## using two pointeres, first get a valid substring, then shrink from the head pointer
        if s == "" or t == "":
            return ""
        d, dt = dict.fromkeys(t,0), dict.fromkeys(t,0)
        for i in t:
            dt[i]+=1
        pi,pj,cont = 0,0,0
        ans = ""
        while pj < len(s):
            if s[pj] in dt:
                d[s[pj]]+=1
                if d[s[pj]]<=dt[s[pj]]:
                    cont +=1
            if cont == len(t):

                while pi <= pj:
                    if s[pi] in dt:
                        d[s[pi]] -= 1
                        if d[s[pi]] < dt[s[pi]]:
                            if ans == "" or pj-pi < len(ans):
                                ans = s[pi:pj+1]
                            cont-=1
                            pi+=1
                            break
                    pi+=1
            pj+=1
        return ans
sol = Solution()
print sol.minWindow("ADOBECODEBANC","ABC")