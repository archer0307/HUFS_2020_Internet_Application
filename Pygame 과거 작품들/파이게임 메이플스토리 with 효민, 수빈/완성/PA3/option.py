import pygame #pyamge 모듈 import
from pygame.locals import * #pygame.locals 하위 모듈 import


exp_percent = 0

def play(screen, health, mana, level, exp, h_count, m_count, meso):
    #######캐릭정보창#####

    pygame.draw.rect(screen, (255,255,255), [0, 590, 1024, 80])  # userscreen
    pygame.draw.rect(screen, (000, 000, 000), [248, 601, 154, 18])  # health 250~400
    pygame.draw.rect(screen, (000, 000, 000), [463, 601, 154, 18])  # mana 465~615
    pygame.draw.rect(screen, (198, 198, 198), [5, 595, 70, 70])  # userimage
    head_image = pygame.image.load('./image/img/profile.png')  # skill2, c button
    screen.blit(head_image, (12, 608))
    pygame.draw.rect(screen, (255, 000, 000), [250, 603, health, 15])  # health
    pygame.draw.rect(screen, (000, 000, 255), [465, 603, mana, 15])  # mana
    susoming = pygame.image.load('./image/img/susoming.png')  # skill2, c button
    susoming = pygame.transform.scale(susoming, (350, 80))
    screen.blit(susoming, (640, 590))

    font = pygame.font.Font("./font/a아시아고딕B.ttf", 15)
    font2 = pygame.font.Font("./font/a아시아고딕B.ttf", 15)
    name = font.render("<player>", True, (0,0,0))
    screen.blit(name, (80, 600))
    level_text = font.render(("level: %d" % level), True, (0, 0, 0))
    screen.blit(level_text, (90, 620))
    #exp_percent = exp / level
    # exp_text = font.render(("exp: %d%% (%d/%d)" % (exp_percent, exp, 100*level) ), True, (0, 0, 0))
    # screen.blit(exp_text, (80, 620))
    money_text = font.render("meso: %d"%(meso), True, (0, 0, 0))
    screen.blit(money_text, (90, 640))
    h = font.render("health", True, (0, 0, 0))
    screen.blit(h, (195, 602))
    m = font.render("mana", True, (0, 0, 0))
    screen.blit(m, (419, 602))
    attack = pygame.image.load('./image/skill/attack.png') #basic attack
    screen.blit(attack, [300, 630, 30, 30])
    skill_x= pygame.image.load('./image/skill/skill_x.png') #skill 1, x button
    screen.blit(skill_x, [350, 630, 30, 30])
    skill_c = pygame.image.load('./image/skill/skill_c.png') # skill2, c button
    screen.blit(skill_c, [400, 630, 30, 30])
    skill_home_image = pygame.image.load('./image/skill/home.png') #home
    screen.blit(skill_home_image, [450, 630, 30, 30])
    skill_health = pygame.image.load('./image/skill/health.png') #health, ctrl button
    screen.blit(skill_health, [500, 630, 30, 30])
    health_text = font2.render(("%d"%(h_count)), True, (0, 0, 0))
    screen.blit(health_text, (532, 635))
    skill_mana = pygame.image.load('./image/skill/mana.png') # mana, shift button
    screen.blit(skill_mana, [550, 630, 30, 30])
    mana_text = font2.render(("%d" %(m_count)), True, (0, 0, 0))
    screen.blit(mana_text, (582, 635))

    # ssm = font.render("SuSoMingStory#", True, (0, 0, 0))
    # screen.blit(ssm, (500, 440))