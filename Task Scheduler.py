class Solution(object):

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        tasks.sort()
        ins_dir = {}
        m = 1
        m_count = 0
        if n == 0:
            return len(tasks)
        if len(tasks) == 0:
            return 0
        for i in tasks:
            ins_dir[i] = ins_dir[i] + 1 if i in ins_dir else 1
            if ins_dir[i] == m:
                m_count+=1
            if ins_dir[i] > m:
                m = ins_dir[i]
                m_count = 1
        emptySlots = (m-1) * (n + 1)+m_count
        taskLeft = len(tasks) - emptySlots
        idles = max(0, -taskLeft)
        return len(tasks) + idles
sol = Solution()
print sol.leastInterval(["A","A","A","B","B","B"], 2)