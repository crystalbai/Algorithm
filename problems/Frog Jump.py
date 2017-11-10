class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dic = {}
        for i in stones:
            dic[i] = set([])
        dic[stones[0]]= [0]
        for i in stones:
            for step in dic[i]:
                if step-1> 0:
                    if i+step-1 in dic:
                        dic[i+step-1].add(step-1)
                if i+step+1 <= stones[-1]:
                    if i+step+1 in dic:
                        dic[i+step+1].add(step+1)
                if i+step <= stones[-1] and step > 0:
                    if i+step in dic:
                        dic[i+step].add(step)
        return len(dic[stones[-1]])>0

sol = Solution()
print sol.canCross([0,1,3,5,6,8,12,17])