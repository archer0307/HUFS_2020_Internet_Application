import sys
sys.stdout = open('output_ex7.txt','w')

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

class Point:
    x = 0      # class attributes
    y = 0      

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def distance(self, q):
        return ((self.x - q.x)**2 + (self.y - q.y)**2) ** 0.5

    def distance_from_origin(self):
        return (self.x **2 + self.y ** 2) ** 0.5

    #############################################################

    def __eq__(self,other): # Question 1 of point class
        return self.x == other.x and self.y == other.y
    
    def __ne__(self,other): # Question 1 of point class
        return self.x != other.x and self.y == other.y
    
    def reflect_x(self):    # Question 2 of point class
        self.y *= -1
        return "Point({0}, {1})".format(self.x, self.y)

    def slope_from_origin(self):    # Question 3 of point class
        try :
            return self.y/self.x
        except ZeroDivisionError:
            print('You cannot get slope in origin.') # dx must not be 0
    
    def get_slope_to(self,q):   # Question 4 of point class
        try :
            return abs((self.y-q.y)/(self.x-q.x))
        except ZeroDivisionError:
            print('You cannot get slope between two points which are same with x') # dx must not be 0

    def get_line_to(self,q):    # Question 4 of point class
        a = Point.get_slope_to(self,q)
        b = self.y-a*self.x
        a = int(a) if a == int(a) else a
        b = int(b) if b == int(b) else b
        return (a,b)

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at Point posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(
            self.corner, self.width, self.height)
    
    def __repr__(self):
        return  "Rectangle({0}, {1}, {2})".format(
            repr(self.corner), self.width, self.height)
    
    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    #########################################################

    def area(self): # Question 1 of rectangle class
        return self.width*self.height
    
    def perimeter(self):    # Question 2 of rectangle class
        return 2*(self.width+self.height)
    
    def flip(self): # Question 3 of rectangle class
        self.width,self.height = self.height,self.width
    
    def contains(self,q): # Question 4 of rectangle class
        contain_x = True if q.x<self.corner.x+self.width and q.x>=self.corner.x else False
        contain_y = True if q.y<self.corner.y+self.height and q.y>=self.corner.y else False
        return contain_x and contain_y
        

#print(Point(3,5).reflect_x())
#print(Point(4,10).slope_from_origin())
#print(Point(4,11).get_line_to(Point(6,15)))

test(Point(3,5).reflect_x()=='Point(3, -5)')
test(Point(4,10).slope_from_origin()==2.5)
test(Point(4,11).get_line_to(Point(6,15))==(2,3))

#r = Rectangle(Point(100,50),10,5)
#print(r.area()) 
#print(r.perimeter())
#r.flip()
#print(r.width==5 and r.height==10)

r = Rectangle(Point(100,50),10,5)
test(r.area() == 50)
test(r.perimeter() == 30)
r.flip()    # this method modifies its attributes
test(r.width == 5 and r.height == 10)

r = Rectangle(Point(0,0),10,5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))