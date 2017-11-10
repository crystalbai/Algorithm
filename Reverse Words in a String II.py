# class Solution:
#     # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
#     # @return nothing
#     def reverseWords(self, s):
#         res = []
#         while len(s)!=0:
#             res.append(s.pop())
#         s= res
#         print s
class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        str.reverse()
        s = 0
        for i in range(len(str)):
            print i
            if str[i] == ' ':
                str[s:i] = str[s:i][::-1]
                s = i+1
        str[s:] = str[s:][::-1]
sol = Solution()
s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
sol.reverseWords(s)
print s