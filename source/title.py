import game
import os
import sys
import time

import pygame
from pygame.locals import *

if getattr(sys, "frozen", False):
    main_path = os.path.dirname(sys.executable)
else:
    main_path = os.path.dirname(os.path.realpath(__file__))



def title():
    pygame.init()
    SCREEN_SIZE = [500,500]
    screen = pygame.display.set_mode(SCREEN_SIZE)

    pygame.display.set_caption("MEIRO")
    clock = pygame.time.Clock()

    if getattr(sys, 'frozen', False):
        main_path = os.path.dirname(sys.executable)
    else:
        main_path = os.path.dirname(os.path.realpath("__file__"))
    print(main_path)
        
    image_font = os.path.join(main_path,"img", "ipaexg.ttf")
    
    os.system("clear")
    endFlag = False
    
    font1 = pygame.font.SysFont(None, 140)
    title1 = font1.render("MEIRO",False, (0,0,0))
    title2 = font1.render("OOOOH",False, (0,0,0))
    font2 = pygame.font.SysFont(None, 50)
    p_text1 = font2.render("Start by press any",True, (0,0,0))
    p_text2 = font2.render("KeyBoard",True, (0,0,0))
    japfont = pygame.font.Font(image_font,15)
    jp_text1 = japfont.render("頑張って割と難しい迷路から脱出してみて", True, (0,0,0))
    jp_text2 = japfont.render("操作は、方向転換[左矢印][右矢印] 歩く[上矢印] です。", True, (0,0,0))
    jp_text3 = japfont.render("右上の英字はそれぞれ東[E]西[S]南[W]北[N]を表している", True, (0,0,0))
    jp_text4 = japfont.render("SPACEでターミナルに一回だけマップが映ります", True, (0,0,0))
    while endFlag == False:
        screen.fill((255,255,255))
        screen.blit(title1,(20,0))
        screen.blit(title2,(40,80))
        screen.blit(p_text1,(40,180))
        screen.blit(p_text2,(100,230))
        screen.blit(jp_text1,(20,300))
        screen.blit(jp_text2,(20,330))
        screen.blit(jp_text3,(20,360))
        screen.blit(jp_text4,(20,390))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                endFlag = True

    ##main script

def result(kekka):
    pygame.init()
    SCREEN_SIZE = [500,500]
    screen = pygame.display.set_mode(SCREEN_SIZE)

    pygame.display.set_caption("MEIRO")
    clock = pygame.time.Clock()

    if getattr(sys, "frozen", False):
        main_path = os.path.dirname(sys.executable)
    else:
        main_path = os.path.dirname(os.path.realpath(__file__))
    
    image_font = os.path.join(main_path, "img/ipaexg.ttf")
    
    endFlag = False
    font3 = pygame.font.Font(image_font, 120)
    result1 = font3.render("けっか",False, (0,0,0))

    font4 = pygame.font.SysFont(None, 70)
    result2 = font4.render("["+kekka+"]sec",False, (255,0,0))

    font2 = pygame.font.SysFont(None, 50)
    r_text1 = font2.render("Back to Title by press any",True, (0,0,0))
    r_text2 = font2.render("KeyBoard",True, (0,0,0))
    japfont = pygame.font.Font(image_font,15)
    jp_text1 = japfont.render("リトライする時は適当にボタン押してね", True, (0,0,0))
    jp_text2 = japfont.render("終了する時はウィンドウのバツボタンから。", True, (0,0,0))
    jp_text3 = japfont.render("またのご挑戦お待ちしております。", True, (0,0,0))
    while endFlag == False:
        screen.fill((255,255,255))
        screen.blit(result1,(20,0))
        screen.blit(result2,(70,180))
        screen.blit(r_text1,(40,250))
        screen.blit(r_text2,(100,300))
        screen.blit(jp_text1,(20,350))
        screen.blit(jp_text2,(20,380))
        screen.blit(jp_text3,(20,410))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                endFlag = True


if __name__ == "__main__":
    while True:
        print("開始します")
        title()
        time1 = time.time()
        game.main()
        time2 = time.time()
        el_time = time2 - time1
        el_time = str(round(el_time, 1))
        result(el_time)
        

        
