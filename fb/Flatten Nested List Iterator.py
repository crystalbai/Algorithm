# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):

   def __init__(self, list):
        self.list = list

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       return isinstance( self.list, int )


   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
       return self.list

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
       return self.list

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.curList = nestedList
        self.curInd = -1
        self.move_to_next()

    def move_to_next(self):
        self.curInd += 1
        while self.curInd >= len(self.curList) and len(self.stack) > 0:
            self.curList, self.curInd = self.stack.pop()
            self.curInd += 1
        if self.curInd >= len(self.curList) and len(self.stack) == 0:
            return False

        while True:
            tmp_nest = self.curList[self.curInd]
            if tmp_nest.isInteger():
                break
            elif len(tmp_nest.getList()) == 0:
                self.move_to_next()
                break
            self.stack.append((self.curList, self.curInd))
            self.curList = tmp_nest.getList()
            self.curInd = 0


    def next(self):
        """
        :rtype: int
        """

        if self.hasNext():
            res = self.curList[self.curInd].getInteger()
            self.move_to_next()
            return res
        return None



    def hasNext(self):
        """
        :rtype: bool
        """

        return self.curInd < len(self.curList)

        # Your NestedIterator object will be instantiated and called as such:
        # i, v = NestedIterator(nestedList), []
        # while i.hasNext(): v.append(i.next())

nestedList = [NestedInteger([NestedInteger(1), NestedInteger(1)]), NestedInteger(2), NestedInteger([NestedInteger([NestedInteger([NestedInteger([])])]), NestedInteger([])]), NestedInteger([NestedInteger(1), NestedInteger(1)])]
# nestedList = [NestedInteger([NestedInteger(1)]), NestedInteger([])]
# nestedList = [NestedInteger([NestedInteger([NestedInteger([])])]), NestedInteger([])]
i = NestedIterator(nestedList)
while i.hasNext(): print i.next()