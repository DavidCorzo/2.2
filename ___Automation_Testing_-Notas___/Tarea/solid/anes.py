# interface segregation
class Shape:
   def draw_triangle(self): 
       # draws triangle
       pass
   def draw_rectangle(self): 
       # draws rectangle
       pass

class Triangle(Shape):
   def draw_circle(self): # draws triangle
       pass
   def draw_square(self): 
       # Also draws square?
       pass

# solution 
class Shape:
   def draw(self): # draw
      pass
class Triangle(Shape):
   def draw(self):
       # only draws the triangle
      pass
class Square(Shape): 
   def draw(self):
       # only draws the square
      pass
