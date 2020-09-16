# single responsability
class incorrect:
    def __init__(self,text):
        self.text = text 
    def manipulate(self):
        self.text.upper()
    def printt(self):
        print(self.text)

class manipulate():
    def __init__(self,text):
        self.text = text
    def manipulate(self):
        self.text.upper()

class printt():
    def __init__(self,text):
        self.text = text 
    def printt(self):
        print(self.text)


# open close principle
# bad
# original class: 
class Employe:
    def __init__(self,_id,name):
        self.id = _id 
        self.name = name 
    def bonus(self,salary):
        return salary*0.1
print(Employe(25,"Someone"))
del Employe
# we add another functionality to the same class 
class Employe:
    def __init__(self,_id,salary,name,t):
        self.id = _id 
        self.name = name 
        self.salary = salary
        self.type = t
    def bonus(self):
        if (self.type == "Permanent"):
            return self.salary*0.1
        else:
            return self.salary*0.05
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, salary bonus:{self.salary}"
print(Employe(25,"Someone",25000,"Permanent"))
del Employe
# good: leave the original untouched
class Employe:
    def __init__(self,_id,name):
        self.id = _id 
        self.name = name 
        self.salary = None
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, salary bonus:{self.salary}"
# implement the new class without the type dif.
class PermanentEmploye(Employe):
    def __init__(self,_id,name,salary):
        self.id = _id 
        self.name = name
        self.salary = salary*0.05
class TemporaryEmploye(Employe):
    def __init__(self,_id,name,salary):
        self.id = _id 
        self.name = name
        self.salary = salary*0.05
em_1 = PermanentEmploye(25,"Someone_perm",90_000)
em_2 = TemporaryEmploye(25,"Someone_temp",90_000)
# print(em_1)
# print(em_2)

# Liskov principle
class T:
    def do(self,a,b):
        return a*b
class S(T):
    def do(self,a,b):
        return a/b
# New exception: 
t_ = T().do(78,0)
s_ = S().do(78,0) # ZeroDivisionError
class Line(Shape):
    def calculate_surface_area(self):
        return -1 # a line does not have a surface area

# dependency inversion principle
class CEO:
    def instruct(self,instructions):
        return instructions
    def do_ceo_stuff(self,do):
        for i in do: 
            print(i)

class truck_driver(CEO):
    def carry_out_those_instructions(self,instructions):
        exec(instructions)

# interface segregation
class Shape:
   def draw_circle(self): # circle 
       pass
   def draw_square(self): # square
       pass

class Circle(Shape):
   def draw_circle(self): # circle
       pass
   def draw_square(self): # square?
       pass

# solution 
class Shape:
   def draw(self): # draw
      pass
class Circle(Shape): # inherits shape
   def draw(self):
      pass
class Square(Shape): # inherits shape
   def draw(self):
      pass
