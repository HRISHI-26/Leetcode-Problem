class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        p1 = z - x
        p2 = z - y
        if abs(p1) > abs(p2):
            return 2
        elif abs(p2) > abs(p1):
            return 1
        else:
            return 0