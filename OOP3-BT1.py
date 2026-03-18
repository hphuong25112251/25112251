import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def PointDistance(pointM, pointN):
        lenght = (pointN.x- pointM.x)**2 + (pointN.y - pointM.y)**2
        return math.sqrt(lenght)

diemA= Point(3,4)
print(f" Diem A la {diemA}")

print("Nhap diem B ")
diemB = Point(int(input(" Nhap x= ")),int(input(" Nhap y= ")))
print(f"Diem B la {diemB}")
diemC = Point(-diemB.x,-diemB.y)
print(f"Diem C la {diemC}")
diemO =Point(0,0)
print(f"Khoang cach giua diem B va diem O la {Point.PointDistance(diemB,diemO)}")
print(f"Khoang cach giua diem A va diem B la {Point.PointDistance(diemB,diemA)}")