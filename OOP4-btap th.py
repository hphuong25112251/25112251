from point import Point
import copy
class LineSegment:
    def _init_(self,*args):
        if len(args)== 0:
            self._d1 = Point(8,5)
            self._d2 = Point(1,0)
        if len(args)== 2:
            if isinstance(args[0], Point):
                self._d1 = args[0]
                self._d2 = args[1]
        if len(args)== 4:
            if isinstance(args[0], int):
                self._d1 = Point(args[0],args[1])
                self._d2 = Point(args[2],args[3])
        if len(args)== 1:
            if isinstance(args[0], LineSegment):
                self._d1 = copy.deepcopy(args[0]._d1)
                self._d2 = copy.deepcopy(args[0]._d2)
    def _str_(self):
        return "[{%d,%d}, {%d,%d}]" % (self._d1.x(), self._d1.y(), self._d2.x(), self._d2.y())
l1= LineSegment()
print(l1)   

p1= Point()
p2= Point()
p1.read()
p2.read()
l2= LineSegment(p1,p2)
print(l2)           

l3= LineSegment(3,4,5,6)
print(l3)
 
l4= LineSegment(l3)
print(l4)