import pygame
from pygame.locals import *
import random
import option, town
import keyboard

class map1:
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 670
    

def play(screen, health, mana, level, exp, h_count, m_count, player, meso):
    pygame.init()

    W, H = 1024, 670  # screen size
    HW, HH = W / 2, H / 2  # half

    CLOCK = pygame.time.Clock()
    FPS = 1000

    bg = pygame.image.load("./image/img/map1.jpg").convert_alpha()
    bg = pygame.transform.scale(bg, (1024, 590))
    bgWidth, bgHeight = bg.get_rect().size  # bg 가로 세로길이

    stageWidth = bgWidth  # 삽입된 이미지의 좌표
    stagePosX = 0

    startScrollingPosX = HW  # 640 #이미지 이동 기준

    ## 비교좌표
    circleRadius = 1020
    circlePosX = circleRadius
    ##플레이어좌표
    playerPosX = 1020
    playerPosY = 325
    tempPosY = 0
    jump = 0
    climb = 0
    playerVelocityX = 0  # 속도
    playerVelocityY = 0  # y축 속도

    xCount = 0
    zCount = 0
    cCount = 0
    stand = 2
    walkCount = 0
    cake1Count = 0
    uCount = 0



    cake1_1Count = 0
    cake1_2Count = 0
    cake1_3Count = 0
    cake1_4Count = 0
    cake1_5Count = 0
    cake2Count = 0
    cake2_2Count = 0

    skill = pygame.image.load('./image/attack/moo.png').convert_alpha()

    ##스킬
    skillPosX = 0
    skillPosY = 0

    cake1_1 = pygame.image.load('./image/map1/cakemove0.png').convert_alpha()
    cake1_2 = pygame.image.load('./image/map1/cakemove0.png').convert_alpha()
    cake1_3 = pygame.image.load('./image/map1/cakemove0.png').convert_alpha()
    cake1_4 = pygame.image.load('./image/map1/cakemove0.png').convert_alpha()
    cake1_5 = pygame.image.load('./image/map1/cakemove0.png').convert_alpha()

    cake2 = pygame.image.load('./image/map1/cake2move0.png').convert_alpha()
    cake2_2 = pygame.image.load('./image/map1/cake2move0.png').convert_alpha()

    level10 = pygame.image.load('./image/level10.png').convert_alpha()
    font = pygame.font.Font("./font/a아시아고딕B.ttf", 15)
    name = pygame.image.load('./image/name.png')


    def skyland(screen, x, y, integer):
        # 띄워져있 있는 땅
        # integer가 1이면 사다리 2이면 줄

        skyland_left = pygame.image.load('./image/img/skyland_left.png')
        screen.blit(skyland_left, (x - 50, y - 5))

        skyland_right = pygame.image.load('./image/img/skyland_left.png')
        screen.blit(skyland_right, (x + 50, y - 5))

        skyland = pygame.image.load('./image/img/land1.png')
        screen.blit(skyland, (x, y))

        skyland_down = pygame.image.load('./image/img/skyland_down.png')
        screen.blit(skyland_down, (x - 30, y + 25))
        screen.blit(skyland_down, (x + 15, y + 25))

        skyland_ladder = pygame.image.load('./image/img/ladder.png')
        # 사다리 넘커서 크기조절
        skyland_ladder = pygame.transform.scale(skyland_ladder, (250, 400))

        skyland_line = pygame.image.load('./image/img/line.png')
        skyland_line = pygame.transform.scale(skyland_line, (200, 300))

        if integer == 1:
            screen.blit(skyland_ladder, (x - 100, y - 100))
        elif integer == 2:
            screen.blit(skyland_line, (x - 50, y - 89))

    def land(screen):
        # 땅 만들기
        y = 620
        for i in range(0, 13):
            land = pygame.image.load('./image/img/land.png')
            screen.blit(land, (i * 80, y - 90))
            land1 = pygame.image.load('./image/img/land1.png')
            screen.blit(land1, (i * 80, y - 112))

    x = 30
    x1 = random.randrange(100,900)
    x2 = random.randrange(100,900)
    x3 = random.randrange(100,900)
    x4 = random.randrange(100,900)
    x5 = random.randrange(100,900)

    x1_1 = random.randrange(220,300)
    x2_1 = random.randrange(520,600)

    x1count = 0
    x2count = 0
    x3count = 0
    x4count = 0
    x5count = 0
    x1_1count = 0
    x2_1count = 0

    y = 325
    y_1 = 65
    y_2 = 165

    skill_x = skill_c = 0

    x1_speed = 1
    x2_speed = 1
    x3_speed = 1
    x4_speed = 1
    x5_speed = 1

    x1_1_speed = 1
    x2_1_speed = 1

    y_speed = 0.3

    running = True

    while running:
        screen.blit(bg, (0, 0))
        option.play(screen, health, mana, level, exp, h_count, m_count, meso)  # option은 town map1 map2용
        k = pygame.key.get_pressed()

        skill_x = skill_c = 0

        ##############################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 종료시 입력시
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):  # ESE 누르면 종료
                    pygame.quit()
            #####HP/MP충전########
            if keyboard.is_pressed('s'):
                if h_count > 0 and health < 150:
                    h_count -= 1
                    health = 150
            elif keyboard.is_pressed('d'):
                if m_count > 0 and mana <150:
                    m_count -= 1
                    mana = 150
            elif k[K_h]:
                town.play(screen, health, mana, level, exp, h_count, m_count, player,meso)
            #####창전환###########
            if keyboard.is_pressed('F12'):  # 화면 키우기
                screen = pygame.display.set_mode((1024, 670),
                                                 pygame.FULLSCREEN | HWSURFACE | DOUBLEBUF)  # 해상도 480*320, 전체화면모드, 하드웨어 가속사용, 더블버퍼모드
            if keyboard.is_pressed('F11'):  # 윈도우 모드
                screen = pygame.display.set_mode((1024, 670), DOUBLEBUF)  # 해상도 480*320, 윈도우모드, 더블버퍼모드
            ######################
        #############################################################

        if k[K_LEFT]:
            climb = 0
            stand = 1
            playerVelocityX = -5
            if walkCount == 2:
                player = pygame.image.load('./image/player/walkleft0.png').convert_alpha()
            elif walkCount == 4:
                player = pygame.image.load('./image/player/walkleft1.png').convert_alpha()
            elif walkCount == 6:
                player = pygame.image.load('./image/player/walkleft2.png').convert_alpha()
            elif walkCount == 0:
                player = pygame.image.load('./image/player/walkleft3.png').convert_alpha()

        elif k[K_RIGHT]:
            climb = 0
            stand = 2
            playerVelocityX = 5
            if walkCount == 2:
                player = pygame.image.load('./image/player/walkright0.png').convert_alpha()
            elif walkCount == 4:
                player = pygame.image.load('./image/player/walkright1.png').convert_alpha()
            elif walkCount == 6:
                player = pygame.image.load('./image/player/walkright2.png').convert_alpha()
            elif walkCount == 0:
                player = pygame.image.load('./image/player/walkright3.png').convert_alpha()

        elif k[K_SPACE]:  # 점프
            # if health >= 0:
            #     health -= 10
            climb = 0
            if jump == 0:
                tempPosY = playerPosY
                playerVelocityY = 20
            jump = 1

        elif k[K_UP] or k[K_DOWN]:
            if 230 < circlePosX < 280:
                if playerPosY < 70: playerPosY += 5
                elif playerPosY > 320: playerPosY -=5
            if 230 < circlePosX < 280 and 70 <= playerPosY <= 320:
                climb = 1
                if k[K_DOWN]:
                    playerPosY += 5
                else:
                    playerPosY -= 5
                if uCount == 2:
                    player = pygame.image.load('./image/player/down0.png').convert_alpha()
                elif uCount == 0:
                    player = pygame.image.load('./image/player/down1.png').convert_alpha()
                #if playerPosY < 70:
                #    player = pygame.image.load('./image/player/standright.png').convert_alpha()
                    # playerVelocityY = 0  # 일정 높이 지나면 멈추게 했는데... 안내려감
            if 570 < circlePosX < 600:
                if playerPosY < 170: playerPosY += 5
                elif playerPosY > 320: playerPosY -=5
            if 570 < circlePosX < 600 and 170 <= playerPosY <= 320:
                climb = 1
                if k[K_DOWN]:
                    playerPosY += 5
                else:
                    playerPosY -= 5
                if uCount == 2:
                    player = pygame.image.load('./image/player/up0.png').convert_alpha()
                elif uCount == 0:
                    player = pygame.image.load('./image/player/up1.png').convert_alpha()

        elif k[K_z]:  # 기본공격
            if stand == 1:
                if zCount == 4:
                    player = pygame.image.load('./image/player/swingleft0.png').convert_alpha()
                elif zCount == 8:
                    player = pygame.image.load('./image/player/swingleft1.png').convert_alpha()
                elif zCount == 0:
                    player = pygame.image.load('./image/player/swingleft2.png').convert_alpha()
            else:
                if zCount == 4:
                    player = pygame.image.load('./image/player/swingright0.png').convert_alpha()
                elif zCount == 8:
                    player = pygame.image.load('./image/player/swingright1.png').convert_alpha()
                elif zCount == 0:
                    player = pygame.image.load('./image/player/swingright2.png').convert_alpha()

        elif k[K_x]and mana >= 1:
            mana -= 1
            skill_x = 1
            if stand == 1:
                skillPosX = circlePosX - 250
                skillPosY = playerPosY
                if xCount == 2:
                    skill = pygame.image.load('./image/attack/lfinalBlow0.png').convert_alpha()
                elif xCount == 3:
                    skill = pygame.image.load('./image/attack/lfinalBlow1.png').convert_alpha()
                elif xCount == 4:
                    skill = pygame.image.load('./image/attack/lfinalBlow2.png').convert_alpha()
                elif xCount == 5:
                    skill = pygame.image.load('./image/attack/lfinalBlow3.png').convert_alpha()
                elif xCount == 6:
                    skill = pygame.image.load('./image/attack/lfinalBlow4.png').convert_alpha()
                elif xCount == 7:
                    skill = pygame.image.load('./image/attack/lfinalBlow5.png').convert_alpha()
                elif xCount == 8:
                    skill = pygame.image.load('./image/attack/lfinalBlow6.png').convert_alpha()
                elif xCount == 9:
                    skill = pygame.image.load('./image/attack/lfinalBlow7.png').convert_alpha()
                elif xCount == 10:
                    skill = pygame.image.load('./image/attack/lfinalBlow8.png').convert_alpha()
                elif xCount == 0:
                    skill = pygame.image.load('./image/attack/lfinalBlow9.png').convert_alpha()
            if stand ==2:
                skillPosX = circlePosX
                skillPosY = playerPosY
                if xCount == 2:
                    skill = pygame.image.load('./image/attack/rfinalBlow0.png').convert_alpha()
                elif xCount == 3:
                    skill = pygame.image.load('./image/attack/rfinalBlow1.png').convert_alpha()
                elif xCount == 4:
                    skill = pygame.image.load('./image/attack/rfinalBlow2.png').convert_alpha()
                elif xCount == 5:
                    skill = pygame.image.load('./image/attack/rfinalBlow3.png').convert_alpha()
                elif xCount == 6:
                    skill = pygame.image.load('./image/attack/rfinalBlow4.png').convert_alpha()
                elif xCount == 7:
                    skill = pygame.image.load('./image/attack/rfinalBlow5.png').convert_alpha()
                elif xCount == 8:
                    skill = pygame.image.load('./image/attack/rfinalBlow6.png').convert_alpha()
                elif xCount == 9:
                    skill = pygame.image.load('./image/attack/rfinalBlow7.png').convert_alpha()
                elif xCount == 10:
                    skill = pygame.image.load('./image/attack/rfinalBlow8.png').convert_alpha()
                elif xCount == 0:
                    skill = pygame.image.load('./image/attack/rfinalBlow9.png').convert_alpha()

        elif circlePosX < 200 and playerPosY < 200:
            playerPosY = 320
            playerVelocityY = 0
            playerVelocityX = 0
        elif 350 < circlePosX < 480 and playerPosY < 200:
            playerPosY = 320
            playerVelocityY = 0
            playerVelocityX = 0
        elif 650 < circlePosX and playerPosY < 200:
            playerPosY = 320
            playerVelocityY = 0
            playerVelocityX = 0
