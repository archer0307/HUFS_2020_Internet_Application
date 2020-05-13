import pygame #pyamge 모듈 import
from pygame.locals import * #pygame.locals 하위 모듈 import
import sys, random,sys
import option, town, user
import keyboard


def play(screen, health, mana, level, exp, h_count, m_count, player, meso):
    pygame.init()
    #############
    W, H = 1024, 670  # screen size
    HW, HH = W / 2, H / 2  # half

    CLOCK = pygame.time.Clock()
    FPS = 1000


    bg = pygame.image.load("./image/img/cookiehouse.png").convert()
    bg = pygame.transform.scale(bg, (1024, 590))
    bgWidth, bgHeight = bg.get_rect().size  # bg 가로 세로길이

    stageWidth = bgWidth  # 삽입된 이미지의 좌표
    stagePosX = 0

    startScrollingPosX = HW  # 640 #이미지 이동 기준

    ## 비교좌표
    circleRadius = 25
    circlePosX = circleRadius
    ##플레이어좌표
    playerPosX = 30
    playerPosY = 320
    tempPosY = 0
    jump = 0
    climb = 0
    playerVelocityX = 0  # 속도
    playerVelocityY = 0  # y축 속도


    ##스킬
    skillPosX = 0
    skillPosY = 0

    cake1_1 = pygame.image.load('./image/map2/cokemove0.png').convert_alpha()
    cake1_2 = pygame.image.load('./image/map2/cokemove0.png').convert_alpha()
    cake1_3 = pygame.image.load('./image/map2/cokemove0.png').convert_alpha()
    cake1_4 = pygame.image.load('./image/map2/cokemove0.png').convert_alpha()
    cake1_5 = pygame.image.load('./image/map2/cokemove0.png').convert_alpha()

    cake2_1 = pygame.image.load('./image/map2/coke2move0.png').convert_alpha()
    cake2_2 = pygame.image.load('./image/map2/coke2move0.png').convert_alpha()
    cake2_3 = pygame.image.load('./image/map2/coke2move0.png').convert_alpha()

    level10 = pygame.image.load('./image/level10.png').convert_alpha()

    cake1_1Count = 0
    cake1_2Count = 0
    cake1_3Count = 0
    cake1_4Count = 0
    cake1_5Count = 0
    cake2_1Count = 0
    cake2_2Count = 0
    cake2_3Count = 0


    xCount = 0
    zCount = 0
    cCount = 0
    stand = 2
    walkCount = 0
    uCount = 0

    skill = pygame.image.load('./image/attack/moo.png').convert_alpha()
    font = pygame.font.Font("./font/a아시아고딕B.ttf", 15)
    name = pygame.image.load('./image/name.png')



    def skyland(screen,x,y):
        # 띄워져있 있는 땅
        # integer가 1이면 사다리 2이면 줄

        skyland_left = pygame.image.load('./image/img/block1.png').convert_alpha()
        screen.blit(skyland_left, (x-300, y-57))

        skyland_ladder = pygame.image.load('./image/img/ladder.png').convert_alpha()
        #사다리 넘커서 크기조절
        skyland_ladder = pygame.transform.scale(skyland_ladder, (250, 400))


        screen.blit(skyland_ladder, (x-240,y-130))

    def skyland2(screen,x,y):
        # 띄워져있 있는 땅

        skyland_left = pygame.image.load('./image/img/block2.png').convert_alpha()
        screen.blit(skyland_left, (x+330, y-10))

        skyland_line = pygame.image.load('./image/img/line.png').convert_alpha()
        skyland_line = pygame.transform.scale(skyland_line, (200, 300))

        screen.blit(skyland_line, (x+420,y-67))

    def land(screen):
        # 땅 만들기
        y=620
        for i in range(0, 2):
            land = pygame.image.load('./image/img/land22.png').convert_alpha()
            screen.blit(land, (i * 500, y-90))
        for i in range(0, 13):
            land1 = pygame.image.load('./image/img/land21.png').convert_alpha()
            screen.blit(land1, (i * 80, y-112))


    x = 30
    x1_2=random.randrange(10, 230)
    x2_2=random.randrange(1, 230)
    x3_2=random.randrange(700, 900)
    x1 = random.randrange(30, 900)
    x2 = random.randrange(30, 900)
    x3 = random.randrange(30, 900)
    x4 = random.randrange(30, 900)
    x5 = random.randrange(30, 900)

    #--xcount--
    x1count = 0
    x2count = 0
    x3count = 0
    x4count = 0
    x5count = 0
    x1_2count = 0
    x2_2count = 0
    x3_2count = 0
    levelcount = 0

    skill_x = 0
    skill_c = 0

    y = 322
    y_2=85
    y_3=138
    x1_2_speed=1
    x2_2_speed=1
    x3_2_speed=1
    x1_speed = 1
    x2_speed = 1
    x3_speed = 1
    x4_speed = 1
    x5_speed = 1

    running = True

    while running:
        screen.blit(bg, (0, 0))
        option.play(screen, health, mana, level, exp, h_count, m_count,meso)  # option은 town map1 map2용
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
            if keyboard.is_pressed('d') and mana <150:
                if m_count > 0:
                    m_count -= 1
                    mana = 150
            elif k[K_h]:
                town.play(screen, health, mana, level, exp, h_count, m_count, player, meso)
            #####창전환###########
            if keyboard.is_pressed('F12'):  # 화면 키우기
                screen = pygame.display.set_mode((1024, 670), pygame.FULLSCREEN | HWSURFACE | DOUBLEBUF)  # 해상도 480*320, 전체화면모드, 하드웨어 가속사용, 더블버퍼모드
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
            # 기본 위치 340?. 누르면 올라갔다가 다시 돌아옴
            # if health >= 0:
            #     health -= 10
            climb = 0
            if jump == 0:
                tempPosY = playerPosY
                playerVelocityY = 20
            jump = 1

        elif k[K_UP] or k[K_DOWN]:
            if 98 < circlePosX < 142:
                if playerPosY < 85: playerPosY += 5
                elif playerPosY > 320: playerPosY -=5
            if 98 < circlePosX < 142 and 85 <= playerPosY <= 320:
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
            if 725 < circlePosX < 760:
                if playerPosY < 140: playerPosY += 5
                elif playerPosY > 320: playerPosY -=5
            if 725 < circlePosX < 760 and 140 <= playerPosY <= 320:
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
            skill_x = 1
            if stand == 1:
                skillPosX = circlePosX - 250
                skillPosY = playerPosY
                mana -= 1
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
            else:
                skillPosX = circlePosX + 50
                skillPosY = playerPosY
                mana -= 1
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


        elif k[K_c]and mana >= 1:
            skill_c = 1
            if stand == 1:
                skillPosX = circlePosX - 200
                skillPosY = playerPosY + 120
                mana -= 1
            else:
                mana -= 1
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

        elif 340 < circlePosX < 680 and playerPosY < 200:
            playerPosY = 320
            playerVelocityY = 0
            playerVelocityX = 0


        else:
            skill = pygame.image.load('./image/attack/moo.png').convert_alpha()
            playerVelocityX = 0
            #playerPosY = 320
            if stand == 1:  # 왼
                player = pygame.image.load('./image/player/standleft.png').convert_alpha()
            else:  # 2 오
                player = pygame.image.load('./image/player/standright.png').convert_alpha()
