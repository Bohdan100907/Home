import turtle
import random


class Stem:
    def __init__(self, length):
        self.length = length

    def draw(self, t):
        t.color("green")
        t.pensize(4)
        t.setheading(270)
        t.forward(self.length)


class Leaf:
    def __init__(self, size):
        self.size = size

    def draw(self, t, position_ratio):
        t.color("forest green")
        t.pensize(2)

        t.setheading(135)
        t.begin_fill()
        t.circle(self.size, 90)
        t.left(90)
        t.circle(self.size, 90)
        t.end_fill()

        t.setheading(45)
        t.begin_fill()
        t.circle(-self.size, 90)
        t.right(90)
        t.circle(-self.size, 90)
        t.end_fill()


class Petal:
    def __init__(self, size, color, count):
        self.size = size
        self.color = color
        self.count = count

    def draw(self, t):
        t.color(self.color)
        t.pensize(1)
        angle = 360 / self.count

        for _ in range(self.count):
            t.begin_fill()
            t.circle(self.size, 60)
            t.left(120)
            t.circle(self.size, 60)
            t.left(120)
            t.end_fill()
            t.left(angle)

        t.color("yellow")
        t.setheading(270)
        t.forward(self.size / 3)
        t.setheading(0)
        t.begin_fill()
        t.circle(self.size / 3)
        t.end_fill()


class Flower:
    def __init__(self, petal_color, size=40, stem_length=150):
        self.stem = Stem(stem_length)
        self.leaf = Leaf(size * 0.8)
        self.petal = Petal(size, petal_color, count=random.choice([5, 6, 8]))
        self.stem_length = stem_length

    def draw(self, t, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

        self.stem.draw(t)

        t.penup()
        t.goto(x, y - self.stem_length / 2)
        t.pendown()
        self.leaf.draw(t, 0.5)

        t.penup()
        t.goto(x, y)
        t.pendown()
        self.petal.draw(t)


def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("lightcyan")
    screen.title("Bouquet")

    t = turtle.Turtle()
    t.speed(0)

    colors = ["crimson", "darkorchid", "orange", "hotpink", "dodgerblue", "tomato"]
    positions = [(-150, 50), (-70, 90), (0, 120), (70, 90), (150, 50)]

    for x, y in positions:
        color = random.choice(colors)
        size = random.randint(35, 50)
        stem_len = random.randint(180, 240)

        flower = Flower(petal_color=color, size=size, stem_length=stem_len)
        flower.draw(t, x, y)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()