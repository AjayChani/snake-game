import random
import pygame
import tkinter
from tkinter import messagebox
pygame.init()


class Snake:        # Sanke class
    s_color = (255, 0, 0)
    e_color = (0, 0, 0)

    def __init__(self, win, x, y):
        self.x = x
        self.y = y
        s = pygame.draw.rect(win, Snake.s_color, (x, y, 20, 20))
        eye1 = pygame.draw.circle(win, Snake.e_color, (x+6, y+4), 2, 1)
        eye2 = pygame.draw.circle(win, Snake.e_color, (x + 14, y + 4), 2, 1)


class Body(Snake):      # snake body
    def __init__(self, win, x, y):
        self.x = x
        self.y = y
        b = pygame.draw.rect(win, Snake.s_color, (x, y, 20, 20))


def food(win, x, y, food_x, food_y, tail):      # food
    food_x, food_y = check_food(food_x, food_y)
    if food_x == x and food_y == y:
        tail += 1
        food_x = random.randint(0, 29) * 20
        food_y = random.randint(0, 29) * 20
    pygame.draw.rect(win, (0, 255, 0), (food_x, food_y, 20, 20))
    return food_x, food_y, tail


def check_food(food_x, food_y):     # check food on the body or not
    for _ in range(len(body_x_co)):
        if food_x == body_x_co[_] and food_y == body_y_co[_]:
            food_x = random.randint(0, 29) * 20
            food_y = random.randint(0, 29) * 20
            check_food(food_x, food_y)
    return food_x, food_y


def draw_win(win, x, y, food_x, food_y, tail):      # draw screen/window
    win.fill((0, 0, 0))
    sn = Snake(win, x, y)
    for i in range(0, tail):    # number of body boxes
        bo = Body(win, x_co[len(x_co) - i - 1], y_co[len(y_co) - i - 1])
        body_x_co.append(x_co[len(x_co) - i - 1])
        body_y_co.append(y_co[len(y_co) - i - 1])
    food_x, food_y, tail = food(win, x, y, food_x, food_y, tail)
    for _ in range(len(body_x_co)):     # check if snake bite its tail
        if x == body_x_co[_] and y == body_y_co[_]:
            game_over()
            tail = 0
    return food_x, food_y, tail


def game_over():    # Game over message
    root = tkinter.Tk()
    root.withdraw()

    messagebox.showinfo("Game Over", "Try again...")


x_co = []       # x movment co-ordinates
y_co = []       # y movment co-ordinates
body_x_co = []  # body x movment co-ordinates
body_y_co = []  # body y movment co-ordinates 


def main():
    global x_co, y_co, body_x_co, body_y_co
    width = 600
    height = 600

    x = 200     # Start x
    y = 200     # Start y

    food_x = random.randint(0, 29) * 20
    food_y = random.randint(0, 29) * 20
    tail = 0

    dirx = 1
    diry = 0

    win = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Snake")
    win.fill((0, 0, 0))
    pygame.display.update()

    run = True
    while run:      # main game loop
        pygame.time.delay(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if dirx != 1:
                dirx = -1
                diry = 0
        elif keys[pygame.K_RIGHT]:
            if dirx != -1:
                dirx = 1
                diry = 0
        elif keys[pygame.K_UP]:
            if diry != 1:
                dirx = 0
                diry = -1
        elif keys[pygame.K_DOWN]:
            if diry != -1:
                dirx = 0
                diry = 1

        if dirx == 1:
            x = x+20 if x <= width-21 else 0
        if dirx == -1:
            x = x-20 if x >= 20 else width-20
        if diry == -1:
            y = y-20 if y >= 20 else height-20
        if diry == 1:
            y = y+20 if y <= height-21 else 0

        pygame.time.delay(50)
        body_y_co.clear()
        body_x_co.clear()

        food_x, food_y, tail = draw_win(win, x, y, food_x, food_y, tail)

        x_co.append(x)
        y_co.append(y)

        pygame.display.flip()


if __name__ == '__main__':
    main()
