import copy


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        tamp = {}
        n2 = len(s2)
        n1 = len(s1)
        for i in s1:
            if i in tamp:
                tamp[i] += 1
            else:
                tamp[i] = 1
        for idx in range(n2-n1+1):
            if s2[idx] in tamp:
                ##compare
                tmp = copy.deepcopy(tamp)
                tmp_ans = True
                for j in range(idx, idx + n1):
                    if s2[j] in tmp:
                        tmp[s2[j]] -= 1
                        if tmp[s2[j]] < 0:
                            tmp_ans = False
                            break
                    else:
                        tmp_ans = False
                        break
                if tmp_ans == True:
                    return True
        return False
sol = Solution()
print sol.checkInclusion("ab","eidboaoo")