# #-------------------------------사다리타다가 떨어지기--------------------
#         elif 230>circlePosX and 70<playerPosY<320:
#             playerPosY = 320
#             playerVelocityY = 0
#             playerVelocityX = 0
#         elif 280<circlePosX<340 and 70<playerPosY<320:
#             playerPosY = 320
#             playerVelocityY = 0
#             playerVelocityX = 0
#         elif 600<circlePosX and 170<playerPosY<320:
#             playerPosY = 320
#             playerVelocityY = 0
#             playerVelocityX = 0
#         elif 500<circlePosX<570 and 170<playerPosY<320:
#             playerPosY = 320
#             playerVelocityY = 0
#             playerVelocityX = 0
#
# #----------------------------------------------------------------------
        elif k[K_c]and mana >= 1:
            skill_c = 1
            if stand == 1:
                mana-=1
                skillPosX = circlePosX - 200
                skillPosY = playerPosY + 120
            else:
                mana-=1
                skillPosX = circlePosX + 85
                skillPosY = playerPosY + 120

            if cCount == 2:
                skill = pygame.image.load('./image/attack/loverSwingDouble0.png').convert_alpha()
            elif cCount == 3:
                skill = pygame.image.load('./image/attack/loverSwingDouble1.png').convert_alpha()
            elif cCount == 4:
                skill = pygame.image.load('./image/attack/loverSwingDouble2.png').convert_alpha()
            elif cCount == 5:
                skill = pygame.image.load('./image/attack/loverSwingDouble3.png').convert_alpha()
            elif cCount == 6:
                skill = pygame.image.load('./image/attack/loverSwingDouble4.png').convert_alpha()
            elif cCount == 0:
                skill = pygame.image.load('./image/attack/loverSwingDouble5.png').convert_alpha()

        else:
            skill = pygame.image.load('./image/attack/moo.png').convert_alpha()
            playerVelocityX = 0
            # playerPosY = 320
            if stand == 1:  # 왼
                player = pygame.image.load('./image/player/standleft.png').convert_alpha()
            else:  # 2 오
                player = pygame.image.load('./image/player/standright.png').convert_alpha()
