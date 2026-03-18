import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

    def corners(self):
        x, y = self.corner.x, self.corner.y
        return [
            Point(x, y),
            Point(x + self.width, y),
            Point(x, y + self.height),
            Point(x + self.width, y + self.height)
        ]

# SỬA LỖI TẠI ĐÂY: Đưa Circle ra ngoài cùng cấp với Rectangle
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def point_in_circle(circle, point):
    dx = point.x - circle.center.x
    dy = point.y - circle.center.y
    distance = math.sqrt(dx**2 + dy**2)
    return distance <= circle.radius

def rect_in_circle(circle, rect):
    for corner in rect.corners():
        if not point_in_circle(circle, corner):
            return False
    return True

def rect_circle_overlap(circle, rect):
    # Kiểm tra xem có góc nào nằm trong vòng tròn không
    for corner in rect.corners():
        if point_in_circle(circle, corner):
            return True
    return False

# Chạy thử
c = Circle(Point(150, 100), 75)
p = Point(160, 120)
print("Point in circle?", point_in_circle(c, p))

r = Rectangle(Point(140, 90), 20, 20)
print("Rectangle in circle?", rect_in_circle(c, r)) # Dòng 48 (hoặc 44 tùy cách đếm)
print("Rectangle overlap circle?", rect_circle_overlap(c, r))