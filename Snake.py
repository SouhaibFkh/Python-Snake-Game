POSITIONS = [(0,0),(-20,0),(-40,0)]
DOWN = 270
UP = 90
RIGHT = 0
LEFT = 180

from turtle import Turtle , Screen, down, pos, up

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
            for seg in range(len(self.segments)-1,0,-1):
                new_x = self.segments[seg -1].xcor()
                new_y = self.segments[seg -1].ycor()
                self.segments[seg].goto(new_x,new_y)   
            self.head.forward(20)
            
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)            
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def create_snake(self):
        for new_posit in POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.pu()
            new_segment.goto(new_posit)
            self.segments.append(new_segment)