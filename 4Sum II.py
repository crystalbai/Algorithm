import copy
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        st = [0]
        dic = {0: A, 1: B, 2: C}
        for i in range(0, 3):
            cur = st
            st = []
            while len(cur) != 0:
                node = cur.pop(0)
                for ele in dic[i]:
                    st.append(node + ele)
        res = 0
        for ele in D:
            cur = copy.deepcopy(st)
            while len(cur) != 0:
                node = cur.pop(0)
                if node + ele == 0:
                    res += 1
        return res



sol = Solution()
print sol.fourSumCount([1,2],[-2,-1],[-1,2],[0,2])