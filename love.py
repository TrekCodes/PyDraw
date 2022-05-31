import turtle

from main import my_goto

t = turtle.Turtle()
turtle.title("Love Programming")
screen = turtle.Screen()
screen.bgcolor("white")
t.color("yellow", "red")
t.begin_fill()
t.speed(2)
t.pensize(3)
t.fillcolor("red")
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

if __name__ == '__main__':
    my_goto(-100, -200)
    turtle.write('Heart Program', font=("Arial", 24, "bold"),)
    turtle.mainloop()
