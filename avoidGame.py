# TODO:
# add list score
# add restart after loose
# add possibility to decide how many ball in the Game


# needed for the tkinter party and creating balls
# import tkinter
from tkinter import *
import random
import time

# constant for widget hight and width
WIDTH = 700
HIGHT = 600

# crating the tkinter canvas with high and width
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HIGHT)
tk.title("Avoid Game")
canvas.pack()

# Timer
from timeit import default_timer


def updateTime():
    now = default_timer() - start
    minutes, secondes = divmod(now, 60)
    houres, minutes = divmod(minutes, 60)
    str_time = " %d : %02d : %02d " % (houres, minutes, secondes)
    canvas.itemconfigure(text_clock, text=str_time)
    # tk.after(1000,updateTime)


start = default_timer()
text_clock = canvas.create_text(500, 20)

# creating ball class that create an oval with size color etc


class Ball:
    # kind of constructor
    def __init__(self, color, size):
        self.shape = canvas.create_oval(10, 10, size, size, fill=color)
        self.xSpeed = random.uniform(-3.5, 3.5)
        self.ySpeed = random.uniform(-3.5, 3.5)
        # avoid geting a deth ball that don't move
        if self.xSpeed == 0:
            self.xSpeed = random.uniform(-3.5, 3.5)
        if self.ySpeed == 0:
            self.ySpeed = random.uniformu(-3.5, 3.5)
    # method that move the ball

    def move(self):
        canvas.move(self.shape, self.xSpeed, self.ySpeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HIGHT or pos[1] <= 0:
            self.ySpeed = -self.ySpeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xSpeed = -self.xSpeed
        return pos


# Ball color that will be in the list colors
colors = ['red', 'green', 'orange', 'yellow', 'red', 'cyan', 'magenta',
          'dodgerblue', 'turquoise', 'grey', 'gold', 'pink']

# creating ball list emty
balls = []

# filling the ball list with multiple ball
for i in range(40):
    balls.append(Ball(random.choice(colors), 45))

# Cord of mouse
x = tk.winfo_pointerx()
y = tk.winfo_pointery()
abs_coord_x = tk.winfo_pointerx() - tk.winfo_rootx()
abs_coord_y = tk.winfo_pointery() - tk.winfo_rooty()

# Creation of rec
rec = canvas.create_rectangle(
    abs_coord_x - 15, abs_coord_y - 15, abs_coord_x + 15, abs_coord_y + 15, fill='black')

# Moving the balls and updating the canvas to have a smooth view


def moveBall():
    A = True
    while A:
        # updating mouse cords
        x = tk.winfo_pointerx()
        y = tk.winfo_pointery()
        abs_coord_x = tk.winfo_pointerx() - tk.winfo_rootx()
        abs_coord_y = tk.winfo_pointery() - tk.winfo_rooty()
        # moving rec
        rectCord = canvas.coords(
            rec, abs_coord_x - 15, abs_coord_y - 15, abs_coord_x + 15, abs_coord_y + 15)
        # moving balls
        for ball in balls:
            cordOval = ball.move()
            if cordOval[3] <= abs_coord_y + 47 and cordOval[1] >= abs_coord_y - 47 and cordOval[2] <= abs_coord_x + 47 and cordOval[0] >= abs_coord_x - 47:
                # print('touched at :\n \t cursor in : \n \t\t x1 = ', abs_coord_x - 15, ' x2 = ', abs_coord_x + 15, ' y1 = ', abs_coord_y - 15, ' y2 = ', abs_coord_y +
                #      15, ' \n \t ball in :\n \t\t cordOval[0] = ', cordOval[0], 'cordOval[1] = ', cordOval[1], 'cordOval[2] = ', cordOval[2], 'cordOval[3] = ', cordOval[3])
                A = False

        # updating the canvas
        tk.update()
        updateTime()
        time.sleep(0.01)


moveBall()
tk.mainloop()