#--------공격받음----------------------------------------------------
        if x1-30 < circlePosX < x1+30 and 305< playerPosY <335 and health >= 1:
            health -= 1
        if x2-30 < circlePosX < x2+30 and 305< playerPosY <335 and health >= 1:
            health -= 1
        if x3-30 < circlePosX < x3+30 and 305< playerPosY <335 and health >= 1:
            health -= 1
        if x4-30 < circlePosX < x4+30 and 305< playerPosY <335 and health >= 1:
            health -= 1
        if x5-30 < circlePosX < x5+30 and 305< playerPosY <335 and health >= 1:
            health -= 1

        if x1_1-30 < circlePosX < x1_1+30 and 55< playerPosY <75 and health >= 1:
            health -= 1
        if x2_1-30 < circlePosX < x2_1+30 and 155< playerPosY <175 and health >= 1:
            health -= 1

        # ---------공격
        if skill_x == 1:
            if x1 - 120 < skillPosX < x1 + 120 and 310 < playerPosY < 335:
                x1count += 1
                cake1_1 = pygame.image.load('./image/map1/cakedie1.png').convert_alpha()
                # health += 10
            if x2 - 120 < skillPosX < x2 + 120 and 310 < playerPosY < 335:
                x2count += 1
                cake1_2 = pygame.image.load('./image/map1/cakedie1.png').convert_alpha()
            # health += 10
            if x3 - 120 < skillPosX < x3 + 120 and 310 < playerPosY < 335:
                x3count += 1
                cake1_3 = pygame.image.load('./image/map1/cakedie1.png').convert_alpha()
            #  health += 10
            if x4 - 120 < skillPosX < x4 + 120 and 310 < playerPosY < 335:
                x4count += 1
                cake1_4 = pygame.image.load('./image/map1/cakedie1.png').convert_alpha()
            # health += 10
            if x5 - 120 < skillPosX < x5 + 120 and 310 < playerPosY < 335:
                x5count += 1
                cake1_5 = pygame.image.load('./image/map1/cakedie1.png').convert_alpha()

            if x1_1 - 120 < skillPosX < x1_1 + 120 and 75 < playerPosY < 95:
                x1_1count += 1
                cake2 = pygame.image.load('./image/map1/cake2die1.png').convert_alpha()
            if x2_1 - 120 < skillPosX < x2_1 + 120 and 75 < playerPosY < 95:
                cake2_2 = pygame.image.load('./image/map1/cake2die1.png').convert_alpha()


        if skill_c == 1:
            if x1 - 120 < skillPosX < x1 + 120 and 310 < playerPosY < 330:
                x1count += 1
                cake1_1 = pygame.image.load('./image/map1/cakedie1.png').convert_alpha()
                # health += 10
            if x2 - 120 < skillPosX < x2 + 120 and 310 < playerPosY < 330:
                x2count += 1
                cake1_2 = pygame.image.load('./image/map1/cakedie1.png').convert_alpha()
            # health += 10
            if x3 - 120 < skillPosX < x3 + 120 and 310 < playerPosY < 330:
                x3count += 1
                cake1_3 = pygame.image.load('./image/map1/cakedie1.png').convert_alpha()
            #  health += 10
            if x4 - 120 < skillPosX < x4 + 120 and 310 < playerPosY < 330:
                x4count += 1
                cake1_4 = pygame.image.load('./image/map1/cakedie1.png').convert_alpha()
            # health += 10
            if x5 - 120 < skillPosX < x5 + 120 and 310 < playerPosY < 330:
                x5count += 1
                cake1_5 = pygame.image.load('./image/map1/cakedie1.png').convert_alpha()

            if x1_1 - 120 < skillPosX < x1_1 + 120 and 75 < playerPosY < 95:
                x1_1count += 1
                cake2 = pygame.image.load('./image/map1/cake2die1.png').convert_alpha()

            if x2_1 - 120 < skillPosX < x2_1 + 120 and 75 < playerPosY < 95:
                x2_1count += 1
                cake2_2 = pygame.image.load('./image/map1/cake2die1.png').convert_alpha()


