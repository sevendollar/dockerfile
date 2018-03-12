import turtle, time

def turtle_walk(size=100):
    jef = turtle.Turtle()
    jef.shape('turtle')
    jef.color('blue')
    size = size
    line_mark = 10
    turtle_mark = 20
    angle = 30
    for i in range(12):
        jef.penup()
        jef.forward(size)
        jef.pendown()
        jef.forward(line_mark)
        jef.penup()
        jef.forward(turtle_mark)
        jef.stamp()
        jef.back(size + line_mark + turtle_mark)
        # time.sleep(2)
        jef.right(angle)


def main():
    windows = turtle.Screen()
    windows.bgcolor('lightgreen')
    windows.title('Hello, Jef!')
    for i in range(100, 301, 100):
        turtle_walk(i)
    windows.mainloop()

if __name__ == '__main__':
    main()
