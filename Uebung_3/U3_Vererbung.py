import math 

class Figur: 
     def __init__(self,name): 
        self.name = name 
 
     def umfang(self): 
        return 0 
 
     def __str__(self): 
        return self.name
   
class Punkt(Figur):
     def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y
     
     def __str__(self):
        return f"Punkt({self.x},{self.y})"
    
class Dreieck(Figur): 
     def __init__(self, p1, p2, p3):
          super().__init__("Dreieck") 
          self.p1 = p1
          self.p2 = p2
          self.p3 = p3
     
     def umfang(self):
          a = ((self.p3.x-self.p1.x)**2+(self.p3.y-self.p1.y)**2)**(1/2)
          b = ((self.p3.x-self.p2.x)**2+(self.p3.y-self.p2.y)**2)**(1/2)
          c = ((self.p2.x-self.p1.x)**2+(self.p2.y-self.p1.y)**2)**(1/2)
          return a+b+c

     def __str__(self):
          return f"Dreieck P1={self.p1.x, self.p1.y}, P2={self.p2, self.p2.y}, P3={self.p3.x, self.p3.y}"
             
#class Rechteck(Figur):
     def __init__(self, p1):
          super().__init__("Rechteck")




class Kreis(Figur):
     def __init__(self, mittelpunkt, radius):
          super().__init__("Kreis")
          self.mittelpunkt = mittelpunkt
          self.radius = radius
     
     def umfang(self):
         return self.radius * math.pi * 2

     def __str__(self):
          return f"Kreis M={self.mittelpunkt} r={self.radius}"

class Polygon(Figur):
     def __init__(self):
          super().__init__("Polygon")
     
     def __str__(self):
          return f"Polygon "
     

#d1 = Punkt(1,1)
#d2 = Punkt(2,2)
#d3 = Punkt(2,1)
#D1 = Dreieck(Punkt(1.4,1.4), Punkt(2.5,2.5), Punkt (3.1,3.1))
#print(D1)

d1 = Punkt(1,1)
d2 = Punkt(2,2)
d3 = Punkt(3,3)

#Dr = (d1, d2, d3)
print(d1.x)
print(d2)
print(d3)

#
# print(Dr)