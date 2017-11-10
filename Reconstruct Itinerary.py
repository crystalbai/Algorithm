import collections
import copy

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        n = len(tickets)+1
        tickets.sort(key = lambda x:(x[0],x[1]))
        d = collections.defaultdict(list)
        for i in tickets:
            d[i[0]].append(i[1])
        res = ["JFK"]
        exist = self.dfs(d, res,n)
        return self.res if exist else ""


    def dfs(self, d, res, n):
        if len(res) == n:
            self.res = res
            return True
        is_true = False
        for i in range(len(d[res[-1]])):
            tmp_d = copy.deepcopy(d)
            if res[-1] not in tmp_d or len(tmp_d[res[-1]])==0:
                return False
            node = tmp_d[res[-1]].pop(i)
            is_true = self.dfs(tmp_d, res+[node], n)
            if is_true:
                return True
        return is_true



sol = Solution()
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print sol.findItinerary(tickets)