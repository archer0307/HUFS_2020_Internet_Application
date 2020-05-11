import pygame #pyamge 모듈 import
from pygame import *
from pygame.locals import * #pygame.locals 하위 모듈 import
import keyboard #keyboard 모듈 improt
import random #ramdom 모듈 import
import town, how, game_option, music, user, map1, map2

music.play(0.3)
player = user.USER()
screen = pygame.display.set_mode((1024, 670), pygame.DOUBLEBUF) #해상도 480*320, 윈도우모드, 더블버퍼모드
pygame.display.set_caption('SuSoMingStory') #타이틀바의 텍스트


def play(screen):
    pygame.init() #초기화 하지 않을 경우, 일부 기능 정상 동작하지 않을수도 있음

    ########배경##########
    start_background = pygame.image.load("./image/start/start_back.png")
    start_background = pygame.transform.scale(start_background, (1024, 670))
    background = start_background

    pygame.display.update()
    #pygame.display.flip() #화면에 모든 내용 업데이트

    ##########################
    health = 150
    mana = 150
    level = 1
    exp = 0
    h_count = 2
    m_count = 2
    meso = 500
    ##########################

    #####START_TEXT###########
    font = pygame.font.Font("./font/Maplestory Bold.ttf", 150)
    font2 = pygame.font.Font("./font/Maplestory Light.ttf", 40)
    start_button = font.render("START", True, (255, 0, 0))
    start_rect = start_button.get_rect(x=265,y=270)
    how_button = font2.render("HOW", True, (0, 0, 0))
    how_rect = how_button.get_rect(x=260,y=450)
    option_button = font2.render("OPTION", True, (0, 0, 0))
    option_rect = option_button.get_rect(x=410,y=450)
    exit_button = font2.render("EXIT", True, (0, 0, 0))
    exit_rect = exit_button.get_rect(x=630,y=450)
    ##########################
    cursor = pygame.image.load("./image/normal.gif").convert()
    cursor.set_colorkey((0,255,0))
    #########################

    running=True #화ccccccccc면이 계속 켜져있게 해줌

    while running :
        target = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))
        screen.blit(start_button, start_rect)
        screen.blit(how_button, how_rect)
        screen.blit(option_button, option_rect)
        screen.blit(exit_button, exit_rect)
        screen.blit(cursor, target)

        
        for event in pygame.event.get():
            if start_rect.collidepoint(pygame.mouse.get_pos()): ##start에 마우스가 올려져 있을 때
                if event.type == MOUSEBUTTONDOWN: #마우스를 클릭하면
                    #map1.play(screen, health, mana, level, exp, h_count, m_count, player, meso)
                    town.play(screen, health, mana, level, exp, h_count, m_count, player, meso) #게임 시작!! town으로 이동
            elif how_rect.collidepoint(pygame.mouse.get_pos()): ##start에 마우스가 올려져 있을 때
                if event.type == MOUSEBUTTONDOWN: #마우스를 클릭하면
                    how.play(screen) #how로 시이동
            elif option_rect.collidepoint(pygame.mouse.get_pos()): ##start에 마우스가 올려져 있을 때
                if event.type == MOUSEBUTTONDOWN: #마우스를 클릭하면
                    game_option.play(screen) #koption으로 이동
            elif exit_rect.collidepoint(pygame.mouse.get_pos()): ##start에 마우스가 올려져 있을 때
                if event.type == MOUSEBUTTONDOWN: #마우스를 클릭하면
                    running = False #게임  종료!
            if event.type == pygame.QUIT:  # 종료시 입력시
                running = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE) :  #ESE 누르면 종료
                    running = False
            #####창전환###########

            if keyboard.is_pressed('F12'):  # 화면 키우기
                screen = pygame.display.set_mode((1024, 670),pygame.FULLSCREEN | pygame.HWSURFACE | DOUBLEBUF)  # 해상도 480*320, 전체화면모드, 하드웨어 가속사용, 더블버퍼모드
            if keyboard.is_pressed('F11'): # 윈도우 모드
                screen = pygame.display.set_mode((1024, 670), pygame.DOUBLEBUF)  # 해상도 480*320, 윈도우모드, 더블버퍼모드
            ######################


        pygame.display.update()#화면 업데이트

    pygame.quit()#파이게임 종료

if __name__ == "__main__":
    play(screen)
