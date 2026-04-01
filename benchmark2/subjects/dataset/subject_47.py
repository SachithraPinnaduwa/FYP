class QuadTreePoint:
    def __init__(self, x: float, y: float, data: any):
        self.x = x
        self.y = y
        self.data = data

class QuadTreeNode:
    def __init__(self, x: float, y: float, w: float, h: float, capacity: int = 4):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.capacity = capacity
        self.points = []
        self.divided = False
        self.nw = self.ne = self.sw = self.se = None

    def insert(self, point: QuadTreePoint) -> bool:
        if (point.x < self.x or point.x > self.x + self.w or 
            point.y < self.y or point.y > self.y + self.h):
            return False

        if len(self.points) < self.capacity and not self.divided:
            self.points.append(point)
            return True

        if not self.divided:
            self._subdivide()

        return (self.nw.insert(point) or self.ne.insert(point) or
                self.sw.insert(point) or self.se.insert(point))

    def _subdivide(self):
        hw = self.w / 2
        hh = self.h / 2
        self.nw = QuadTreeNode(self.x, self.y, hw, hh, self.capacity)
        self.ne = QuadTreeNode(self.x + hw, self.y, hw, hh, self.capacity)
        self.sw = QuadTreeNode(self.x, self.y + hh, hw, hh, self.capacity)
        self.se = QuadTreeNode(self.x + hw, self.y + hh, hw, hh, self.capacity)
        self.divided = True