#------------공격받음---------------------------------
        if x1-30 < circlePosX < x1+30 and 310< playerPosY <330 and health >= 1:
            health -= 1
        if x2-30 < circlePosX < x2+30 and 310< playerPosY <330 and health >= 1:
            health -= 1
        if x3-30 < circlePosX < x3+30 and 310< playerPosY <330 and health >= 1:
            health -= 1
        if x4-30 < circlePosX < x4+30 and 310< playerPosY <330 and health >= 1:
            health -= 1
        if x5-30 < circlePosX < x5+30 and 310< playerPosY <330 and health >= 1:
            health -= 1

        if x1_2-30 < circlePosX < x1_2+30 and 75< playerPosY <95 and health >= 1:
            health -= 1
        if x2_2-30 < circlePosX < x2_2+30 and 75< playerPosY <95 and health >= 1:
            health -= 1
        if x3_2-30 < circlePosX < x3_2+30 and 130< playerPosY <150 and health >= 1:
            health -= 1

#---------공격
        if skill_x == 1 :
            if x1 - 80 < skillPosX < x1 + 80 and 310 < playerPosY < 330 :
                x1count += 1
                cake1_1 = pygame.image.load('./image/map2/cokedie0.png').convert_alpha()

            if x2 - 80 < skillPosX < x2 + 80 and 310 < playerPosY < 330 :
                x2count += 1
                cake1_2 = pygame.image.load('./image/map2/cokedie0.png').convert_alpha()

            if x3 - 80 < skillPosX < x3 + 80 and 310 < playerPosY < 330 :
                x3count += 1
                cake1_3 = pygame.image.load('./image/map2/cokedie0.png').convert_alpha()

            if x4 - 80 < skillPosX < x4 + 80 and 310 < playerPosY < 330 :
                x4count += 1
                cake1_4 = pygame.image.load('./image/map2/cokedie0.png').convert_alpha()

            if x5 - 80 < skillPosX < x5 + 80 and 310 < playerPosY < 330:
                x5count += 1
                cake1_5 = pygame.image.load('./image/map2/cokedie0.png').convert_alpha()

            if x1_2 - 80 < skillPosX < x1_2 + 80 and 75 < playerPosY < 95 :
                x1_2count += 1
            if x2_2 - 80 < skillPosX < x2_2 + 80 and 75 < playerPosY < 95 :
                x2_2count += 1
            if x3_2 - 80 < skillPosX < x3_2 + 80 and 130 < playerPosY < 150 :
                x3_2count += 1

        if skill_c == 1 :
            if x1 - 60 < skillPosX < x1 + 60 and 310 < playerPosY < 330 :
                x1count += 1
                cake1_1 = pygame.image.load('./image/map2/cokedie0.png').convert_alpha()
                #health += 10
            if x2 - 60 < skillPosX < x2 + 60 and 310 < playerPosY < 330 :
                x2count += 1
                cake1_2 = pygame.image.load('./image/map2/cokedie0.png').convert_alpha()
               # health += 10
            if x3 - 60 < skillPosX < x3 + 60 and 310 < playerPosY < 330 :
                x3count += 1
                cake1_3 = pygame.image.load('./image/map2/cokedie0.png').convert_alpha()
              #  health += 10
            if x4 - 60 < skillPosX < x4 + 60 and 310 < playerPosY < 330 :
                x4count += 1
                cake1_4 = pygame.image.load('./image/map2/cokedie0.png').convert_alpha()
               # health += 10
            if x5 - 60 < skillPosX < x5 + 60 and 310 < playerPosY < 330:
                x5count += 1
                cake1_5 = pygame.image.load('./image/map2/cokedie0.png').convert_alpha()

            if x1_2 - 60 < skillPosX < x1_2 + 60 and 75 < playerPosY < 95 :
                x1_2count += 1
            if x2_2 - 60 < skillPosX < x2_2 + 60 and 75 < playerPosY < 95 :
                x2_2count += 1
            if x3_2 - 60 < skillPosX < x3_2 + 60 and 130 < playerPosY < 150 :
                x3_2count += 1


        # if x1 - 10 < circlePosX < x1 + 10 and 310 < playerPosY < 330:
        #     x1count += 2
        #     levelcount += 2
        # if x2 - 10 < circlePosX < x2 + 10 and 310 < playerPosY < 330:
        #     x2count += 2
        #     levelcount += 2
        # if x3 - 10 < circlePosX < x3 + 10 and 310 < playerPosY < 330:
        #     x3count += 2
        #     levelcount += 2
        # if x4 - 10 < circlePosX < x4 + 10 and 310 < playerPosY < 330:
        #     x4count += 2
        #     levelcount += 2
        # if x5 - 10 < circlePosX < x5 + 10 and 310 < playerPosY < 330:
        #     x5count += 2
        #     levelcount += 2
        #
        # if x1_2 - 10 < circlePosX < x1_2 + 10 and 75 < playerPosY < 95:
        #     x1_2count += 2
        #     levelcount += 2
        # if x2_2 - 10 < circlePosX < x2_2 + 10 and 75 < playerPosY < 95:
        #     x2_2count += 2
        #     levelcount += 2
        # if x3_2 - 10 < circlePosX < x3_2 + 10 and 130 < playerPosY < 150:
        #     x3_2count += 2
        #     levelcount += 2

