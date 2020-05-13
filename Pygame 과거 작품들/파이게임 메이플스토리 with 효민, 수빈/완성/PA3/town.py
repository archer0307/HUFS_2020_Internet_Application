import pygame #pyamge 모듈 import
from pygame.locals import * #pygame.locals 하위 모듈 import
import option, user, map2 ,map1
import keyboard
import sys

def play(screen, health, mana, level, exp, h_count, m_count, player, meso):
    pygame.init()

    #############
    W, H = 1024, 670  # screen size
    HW, HH = W / 2, H / 2  # half

    CLOCK = pygame.time.Clock()
    FPS = 1000

    #############
    BLACK = (0, 0, 0, 255)
    WHITE = (255, 255, 255, 255)
    #############
    bg = pygame.image.load("./image/town/town.png")
    bg = pygame.transform.scale(bg, (1700, 590))
    bgWidth, bgHeight = bg.get_rect().size  # bg 가로 세로길이

    shop = 0
    shop_image = pygame.image.load('./image/attack/moo.png').convert_alpha()

    health_shop = pygame.image.load("./image/attack/moo.png").convert_alpha()
    health_shop = pygame.transform.scale(health_shop, (300, 50))
    health_rect = health_shop.get_rect(x=500, y=300)
    mana_shop = pygame.image.load("./image/attack/moo.png").convert_alpha()
    mana_shop = pygame.transform.scale(mana_shop, (300, 50))
    mana_rect = mana_shop.get_rect(x=500, y=350)

    name = pygame.image.load('./image/name.png')
    #500, 200

    stageWidth = bgWidth  # 삽입된 이미지의 좌표
    stagePosX = 0

    startScrollingPosX = HW  # 640 #이미지 이동 기준

    ## 비교좌표
    circleRadius = 25
    circlePosX = circleRadius
    ##플레이어좌표
    playerPosX = 30
    playerPosY = 340
    tempPosY = 0
    jump = 0
    playerVelocityX = 0  # 속도
    playerVelocityY = 0  # y축 속도

    ##스킬
    skillPosX = 0
    skillPosY = 0

    xCount = 0
    zCount = 0
    cCount = 0
    stand = 2
    walkCount = 0

    skill = pygame.image.load('./image/attack/moo.png').convert_alpha()
    cursor = pygame.image.load("./image/normal.gif").convert()
    cursor.set_colorkey((0,255,0))

    # potal = pygame.image.load("./image/img/potal.png")
    # potal = pygame.transform.scale(potal, (200, 400))


    running = True
    while running:
        target = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))
        #screen.blit(potal, (700, 330))
        option.play(screen, health, mana, level, exp, h_count, m_count, meso)  # option은 town map1 map2용
        k = pygame.key.get_pressed()
        ##############################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 종료시 입력시
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):  # ESE 누르면 종료
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_a):
                    if shop == 0:
                        shop = 1
                        shop_image = pygame.image.load("./image/img/shop.png").convert_alpha()
                    else:
                        shop_image = pygame.image.load('./image/attack/moo.png').convert_alpha()
                        shop = 0
            if health_rect.collidepoint(pygame.mouse.get_pos()):  ##start에 마우스가 올려져 있을 때
                if event.type == MOUSEBUTTONDOWN:  # 마우스를 클릭하면
                    if meso > 0:
                        h_count += 1
                        meso -= 50
            if mana_rect.collidepoint(pygame.mouse.get_pos()):  ##start에 마우스가 올려져 있을 때
                if event.type == MOUSEBUTTONDOWN:  # 마우스를 클릭하면
                    if meso > 0:
                        m_count += 1
                        meso -= 50
            if event.type == pygame.QUIT:  # 종료 입력시
                pygame.quit()

            #####HP/MP충전########
            if keyboard.is_pressed('s'):
                if h_count > 0 and health <150:
                    h_count -= 1
                    health = 150
            if keyboard.is_pressed('d'):
                if m_count > 0 and mana <150:
                    m_count -= 1
                    mana = 150

            #####창전환###########
            if keyboard.is_pressed('F12'):  # 화면 키우기
                screen = pygame.display.set_mode((1024, 670), pygame.FULLSCREEN | HWSURFACE | DOUBLEBUF)  # 해상도 480*320, 전체화면모드, 하드웨어 가속사용, 더블버퍼모드
            if keyboard.is_pressed('F11'):  # 윈도우 모드
                screen = pygame.display.set_mode((1024, 670), DOUBLEBUF)  # 해상도 480*320, 윈도우모드, 더블버퍼모드
            ######################

        #############################################################
        if k[K_LEFT]:
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
            if jump == 0:
                tempPosY = playerPosY
                playerVelocityY = 20
            jump = 1

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
            if stand == 1:
                mana-=1
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
            else:
                mana-=1
                skillPosX = circlePosX + 50
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

        elif k[K_c]and mana >= 1:
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

        elif k[K_UP]:
            if 0 < circlePosX <50 :
                map1.play(screen, health, mana, level, exp, h_count, m_count, player, meso)
            if 800 < circlePosX:
                map2.play(screen, health, mana, level, exp, h_count, m_count, player, meso)

        else:
            skill = pygame.image.load('./image/attack/moo.png').convert_alpha()
            playerVelocityX = 0
            # playerPosY = 340
            if stand == 1:  # 왼
                player = pygame.image.load('./image/player/standleft.png')
            else:  # 2 오
                player = pygame.image.load('./image/player/standright.png')

        playerPosX += playerVelocityX  # 가는만큼 더해줌
        walkCount += 1
        zCount += 1
        xCount += 1
        cCount += 1

        ######
        ######
        ######


        if playerPosX > bgWidth - 60:
            map2.play(screen, health, mana, level, exp, h_count, m_count, player, meso)
        if playerPosX < bgWidth - bgWidth + 2:
            map1.play(screen, health, mana, level, exp, h_count, m_count, player, meso)

        ######
        ######
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

        ######
        # 화면 오른쪽 끝
        if playerPosX > stageWidth - 60: playerPosX = stageWidth - 60
        # 화면 왼쪽 끝
        if playerPosX < 0: playerPosX = 0

        #######이동관련좌표
        if playerPosX < startScrollingPosX:
            circlePosX = playerPosX
        elif playerPosX > stageWidth - startScrollingPosX:
            circlePosX = playerPosX - stageWidth + W
        else:
            circlePosX = startScrollingPosX
            stagePosX += -playerVelocityX

        #######
        rel_x = stagePosX % bgWidth
        screen.blit(bg, (rel_x - bgWidth, 0))
        if rel_x < W:
            screen.blit(bg, (rel_x, 0))

        if jump == 1:
            playerPosY -= playerVelocityY
            playerVelocityY -= 4
            if playerVelocityY == -24:
                jump = 0
                playerPos = tempPosY
            if stand == 1:
                player = pygame.image.load('./image/player/jumpleft.png')
            else:
                player = pygame.image.load('./image/player/jumpright.png')

        screen.blit(player, (circlePosX, playerPosY))
        screen.blit(skill, (skillPosX, skillPosY))
        # if k[K_a]:
        #     if shop == 0:
        #         shop = 1
        #         shop_image = pygame.image.load("./image/img/shop.png").convert_alpha()
        #     else :
        #         shop_image=pygame.image.load('./image/attack/moo.png').convert_alpha()
        #         shop = 0

        shop_image = pygame.transform.scale(shop_image, (300, 200))
        screen.blit(shop_image, (500, 200))
        screen.blit(health_shop, health_rect)
        screen.blit(mana_shop, mana_rect)
        screen.blit(cursor, target)
        screen.blit(name, (circlePosX+10,playerPosY+193))

        pygame.display.update()  # 화면 업데이트
        CLOCK.tick(FPS)
if __name__ == "__main__":

    play()