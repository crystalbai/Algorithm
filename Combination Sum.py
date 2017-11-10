class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d = {}
        res = []
        d_cur = {}
        if len(candidates) == 0 and target == 0:
            return [[]]
        if len(candidates) == 0 and target != 0:
            return -1

        candidates = list(set(candidates))
        candidates.sort()
        for ele in candidates:
            tmp_ele = ele
            tmp_list = [ele]
            if ele < target:
                if tmp_ele not in d:
                    d[tmp_ele] = [tmp_list[:]]
                else:
                    d[tmp_ele].append(tmp_list[:])
            if ele == target:
                res.append([ele])
        while len(d) > 0 and min(d.keys()) + candidates[0] <= target:
            d_cur = d
            d = {}
            for ele in candidates:
                for k in d_cur:
                        tmp_r = k + ele
                        if tmp_r == target:
                            res = res + [d_i + [ele] for d_i in d_cur[k] if d_i[-1] <= ele]
                        if tmp_r < target:
                            if tmp_r not in d:
                                d[tmp_r] = [d_i + [ele] for d_i in d_cur[k] if d_i[-1] <= ele]
                            else:
                                d[tmp_r] = d[tmp_r]+[d_i + [ele] for d_i in d_cur[k]if d_i[-1] <= ele]


        return res

    def combinationSum2(self,candidates, target):
        candidates = list(set(candidates))
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret

    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])


sol = Solution()
print sol.combinationSum2([8,7,4,3],11)