#-------------------------------cake---------------------------------------------------
        if cake1_1Count == 5:
            cake1_1 = pygame.image.load('./image/map2/cokemove0.png').convert_alpha()
        elif cake1_1Count == 10:
            cake1_1 = pygame.image.load('./image/map2/cokemove1.png').convert_alpha()
        elif cake1_1Count == 15:
            cake1_1 = pygame.image.load('./image/map2/cokemove2.png').convert_alpha()
        elif cake1_1Count == 20:
            cake1_1 = pygame.image.load('./image/map2/cokemove3.png').convert_alpha()
        elif cake1_1Count == 0:
            cake1_1 = pygame.image.load('./image/map2/cokemove4.png').convert_alpha()

        if cake1_2Count == 5:
            cake1_2 = pygame.image.load('./image/map2/cokemove0.png').convert_alpha()
        elif cake1_2Count == 10:
            cake1_2 = pygame.image.load('./image/map2/cokemove1.png').convert_alpha()
        elif cake1_2Count == 15:
            cake1_2 = pygame.image.load('./image/map2/cokemove2.png').convert_alpha()
        elif cake1_2Count == 20:
            cake1_2 = pygame.image.load('./image/map2/cokemove3.png').convert_alpha()
        elif cake1_2Count == 0:
            cake1_2 = pygame.image.load('./image/map2/cokemove4.png').convert_alpha()

        if cake1_3Count == 5:
            cake1_3 = pygame.image.load('./image/map2/cokemove0.png').convert_alpha()
        elif cake1_3Count == 10:
            cake1_3 = pygame.image.load('./image/map2/cokemove1.png').convert_alpha()
        elif cake1_3Count == 15:
            cake1_3 = pygame.image.load('./image/map2/cokemove2.png').convert_alpha()
        elif cake1_3Count == 20:
            cake1_3 = pygame.image.load('./image/map2/cokemove3.png').convert_alpha()
        elif cake1_3Count == 0:
            cake1_3 = pygame.image.load('./image/map2/cokemove4.png').convert_alpha()

        if cake1_4Count == 5:
            cake1_4 = pygame.image.load('./image/map2/cokemove0.png').convert_alpha()
        elif cake1_4Count == 10:
            cake1_4 = pygame.image.load('./image/map2/cokemove1.png').convert_alpha()
        elif cake1_4Count == 15:
            cake1_4 = pygame.image.load('./image/map2/cokemove2.png').convert_alpha()
        elif cake1_4Count == 20:
            cake1_4 = pygame.image.load('./image/map2/cokemove3.png').convert_alpha()
        elif cake1_4Count == 0:
            cake1_4 = pygame.image.load('./image/map2/cokemove4.png').convert_alpha()

        if cake1_5Count == 5:
            cake1_5 = pygame.image.load('./image/map2/cokemove0.png').convert_alpha()
        elif cake1_5Count == 10:
            cake1_5 = pygame.image.load('./image/map2/cokemove1.png').convert_alpha()
        elif cake1_5Count == 15:
            cake1_5 = pygame.image.load('./image/map2/cokemove2.png').convert_alpha()
        elif cake1_5Count == 20:
            cake1_5 = pygame.image.load('./image/map2/cokemove3.png').convert_alpha()
        elif cake1_5Count == 0:
            cake1_5 = pygame.image.load('./image/map2/cokemove4.png').convert_alpha()

        if cake2_1Count == 5:
            cake2_1 = pygame.image.load('./image/map2/coke2move0.png').convert_alpha()
        elif cake2_1Count == 10:
            cake2_1 = pygame.image.load('./image/map2/coke2move1.png').convert_alpha()
        elif cake2_1Count == 15:
            cake2_1 = pygame.image.load('./image/map2/coke2move2.png').convert_alpha()
        elif cake2_1Count == 0:
            cake2_1 = pygame.image.load('./image/map2/coke2move3.png').convert_alpha()

        if cake2_2Count == 5:
            cake2_2 = pygame.image.load('./image/map2/coke2move0.png').convert_alpha()
        elif cake2_2Count == 10:
            cake2_2 = pygame.image.load('./image/map2/coke2move1.png').convert_alpha()
        elif cake2_2Count == 15:
            cake2_2 = pygame.image.load('./image/map2/coke2move2.png').convert_alpha()
        elif cake2_2Count == 0:
            cake2_2 = pygame.image.load('./image/map2/coke2move3.png').convert_alpha()

        if cake2_3Count == 5:
            cake2_3 = pygame.image.load('./image/map2/coke2move0.png').convert_alpha()
        elif cake2_3Count == 10:
            cake2_3 = pygame.image.load('./image/map2/coke2move1.png').convert_alpha()
        elif cake2_3Count == 15:
            cake2_3 = pygame.image.load('./image/map2/coke2move2.png').convert_alpha()
        elif cake2_3Count == 0:
            cake2_3 = pygame.image.load('./image/map2/coke2move3.png').convert_alpha()

