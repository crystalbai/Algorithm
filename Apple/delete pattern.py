class Solution(object):
    def get_remove(self, dic, str):
        cur_pos = len(str)-1
        while cur_pos>=0:
            for i in dic:
                if len(str)-cur_pos >= len(i):
                    if str[cur_pos:cur_pos+len(i)] == i:
                        str = str[:cur_pos]+ str[cur_pos+len(i):]

            cur_pos-=1
        return str


sol = Solution()
dic = ["ab", "cd"]
str = "ccabdfds"
print sol.get_remove(dic, str)