#-------------------------------cake--------------------------
        if cake1Count == 2:
            cake1_1 = pygame.image.load('./image/map1/cakemove0.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove0.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove0.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove0.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove0.png').convert_alpha()
        elif cake1Count == 4:
            cake1_1 = pygame.image.load('./image/map1/cakemove1.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove1.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove1.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove1.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove1.png').convert_alpha()
        elif cake1Count == 6:
            cake1_1 = pygame.image.load('./image/map1/cakemove2.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove2.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove2.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove2.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove2.png').convert_alpha()
        elif cake1Count == 8:
            cake1_1 = pygame.image.load('./image/map1/cakemove3.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove3.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove3.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove3.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove3.png').convert_alpha()
        elif cake1Count == 10:
            cake1_1 = pygame.image.load('./image/map1/cakemove4.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove4.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove4.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove4.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove4.png').convert_alpha()
        elif cake1Count == 12:
            cake1_1 = pygame.image.load('./image/map1/cakemove4.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove4.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove4.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove4.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove4.png').convert_alpha()
        elif cake1Count == 14:
            cake1_1 = pygame.image.load('./image/map1/cakemove6.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove6.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove6.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove6.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove6.png').convert_alpha()
        elif cake1Count == 16:
            cake1_1 = pygame.image.load('./image/map1/cakemove7.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove7.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove7.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove7.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove7.png').convert_alpha()
        elif cake1Count == 18:
            cake1_1 = pygame.image.load('./image/map1/cakemove8.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove8.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove8.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove8.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove8.png').convert_alpha()
        elif cake1Count == 20:
            cake1_1 = pygame.image.load('./image/map1/cakemove9.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove9.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove9.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove9.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove9.png').convert_alpha()
        elif cake1Count == 22:
            cake1_1 = pygame.image.load('./image/map1/cakemove10.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove10.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove10.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove10.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove10.png').convert_alpha()
        elif cake1Count == 24:
            cake1_1 = pygame.image.load('./image/map1/cakemove11.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove11.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove11.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove11.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove11.png').convert_alpha()
        elif cake1Count == 0:
            cake1_1 = pygame.image.load('./image/map1/cakemove12.png').convert_alpha()
            cake1_2 = pygame.image.load('./image/map1/cakemove12.png').convert_alpha()
            cake1_3 = pygame.image.load('./image/map1/cakemove12.png').convert_alpha()
            cake1_4 = pygame.image.load('./image/map1/cakemove12.png').convert_alpha()
            cake1_5 = pygame.image.load('./image/map1/cakemove12.png').convert_alpha()

        if cake1Count == 2:
            cake2 = pygame.image.load('./image/map1/cake2move0.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move0.png').convert_alpha()
        elif cake1Count == 4:
            cake2 = pygame.image.load('./image/map1/cake2move1.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move1.png').convert_alpha()
        elif cake1Count == 6:
            cake2 = pygame.image.load('./image/map1/cake2move2.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move2.png').convert_alpha()
        elif cake1Count == 8:
            cake2 = pygame.image.load('./image/map1/cake2move3.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move3.png').convert_alpha()
        elif cake1Count == 10:
            cake2 = pygame.image.load('./image/map1/cake2move4.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move4.png').convert_alpha()
        elif cake1Count == 12:
            cake2 = pygame.image.load('./image/map1/cake2move5.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move5.png').convert_alpha()
        elif cake1Count == 14:
            cake2 = pygame.image.load('./image/map1/cake2move6.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move6.png').convert_alpha()
        elif cake1Count == 16:
            cake2 = pygame.image.load('./image/map1/cake2move7.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move7.png').convert_alpha()
        elif cake1Count == 18:
            cake2 = pygame.image.load('./image/map1/cake2move8.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move8.png').convert_alpha()
        elif cake1Count == 20:
            cake2 = pygame.image.load('./image/map1/cake2move9.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move9.png').convert_alpha()
        elif cake1Count == 22:
            cake2 = pygame.image.load('./image/map1/cake2move10.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move10.png').convert_alpha()
        elif cake1Count == 24:
            cake2 = pygame.image.load('./image/map1/cake2move11.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move11.png').convert_alpha()
        elif cake1Count == 0:
            cake2 = pygame.image.load('./image/map1/cake2move12.png').convert_alpha()
            cake2_2 = pygame.image.load('./image/map1/cake2move12.png').convert_alpha()
