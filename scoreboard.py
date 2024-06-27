from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0;
        self.color("cyan")
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)
        self.penup()
        self.color("white")
        self.goto(0, 300)
        self.write(f"Score : {self.score}", align = "center", font = ("Arial", 24, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.color("cyan")
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)
        self.penup()
        self.color("white")
        self.goto(0, 300)
        self.write(f"Score : {self.score}", align = "center", font = ("Arial", 24, "normal"))

    def gameover(self):
        self.goto(0, 0);
        self.write("GAME OVER", align = "center", font = ("Arial", 24, "normal"))

