import random
import sys
import os.path
import os

import pygame
from pygame.locals import *
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYUP, KEYDOWN, K_SPACE

def main():
    dev = False
    kabe = "＃"
    miti = "　"
    Player_img = "Ｏ"
    Goal_img = "＋"

    #base status
    Y_max = 25
    X_max = 25

    board_column = []
    Board = []


    g_rand = [i+1 for i in range(X_max) if i < X_max-1 and i % 2 == 0]
    a = random.choice(g_rand)

    Goal_pos = [X_max-2,a]
    Player_pos = [1,1]
    Player_dir = 2
    
    #board base
    for x in range(X_max):
        for y in range(Y_max):
            if x == 0 or x == X_max-1 or y == 0 or y == Y_max-1:
                board_column.append(kabe)
            elif x % 2 == 0 and y % 2 == 0:
                board_column.append(kabe)
            else:
                board_column.append(miti)
        Board.append(board_column)
        board_column = []


    #randomize     
    for x in range(X_max):
        for y in range(Y_max):
            a = 0
            if x > 0 and y > 0 and X_max-1 > x and Y_max-1 > y:
                if x % 2 == 0 and y % 2 == 0:
                    ran_list = []
                    ran = None

                    if Board[x][y+1] == miti:
                        ran_list.append(1)
                    if Board[x+1][y] == miti:
                        ran_list.append(2)
                    if Board[x][y-1] == miti:
                        ran_list.append(3)
                    if x == 2:
                        ran_list.append(4)

                    ##add wall
                    ran = random.choice(ran_list)
                    if ran == 1:
                        Board[x][y+1] = kabe
                    elif ran == 2:
                        Board[x+1][y] = kabe
                    elif ran == 3:
                        Board[x][y-1] = kabe
                    elif ran == 4:
                        Board[x-1][y] = kabe

    Board[Goal_pos[0]][Goal_pos[1]] = Goal_img

    pygame.init()
    if getattr(sys, "frozen", False):
        main_path = os.path.dirname(sys.executable)
    else:
        main_path = os.path.dirname(os.path.realpath(__file__))

    oneway = os.path.join(main_path, "img/oneway.png")
    l_oneway = os.path.join(main_path, "img/l_oneway.png")
    r_oneway = os.path.join(main_path, "img/r_oneway.png")
    two_oneway = os.path.join(main_path, "img/two_oneway.png")
    oneway_l = os.path.join(main_path, "img/oneway_l.png")
    r_oneway_l = os.path.join(main_path, "img/r_oneway_l.png")
    oneway_r = os.path.join(main_path, "img/oneway_r.png")
    l_oneway_r = os.path.join(main_path, "img/l_oneway_r.png")
    wall = os.path.join(main_path, "img/wall.png")
    r_wall = os.path.join(main_path, "img/r_wall.png")
    l_wall = os.path.join(main_path, "img/l_wall.png")
    two_wall = os.path.join(main_path, "img/two_wall.png")
    twoway = os.path.join(main_path, "img/twoway.png")
    goal = os.path.join(main_path, "img/goal.png")
    p_dir =  os.path.join(main_path, "img/p_dir.png")

    img_oneway = pygame.image.load(oneway)
    img_l_oneway = pygame.image.load(l_oneway)
    img_r_oneway = pygame.image.load(r_oneway)
    img_two_oneway = pygame.image.load(two_oneway)
    img_oneway_l = pygame.image.load(oneway_l)
    img_r_oneway_l = pygame.image.load(r_oneway_l)
    img_oneway_r = pygame.image.load(oneway_r)
    img_l_oneway_r = pygame.image.load(l_oneway_r)
    img_wall = pygame.image.load(wall)
    img_r_wall = pygame.image.load(r_wall)
    img_l_wall = pygame.image.load(l_wall)
    img_two_wall = pygame.image.load(two_wall)
    img_twoway = pygame.image.load(twoway)
    img_goal = pygame.image.load(goal)
    img_dir = pygame.image.load(p_dir)

    X = img_oneway.get_width()
    Y = img_oneway.get_height()

    SCREEN_SIZE = [X,Y]
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("M E I R O")
    clock = pygame.time.Clock()

    t = pygame.font.SysFont(None, 70)
    t_E = t.render("E",True,(255,0,0))
    t_S = t.render("S",True,(255,0,0))
    t_W = t.render("W",True,(255,0,0))
    t_N = t.render("N",True,(255,0,0))

    cheat = False

    while True:
        ##key
        key = False
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                key = True

                if event.key == K_LEFT:
                    Player_dir -= 1
                elif event.key == K_RIGHT:
                    Player_dir += 1
                ##move char    
                elif event.key == K_UP:
                    if front == True:
                        Board[Player_pos[0]][Player_pos[1]] = miti
                        if Player_dir == 1:
                            Player_pos = [Player_pos[0],Player_pos[1]+1]
                        elif Player_dir == 2:
                            Player_pos = [Player_pos[0]+1,Player_pos[1]]
                        elif Player_dir == 3:
                            Player_pos = [Player_pos[0],Player_pos[1]-1]
                        elif Player_dir == 4:
                            Player_pos = [Player_pos[0]-1,Player_pos[1]]
                    else:
                        print("wall,cannot move")
                    Board[Player_pos[0]][Player_pos[1]] = Player_img
                elif event.key == K_SPACE:
                    if cheat == False:
                        cheat = True
                        for x in Board:
                            strings = ""
                            for y in x:
                                strings += y
                            print(strings)
                    

        if Player_dir == 5:
            Player_dir = 1
        if Player_dir == 0:
            Player_dir = 4

        x = Player_pos[1]
        y = Player_pos[0]

        if goal is True:
            if x == Goal_pos[1] and y == Goal_pos[0]:
                return

        front_right = False
        front_left = False
        front = False
        right = False
        left = False
        goal = False    

        ##serch front##[y][x]
        if Player_dir == 1:#right
            if Board[y+1][x+1] != kabe:
                front_right = True
            if Board[y][x+1] != kabe:
                front = True
                if  Board[y][x+1] == Goal_img:
                    goal = True
            if Board[y-1][x+1] != kabe:
                front_left = True
            if Board[y+1][x] != kabe:
                right = True
            if Board[y-1][x] != kabe:
                left = True

        elif Player_dir == 2:#down
            if Board[y+1][x-1] != kabe:
                front_right = True
            if Board[y+1][x] != kabe:
                front = True
                if Board[y+1][x] == Goal_img:
                    goal = True
            if Board[y+1][x+1] != kabe:
                front_left = True
            if Board[y][x-1] != kabe:
                right = True
            if Board[y][x+1] != kabe:
                left = True

        elif Player_dir == 3:#left
            if Board[y-1][x-1] != kabe:
                front_right = True
            if Board[y][x-1] != kabe:
                front = True
                if Board[y][x-1] == Goal_img:
                    goal = True
            if Board[y+1][x-1] != kabe:
                front_left = True
            if Board[y-1][x] != kabe:
                right = True
            if Board[y+1][x] != kabe:
                left = True

        elif Player_dir == 4:#up
            if Board[y-1][x+1] != kabe:
                front_right = True
            if Board[y-1][x] != kabe:
                front = True
                if Board[y-1][x] == Goal_img:
                    goal = True
            if Board[y-1][x-1] != kabe:
                front_left = True
            if Board[y][x+1] != kabe:
                right = True
            if Board[y][x-1] != kabe:
                left = True

        ##judge Wall, choice draw image
        if front and front_right and front_left:
            screen.blit(img_twoway, (0,0))

        elif front and front_right:
            if left:
                screen.blit(img_l_oneway_r, (0,0))
            else:
                screen.blit(img_oneway_r, (0,0))

        elif front and front_left:
            if right:
                screen.blit(img_r_oneway_l, (0,0))
            else:
                screen.blit(img_oneway_l, (0,0))

        elif front:
            if left and right:
                screen.blit(img_two_oneway, (0,0))
            elif right:
                screen.blit(img_r_oneway, (0,0))
            elif left:
                screen.blit(img_l_oneway, (0,0))
            else:
                screen.blit(img_oneway, (0,0))

        else:
            if left == True and right == True:
                screen.blit(img_two_wall, (0,0))
            elif right == True:
                screen.blit(img_r_wall, (0,0))
            elif left == True:
                screen.blit(img_l_wall, (0,0))
            else:
                screen.blit(img_wall, (0,0))

        if goal == True:
            screen.blit(img_goal, (0,0))


        if Player_dir == 1:
            screen.blit(t_E, (X-50,10))
        elif Player_dir == 2:
            screen.blit(t_S, (X-50,10))
        elif Player_dir == 3:
            screen.blit(t_W, (X-50,10))
        elif Player_dir == 4:
            screen.blit(t_N, (X-50,10))

        pygame.display.update()

        ##debug
        if dev == True:
            if key == True:
                print("\n")
                for x in Board:
                    strings = ""
                    for y in x:
                        strings += y
                    print(strings)   
                print(Player_dir,left,right,Player_pos)

    