#---------------------------------------------------
        playerPosX += playerVelocityX  # 가는만큼 더해줌
        walkCount += 1
        zCount += 1
        xCount += 1
        cCount += 1
        uCount += 1
        cake1Count += 1

        # 이미지 초기화
        if walkCount == 6:
            walkCount = 0
        if zCount == 10:
            zCount = 0
        if xCount == 12:
            xCount = 0
        if cCount == 7:
            cCount = 0
        if uCount == 3:
            uCount = 0
        if cake1Count == 26:
            cake1Count = 0

        # 화면 오른쪽 끝
        if playerPosX > stageWidth - 60: playerPosX = stageWidth - 60
        # 화면 왼쪽 끝
        if playerPosX < 5: playerPosX = 5

        #######이동관련좌표
        if playerPosX < startScrollingPosX:
            circlePosX = playerPosX
        elif playerPosX > stageWidth - startScrollingPosX:
            circlePosX = playerPosX - stageWidth + W
        else:
            circlePosX = startScrollingPosX
            stagePosX += -playerVelocityX

        if jump == 1:
            playerPosY -= playerVelocityY
            playerVelocityY -= 4
            if playerVelocityY == -24:
                jump = 0
                playerPosy = tempPosY
            if stand == 1:
                player = pygame.image.load('./image/player/jumpleft.png')
            else:
                player = pygame.image.load('./image/player/jumpright.png')

        if climb == 1:
            player = pygame.image.load('./image/player/down1.png').convert_alpha()

        if health <= 0:
            player = pygame.image.load('./image/player/dead.png').convert_alpha()
            if keyboard.is_pressed('h'):
                town.play(screen, health, mana, level, exp, h_count, m_count, player,meso)

        rel_x = stagePosX % bgWidth
        screen.blit(bg, (rel_x - bgWidth, 0))
        if rel_x < W:
            screen.blit(bg, (rel_x, 0))

        # screen.blit(player, (circlePosX, playerPosY))
        screen.blit(skill, (skillPosX, skillPosY))

        # ----------------메소 떨굼--
        if x1count >= 30:
            x1count = -1
            cake1_1 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            # y = 5000
            x1 = 5000
            meso += 10
            level += 1
        if x2count >= 30:
            x2count = -1
            cake1_2 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            # y = 5000
            x2 = 5000
            meso += 10
            level += 1

        if x3count >= 30:
            x3count = -1
            cake1_3 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            # y = 5000
            x3 = 5000
            meso += 10
            level += 1
        if x4count >= 30:
            x4count = -1
            cake1_4 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            # y = 5000
            x4 = 5000
            meso += 10
            level += 1
        if x5count >= 30:
            x5count = -1
            cake1_5 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            # y = 5000
            x5 = 5000
            meso += 10
            level += 1
        if x1_1count >= 30:
            x1_1count = -1
            cake2 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            # y_2 = 5000
            x2_1 = 5000
            meso += 10
            level += 1
        if x2_1count >= 30:
            x2_1count = -1
            cake2_2 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            # y_2 = 5000
            x2_1 = 5000
            meso += 10
            level += 1

        if 10 <=level<= 11:
            screen.blit(level10, (350, 80))



        #######################

        x1 = x1 + x1_speed
        if x1 > 920 or x1 < 0:
            x1_speed = -x1_speed  # 움직임 부호를 바꿔준다.

        x2 = x2 + x2_speed
        if x2 > 920 or x2 < 0:
            x2_speed = -x2_speed  # 움직임 부호를 바꿔준다.

        x3 = x3 - x3_speed
        if x3 > 920 or x3 < 0:
            x3_speed = -x3_speed  # 움직임 부호를 바꿔준다.

        x4 = x4 - x4_speed
        if x4 > 920 or x4 < 0:
            x4_speed = -x4_speed  # 움직임 부호를 바꿔준다.

        x5 = x5 + x5_speed
        if x5 > 920 or x5 < 0:
            x5_speed = -x5_speed  # 움직임 부호를 바꿔준다.

        x1_1 = x1_1 + x1_1_speed
        if x1_1 > 320 or x1_1 < 200:
            x1_1_speed = -x1_1_speed  # 움직임 부호를 바꿔준다.

        x2_1 = x2_1 + x2_1_speed
        if x2_1 > 630 or x2_1 < 500:
            x2_1_speed = -x2_1_speed  # 움직임 부호를 바꿔준다.

        # ---------------------------------------------------------------------
        # DS.blit(my_ball, [x, y])  # 새로운 위치에 그림출력
        screen.blit(cake1_1, [x1, y])
        screen.blit(cake1_2, [x2, y])
        screen.blit(cake1_3, [x3, y])
        screen.blit(cake1_4, [x4, y])
        screen.blit(cake1_5, [x5, y])
        screen.blit(cake2, [x1_1, y_1])
        screen.blit(cake2_2, [x2_1, y_2])
        screen.blit(skill, (skillPosX, skillPosY))

        land(screen)
        skyland(screen, 300, 250, 1)
        skyland(screen, 600, 350, 2)
        screen.blit(player, (circlePosX, playerPosY))
        screen.blit(name, (circlePosX+10,playerPosY+193))

        pygame.display.update()
        CLOCK.tick(FPS)

if __name__ == "__main__":
    play(screen)