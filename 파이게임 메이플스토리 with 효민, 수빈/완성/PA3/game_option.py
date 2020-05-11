import pygame #pyamge 모듈 import
from pygame.locals import * #pygame.locals 하위 모듈 import
import option
import keyboard
import main, music

def play(screen):
    pygame.init()  # 초기화 하지 않을 경우, 일부 기능 정상 동작하지 않을수도 있음
    start_background = pygame.image.load("./image/start/start_back.png")
    start_background = pygame.transform.scale(start_background, (1024, 670))
    background = start_background

    font = pygame.font.SysFont("comicsansms", 70)
    font2 = pygame.font.SysFont("comicsansms", 30)
    on_button = font.render("ON ", True, (0,0,0))
    on_rect = on_button.get_rect(x=200, y=300)
    off_button = font.render("OFF ", True, (0,0,0))
    off_rect = off_button.get_rect(x=500, y=300)
    back_button = font2.render(" BACK ", True, (225, 225, 225), (0, 0, 0))
    back_rect = back_button.get_rect(x=370, y=450)

    running = True

    while running:
        screen.blit(background, (0, 0))
        screen.blit(on_button, on_rect)
        screen.blit(off_button, off_rect)
        screen.blit(back_button, back_rect)
        for event in pygame.event.get():
            if on_rect.collidepoint(pygame.mouse.get_pos()):  ##start에 마우스가 올려져 있을 때
                if event.type == MOUSEBUTTONDOWN:  # 마우스를 클릭하면
                    music.play(0.3)
            if off_rect.collidepoint(pygame.mouse.get_pos()):  ##start에 마우스가 올려져 있을 때
                if event.type == MOUSEBUTTONDOWN:  # 마우스를 클릭하면
                    music.play(0)
            if back_rect.collidepoint(pygame.mouse.get_pos()):  ##start에 마우스가 올려져 있을 때
                if event.type == MOUSEBUTTONDOWN:  # 마우스를 클릭하면
                    main.play(screen) #메인으로 (이전화면으로)
            if event.type == pygame.QUIT:  # 종료 입력시
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):  # ESE 누르면 종료
                    pygame.quit()
            #####창전환###########
            if keyboard.is_pressed('F12'):  # 화면 키우기
                screen = pygame.display.set_mode((1024, 670),
                                                 pygame.FULLSCREEN | HWSURFACE | DOUBLEBUF)  # 해상도 480*320, 전체화면모드, 하드웨어 가속사용, 더블버퍼모드
            if keyboard.is_pressed('F11'):  # 윈도우 모드
                screen = pygame.display.set_mode((1024, 670), DOUBLEBUF)  # 해상도 480*320, 윈도우모드, 더블버퍼모드
            ######################
        pygame.display.update()  # 화면 업데이트

    pygame.quit()

if __name__ == "__main__":
    play()