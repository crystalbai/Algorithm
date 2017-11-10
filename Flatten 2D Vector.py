class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.v = vec2d
        self.cur = []

    def next(self):
        """
        :rtype: int
        """
        if len(self.cur):
            cur = self.cur.pop(0)
        else:
            self.cur = self.v.pop(0)
            cur = self.cur.pop(0)
        return cur

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.v) != 0 or len(self.cur) != 0


        # Your Vector2D object will be instantiated and called as such:
vec2d = [[1,2],[3],[4,5,6]]
i, v = Vector2D(vec2d), []
while i.hasNext():
    v.append(i.next())
print v
