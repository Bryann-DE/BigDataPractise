class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

rect=Rectangle(10,15)
print("Rectangle length: ",rect.length,"\nRectangle Breadth: ",rect.breadth)
# output:
# Rectangle length:  10
# Rectangle Breadth:  15

#-----Inheritance----
class Shape:  #parent class
    def color(self,color):
        self.color=color
    def calc_area(self):
        pass
    def color_cost(self):
        cost={'Red':10,'Brown':12,'Black':22}
        return self.calc_area()*cost[self.color]

from math import  pi
class Circle(Shape):  #Inheritence of Shape into Circle class
    def __init__(self,radius):
        self.radius=radius
    def calc_area(self):
        return pi*self.radius

c=Circle(5)
print("Circle Area: ",c.calc_area())
c.color='Red'
print("Circle Radius: ",c.radius,"\nCircle color: ",c.color,"\nCircle Color Cost: ",c.color_cost())

#Output:Circle
# Area:  15.707963267948966
# Circle Radius:  5
# Circle color:  Red
# Circle Color Cost:  157.07963267948966

#---Overwriting Class Method---
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calc_area(self):
        return self.length*self.breadth
    def color_cost(self):
        cost={'Blue':192,'Black':24,'Pink':1234}
        return 1.25*(self.calc_area()*cost[self.color])

rect = Rectangle(10,24)
print("Rectangle Area: ",rect.calc_area())
rect.color='Pink'
print("Rectangle Dimensions: ",rect.length,",",rect.breadth,"\nRectangle color: ",rect.color,"\nRectangle Color Cost: ",rect.color_cost())

#Output:
#Rectangle Area:  240
# Rectangle Dimensions:  10 , 24
# Rectangle color:  Pink
# Rectangle Color Cost:  370200.0