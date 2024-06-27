from turtle import Turtle


N = 600
n = 15
D = 10

up = 90
down = 270
left = 180
right = 0


black = "black"
white = "white"
red = "red"
blue = "blue"
pink = "pink"
green = "green"

sqr = "square"


class Snake:

    def __init__(self):
        self.speed = 3;
        self.segment = []
        self.create()
        self.head = self.segment[0]


    def create(self):
        for i in range(0, 15):
            a = Turtle(sqr)
            a.penup()
            a.color(red)
            a.goto(-i*self.speed, 0)
            a.shapesize(0.5)
            self.segment.append(a);


    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            x = self.segment[i-1].xcor()
            y = self.segment[i-1].ycor()
            self.segment[i].goto(x, y)

        self.segment[0].forward(self.speed)


    def add(self, position):
        a = Turtle(sqr)
        a.penup()
        a.color(red)
        a.goto(position)
        a.shapesize(0.5)
        self.segment.append(a);


    def extend(self):
        for i in range(0, 5):
            self.add(self.segment[-1].position())


    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)


    def incr_speed(self):
        if self.speed < 7:
            self.speed += 0.1

