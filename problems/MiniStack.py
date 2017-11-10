class MiniStack(object):
    def __init__(self):
        self.st = []
    def push(self, ele):
        if len(self.st)== 0:
            self.st.append(ele)
        else:
            tmp_st = []
            while len(self.st)>0 and self.st[-1]>ele:
                tmp_st.append(self.st.pop())
            self.st.append(ele)
            while len(tmp_st) !=0:
                self.st.append(tmp_st.pop())
my_stack = MiniStack()
my_stack.push(2)
my_stack.push(10)
my_stack.push(6)
my_stack.push(7)
my_stack.push(3)
my_stack.push(7)
my_stack.push(2)
print my_stack.st