#-----------------------------------------------------------------------------------------
        playerPosX += playerVelocityX  # 가는만큼 더해줌
        walkCount += 1
        zCount += 1
        xCount += 1
        cCount += 1
        uCount += 1
        if cake1_1Count >= 0:
            cake1_1Count += 1
        if cake1_2Count >= 0:
            cake1_2Count += 1
        if cake1_3Count >= 0:
            cake1_3Count += 1
        if cake1_4Count >= 0:
            cake1_4Count += 1
        if cake1_5Count >= 0:
            cake1_5Count += 1
        if cake2_1Count >= 0:
            cake2_1Count += 1
        if cake2_2Count >= 0:
            cake2_2Count += 1
        if cake2_3Count >= 0:
            cake2_3Count += 1
        ######

        # 이미지 초기화
        if walkCount ==6:
            walkCount = 0
        if zCount == 10:
            zCount = 0
        if xCount == 12:
            xCount = 0
        if cCount == 7:
            cCount = 0
        if uCount == 3:
            uCount = 0
        if cake1_1Count == 25:
            cake1_1Count = 0
        if cake1_2Count == 25:
            cake1_2Count = 0
        if cake1_3Count == 25:
            cake1_3Count = 0
        if cake1_4Count == 25:
            cake1_4Count = 0
        if cake1_5Count == 25:
            cake1_5Count = 0
        if cake2_1Count == 25:
            cake2_1Count = 0
        if cake2_2Count == 25:
            cake2_2Count = 0
        if cake2_3Count == 25:
            cake2_3Count = 0

        ######
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

        #######
        rel_x = stagePosX % bgWidth
        screen.blit(bg, (rel_x - bgWidth, 0))
        if rel_x < W:
            screen.blit(bg, (rel_x, 0))

        # screen.blit(player, (circlePosX, playerPosY))
        screen.blit(skill, (skillPosX, skillPosY))

        ########################33
        x1_2 = x1_2 + x1_2_speed
        if x1_2 > screen.get_width() - 710 or x1_2 < 0:
            x1_2_speed = -x1_2_speed  # 움직임 부호를 바꿔준다.

        x2_2 = x2_2 + x2_2_speed
        if x2_2 > screen.get_width() - 710 or x2_2 < 0:
            x2_2_speed = -x2_2_speed  # 움직임 부호를 바꿔준다.

        x3_2 = x3_2 + x3_2_speed
        if x3_2 < 700 or x3_2 > 900:
            x3_2_speed = -x3_2_speed

        x1 = x1 + x1_speed
        if x1 > screen.get_width() - 130 or x1 < 0:
            x1_speed = -x1_speed  # 움직임 부호를 바꿔준다.

        x2 = x2 + x2_speed
        if x2 > screen.get_width() - 130 or x2 < 0:
            x2_speed = -x2_speed  # 움직임 부호를 바꿔준다.

        x3 = x3 - x3_speed
        if x3 > screen.get_width() - 130 or x3 < 0:
            x3_speed = -x3_speed  # 움직임 부호를 바꿔준다.

        x4 = x4 - x4_speed
        if x4 > screen.get_width() - 130 or x4 < 0:
            x4_speed = -x4_speed  # 움직임 부호를 바꿔준다.

        x5 = x5 + x5_speed
        if x5 > screen.get_width() - 130 or x5 < 0:
            x5_speed = -x5_speed  # 움직임 부호를 바꿔준다.
        ##################################333

