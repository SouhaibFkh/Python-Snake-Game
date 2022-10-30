from turtle import Turtle, hideturtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("White")
        self.score = 0
        self.pu()
        self.hideturtle()
        self.goto(0,270)
    
    def scoreb(self,score):
        self.clear()
        self.write(f"Score: {score}",True,"Center",font=('Arial', 22, 'normal'))
        self.goto(0,270)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",True,"Center",font=('Arial', 30, 'normal'))
