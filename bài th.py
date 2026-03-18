class Point:
    x = int
    y = int 
def print_Point(self):
    print(f"({self.x}, {self.y})")
diemB= Point()
diemB.x = 3
diemB.y = 4
print_Point(diemB)
print ("%d,%d"  % (diemB.x, diemB.y))
diemB.x = int(input("Nhập x: "))
diemB.y = int(input("Nhập y: "))
print_Point(diemB)