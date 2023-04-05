import math 

class Figur: 
     def __init__(self, name): 
        self.name = name 
 
     def umfang(self): 
        return 0 
 
     def __str__(self): 
        return self.name

# -------------------------------------------------------------

class Punkt(Figur):
     def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y
     
     def distanz(self, other):
         return math.sqrt(((self.x-other.x)**2)+((self.y-other.y)**2))
         

     def __str__(self):
        return f"Punkt({self.x},{self.y})"

# -------------------------------------------------------------   
 
class Dreieck(Figur): 
     def __init__(self, A, B, C):
          super().__init__("Dreieck") 
          self.A = A
          self.B = B
          self.C = C
     
     def umfang(self):
          return self.A.distanz(self.B) + self.B.distanz(self.C) + self.C.distanz(self.A)

     def __str__(self):
          return f"Dreieck {self.A}, {self.B}, {self.C}"
     
# -------------------------------------------------------------

class Kreis(Figur):
     def __init__(self, M, r):
          super().__init__("Kreis")
          self.M = M
          self.r = r
     
     def umfang(self):
         return self.r * math.pi * 2

     def __str__(self):
          return f"Kreis M={self.M} r={self.r}"

# -------------------------------------------------------------

class Rechteck(Figur):
     def __init__(self, Pmin, Pmax):
          super().__init__("Rechteck")
          self.Pmin = Pmin
          self.Pmax = Pmax
     
     def umfang(self):
         return (abs(self.Pmax.x - self.Pmin.x))*2 + (abs(self.Pmax.y - self.Pmin.y))*2

     def __str__(self):
          return f"Rechteck: {self.Pmin}, {self.Pmax}"
     
# -------------------------------------------------------------

class Polygon(Figur):
     def __init__(self, Punktliste):
          super().__init__("Polygon")
          self.pl = Punktliste
     
     def umfang(self):
          s = 0
          for i in range(0, len(self.pl)-1):
             l1 = self.pl[i]
             l2 = self.pl[i+1]
             s = s + l1.distanz(l2)
          return s
     
     def __str__(self):
          s = f"Polygon: "
          for punkt in self.pl:
              s = s + f"{punkt} "
          return s
     

d1 = Punkt(1,1)
d2 = Punkt(2,2)
d3 = Punkt(2,1)
D1 = Dreieck(d1,d2,d3)
print(D1.umfang())
print(D1)

polygonliste = [Punkt(1,1), Punkt(2,4), Punkt(3,3.5), Punkt(4,4), Punkt(4,1), Punkt(1,1)]

p = Polygon(polygonliste)
print(p)