#----------------메소 떨굼--
        if x1count >= 30:
            x1count = -1
            cake1_1 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            #y = 5000
            x1 = 5000
            meso += 10
            level += 1
        if x2count >= 30:
            x2count = -1
            cake1_2 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            #y = 5000
            x2 = 5000
            meso += 10
            level += 1
        if x3count >= 30:
            x3count = -1
            cake1_3 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            #y = 5000
            x3 = 5000
            meso += 10
            level += 1
        if x4count >= 30:
            x4count = -1
            cake1_4 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            #y = 5000
            x4 = 5000
            meso += 10
            level += 1
        if x5count >= 30:
            x5count = -1
            cake1_5 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            #y = 5000
            x5 = 5000
            meso += 10
            level += 1
        if x1_2count >= 30:
            x1_2count = -1
            cake2_1 = pygame.image.load('./image/attack/moo.png').convert_alpha()
           # y_2 = 5000
            x1_2 = 5000
            meso += 10
            level += 1
        if x2_2count >= 30:
            x2_2count = -1
            cake2_2 = pygame.image.load('./image/attack/moo.png').convert_alpha()
            #y_2 = 5000
            x2_2 = 5000
            meso += 10
            level += 1
        if x3_2count >= 30:
            x3_2count = -1
            cake2_3 = pygame.image.load('./image/attack/moo.png').convert_alpha()
           # y_3 = 5000
            x3_2 = 5000
            meso += 10
            level += 1

        if 10 <= level <= 11:
            screen.blit(level10, (350,80))

        screen.blit(cake1_1, [x1, y])
        screen.blit(cake1_2, [x2, y])
        screen.blit(cake1_3, [x3, y])
        screen.blit(cake1_4, [x4, y])
        screen.blit(cake1_5, [x5, y])
        screen.blit(cake2_1, [x1_2, y_2])
        screen.blit(cake2_2, [x2_2, y_2])
        screen.blit(cake2_3, [x3_2, y_3])

        screen.blit(skill, (skillPosX, skillPosY))

        land(screen)
        skyland(screen, 300, 300)
        skyland2(screen, 300, 300)
        screen.blit(player, (circlePosX, playerPosY))
        screen.blit(name, (circlePosX+10,playerPosY+193))


        pygame.display.update()  # 화면 업데이트
        CLOCK.tick(FPS)

if __name__ == "__main__":
    play(screen)