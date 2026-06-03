import turtle


class Figure:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        self.draw("black")

    def hide(self):
        self.draw("white")

    def draw(self, color):
        pass


class Grid(Figure):
    def draw(self, color):
        self.t.clear()
        self.t.pencolor(color)
        self.t.pensize(5)

        for x_pos in [-50, 50]:
            self.t.penup()
            self.t.goto(x_pos, 150)
            self.t.pendown()
            self.t.goto(x_pos, -150)

        for y_pos in [-50, 50]:
            self.t.penup()
            self.t.goto(-150, y_pos)
            self.t.pendown()
            self.t.goto(150, y_pos)


class Cross(Figure):
    def draw(self, color):
        self.t.clear()
        self.t.pencolor(color)
        self.t.pensize(4)
        size = 30

        self.t.penup()
        self.t.goto(self.x - size, self.y + size)
        self.t.pendown()
        self.t.goto(self.x + size, self.y - size)

        self.t.penup()
        self.t.goto(self.x - size, self.y - size)
        self.t.pendown()
        self.t.goto(self.x + size, self.y + size)


class Zero(Figure):
    def draw(self, color):
        self.t.clear()
        self.t.pencolor(color)
        self.t.pensize(4)
        radius = 30

        self.t.penup()
        self.t.goto(self.x, self.y - radius)
        self.t.pendown()
        self.t.circle(radius)


class TicTacToeGame:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Хрестики-Нулики")
        self.window.setup(400, 400)

        self.grid = Grid()
        self.grid.show()

        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_turn = 'X'
        self.placed_figures = []

    def get_cell_coordinates(self, row, col):
        x = (col - 1) * 100
        y = (1 - row) * 100
        return x, y

    def handle_click(self, click_x, click_y):
        if -150 <= click_x <= 150 and -150 <= click_y <= 150:
            col = int((click_x + 150) // 100)
            row = int((150 - click_y) // 100)

            col = min(max(col, 0), 2)
            row = min(max(row, 0), 2)

            if self.board[row][col] is None:
                cell_x, cell_y = self.get_cell_coordinates(row, col)

                if self.current_turn == 'X':
                    shape = Cross()
                    shape.setPosition(cell_x, cell_y)
                    shape.show()
                    self.board[row][col] = 'X'
                    self.current_turn = 'O'
                else:
                    shape = Zero()
                    shape.setPosition(cell_x, cell_y)
                    shape.show()
                    self.board[row][col] = 'O'
                    self.current_turn = 'X'

                self.placed_figures.append(shape)

    def start(self):
        self.window.onclick(self.handle_click)
        self.window.listen()
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToeGame()
    game.start()