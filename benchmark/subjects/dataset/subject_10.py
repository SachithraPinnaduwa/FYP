import math
class Vector3D:
    def __init__(self, x=0, y=0, z=0): self.x, self.y, self.z = x, y, z
    def add(self, v): return Vector3D(self.x+v.x, self.y+v.y, self.z+v.z)
    def dot(self, v): return self.x*v.x + self.y*v.y + self.z*v.z
    def magnitude(self): return math.sqrt(self.x**2 + self.y**2 + self.z**2)
