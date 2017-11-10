class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        l = list(str(num))
        l_sort = sorted(l, reverse=True)
        i = 0
        while i< len(l) and l_sort[i]== l[i]:
            i+=1
        if i == len(l):
            return num
        j= len(l)-1
        max_j = j
        while j > i:
            if l[max_j] < l[j]:
                max_j = j
            j-=1
        l[i], l[max_j] = l[max_j], l[i]
        return int(''.join(l))
sol = Solution()
# print sol.maximumSwap('10909091')
print sol.maximumSwap('9973')