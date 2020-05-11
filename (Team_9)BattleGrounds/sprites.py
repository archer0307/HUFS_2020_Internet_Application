import pygame as pg
from settings import *
import time
import random
global p_spread_pos, p_spread_bool, c_spread_pos, c_spread_bool
p_spread_pos = []
p_spread_bool = False
c_spread_pos = []
c_spread_bool = False
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.players
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load("image/P1_Down.png")
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.dir = 2
        self.shot_delay = 0#총알 간격 초단위임
        self.last_shot = 0 #마지막으로 총알쏜 시간
        self.drop_delay = 3
        self.last_drop = time.time()
        self.arrival = 0
        self.health = PLAYER_HEALTH
        self.weapon = "PISTOL"
        self.pistol_ammo = 15 #권총 장탄수
        self.rifle_ammo = 30# 라이플 장탄수
        self.rifle_mxtotal_am = 90# 라이플 total 총알수
        self.shotgun_shells = 8 #샷건 장탄수
        self.shotgun_mxtotal_am = 24# 샷건 total 총알수
        self.sniper_ammo = 7# 스나이퍼 장탄수
        self.sniper_mxtotal_am = 21#스나이퍼 total 총알수
        self.bazook_mxtotal_am = 10#바주카포 total 총알수
        self.speed = PLAYER_SPEED

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.use_weapon()

        if keys[pg.K_f]: #플레이어 근처로 아이템을 투하한다.
            if time.time() - self.last_drop > self.drop_delay:
                box = Box(self.game)
                box.rect.x = self.rect.x + 20
                box.rect.y = self.rect.y + 20
                self.game.all_sprites.add(box)
                self.last_drop = time.time()
                self.game.box.add(box)
                item = Item()
                item.rect.x = box.rect.x
                item.rect.y = self.rect.y - HEIGHT //2
                self.game.items.add(item)
                self.game.all_sprites.add(item)
                pg.mixer.Channel(3).play(pg.mixer.Sound("sound/BOX.wav"))

        if keys[pg.K_r]:
            self.reload()

        if  keys[pg.K_a]:
            self.image = pg.image.load("image/P1_Left.png")
            self.vx = -self.speed
            self.dir = 3
        if keys[pg.K_d]:
            self.image = pg.image.load("image/P1_Right.png")
            self.vx = self.speed
            self.dir = 1
        if keys[pg.K_w]:
            self.image = pg.image.load("image/P1_Up.png")
            self.vy = -self.speed
            self.dir = 0
        if keys[pg.K_s]:
            self.image = pg.image.load("image/P1_Down.png")
            self.vy = self.speed
            self.dir = 2
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def use_weapon(self): #무기발사
        if self.weapon == "PISTOL":
            if self.dir ==3: self.image = pg.image.load("image/P1_Left.png")
            elif self.dir ==1: self.image = pg.image.load("image/P1_Right.png")
            elif self.dir ==0: self.image = pg.image.load("image/P1_Up.png")
            elif self.dir ==2: self.image = pg.image.load("image/P1_Down.png")
            self.speed = PLAYER_SPEED
            if self.pistol_ammo == 0 and time.time() - self.last_shot > self.shot_delay:
                self.shot_delay = 2
                self.pistol_ammo = 15
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/pistol_reload.wav"))
            if time.time() - self.last_shot > self.shot_delay:
                player_bullet = Pistol_Bullet()
                player_bullet.rect.x = self.rect.x
                player_bullet.rect.y = self.rect.y
                player_bullet.dir = self.game.player.dir
                self.shot_delay = player_bullet.delay
                self.game.all_sprites.add(player_bullet)
                self.game.player_bullets.add(player_bullet)
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/PISTOL.wav"))
                self.pistol_ammo -= 1
                self.last_shot = time.time()

        elif self.weapon == "RIFLE":
            if self.dir ==3: self.image = pg.image.load("image/P1_Left.png")
            elif self.dir ==1: self.image = pg.image.load("image/P1_Right.png")
            elif self.dir ==0: self.image = pg.image.load("image/P1_Up.png")
            elif self.dir ==2: self.image = pg.image.load("image/P1_Down.png")
            if self.rifle_mxtotal_am == 0 :
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/get_bullets.wav"))
                self.weapon = "PISTOL"
                self.pistol_ammo = 15
                self.shot_delay = -1
            elif self.rifle_ammo == 0 and time.time() - self.last_shot > self.shot_delay:
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/get_bullets.wav"))
                self.shot_delay = 4
                self.rifle_ammo = 30
            if time.time() - self.last_shot > self.shot_delay:
                player_bullet = Rifle_Bullet()
                player_bullet.rect.x = self.rect.x
                player_bullet.rect.y = self.rect.y
                player_bullet.dir = self.game.player.dir
                if self.shot_delay == -1:
                    self.shot_delay = 0.4
                else:
                    self.shot_delay = player_bullet.delay
                self.game.all_sprites.add(player_bullet)
                self.game.player_bullets.add(player_bullet)
                self.rifle_ammo -= 1
                self.rifle_mxtotal_am -= 1
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/Rifle.wav"))
                self.last_shot = time.time()

        elif self.weapon == "SHOTGUN":
            if self.dir ==3: self.image = pg.image.load("image/P1_Left.png")
            elif self.dir ==1: self.image = pg.image.load("image/P1_Right.png")
            elif self.dir ==0: self.image = pg.image.load("image/P1_Up.png")
            elif self.dir ==2: self.image = pg.image.load("image/P1_Down.png")
            if self.shotgun_mxtotal_am == 0 :
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/get_bullets.wav"))
                self.weapon = "PISTOL"
                self.pistol_ammo = 15
                self.shot_delay = -1
            elif self.shotgun_shells == 0 and time.time() - self.last_shot > 0.5:
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/shot_reload.wav"))
                self.shot_delay = 4
                self.shotgun_shells = 8

            if time.time() - self.last_shot > self.shot_delay:
                bullet_list = []
                global p_spread_bool , p_spread_pos
                spread_num1 = -0.1
                if p_spread_bool == False:
                    for i in range(20):
                        player_bullet = Shotgun_Bullet()
                        bullet_list.append(player_bullet)
                    for b in bullet_list:
                        spread_num2 = random.randint(-10, 10)
                        b.rect.x = self.rect.x + spread_num2
                        b.rect.y = self.rect.y + spread_num2
                        p_spread_pos.append(spread_num2)
                        b.dir = self.dir
                        b.bullet_spread = spread_num1
                        self.game.all_sprites.add(b)
                        self.game.player_bullets.add(b)
                        if self.shot_delay == -1:
                            self.shot_delay = 0.4
                        else:
                            self.shot_delay = b.delay
                        spread_num1 += 0.2
                    pg.mixer.Channel(0).play(pg.mixer.Sound("sound/Shotgun.wav"))
                else:
                    for i in range(20):
                        player_bullet = Shotgun_Bullet()
                        bullet_list.append(player_bullet)
                    i = 0
                    for b in bullet_list:
                        b.rect.x = self.rect.x + p_spread_pos[i]
                        b.rect.y = self.rect.y + p_spread_pos[i]

                        b.dir = self.dir
                        b.bullet_spread = spread_num1
                        self.game.all_sprites.add(b)
                        self.game.player_bullets.add(b)
                        if self.shot_delay == -1:
                            self.shot_delay = 0.4
                        else:
                            self.shot_delay = b.delay
                        spread_num1 += 0.2
                        i += 1
                self.shotgun_shells -= 1
                self.shotgun_mxtotal_am -= 1
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/Shotgun.wav"))
                self.last_shot = time.time()
                print("1", self.shotgun_shells, "total:", self.shotgun_mxtotal_am)
                p_spread_bool = True

        elif self.weapon == "SNIPER":
            if self.dir ==3: self.image = pg.image.load("image/P1_Left.png")
            elif self.dir ==1: self.image = pg.image.load("image/P1_Right.png")
            elif self.dir ==0: self.image = pg.image.load("image/P1_Up.png")
            elif self.dir ==2: self.image = pg.image.load("image/P1_Down.png")
            if self.sniper_mxtotal_am == 0 :
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/get_bullets.wav"))
                self.weapon = "PISTOL"
                self.pistol_ammo = 15
                self.shot_delay = -1
            elif self.sniper_ammo == 0 and time.time() - self.last_shot > 0.3:
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/Sniper_reload.wav"))
                self.shot_delay = 4.3
                self.sniper_ammo = 7
            if time.time() - self.last_shot > self.shot_delay:
                player_bullet = Sniper_Bullet()
                player_bullet.rect.x = self.rect.x
                player_bullet.rect.y = self.rect.y
                player_bullet.dir = self.game.player.dir
                if self.shot_delay == -1:
                    self.shot_delay = 0.4
                else:
                    self.shot_delay = player_bullet.delay
                self.game.all_sprites.add(player_bullet)
                self.game.player_bullets.add(player_bullet)
                self.sniper_ammo -= 1
                self.sniper_mxtotal_am -= 1
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/Sniper.wav"))
                self.last_shot = time.time()

        elif self.weapon == "BAZOOKA":
            if self.dir ==3: self.image = pg.image.load("image/P1_Left.png")
            elif self.dir ==1: self.image = pg.image.load("image/P1_Right.png")
            elif self.dir ==0: self.image = pg.image.load("image/P1_Up.png")
            elif self.dir ==2: self.image = pg.image.load("image/P1_Down.png")
            if self.bazook_mxtotal_am == 0 :
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/get_bullets.wav"))
                self.weapon = "PISTOL"
                self.pistol_ammo = 15
                self.shot_delay = -1
            if time.time() - self.last_shot > self.shot_delay:
                player_bullet = Bazooka()
                player_bullet.rect.x = self.rect.x
                player_bullet.rect.y = self.rect.y
                player_bullet.dir = self.game.player.dir
                if self.shot_delay == -1:
                    self.shot_delay = 0.4
                else:
                    self.shot_delay = player_bullet.delay
                self.game.all_sprites.add(player_bullet)
                self.game.player_bullets.add(player_bullet)
                self.bazook_mxtotal_am -= 1
                self.last_shot = time.time()
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/Bazooka.wav"))

    def reload(self):
        if self.weapon == "PISTOL" :
            pg.mixer.Channel(0).play(pg.mixer.Sound("sound/pistol_reload.wav"))
            self.last_shot = time.time()
            self.shot_delay = 2
            self.pistol_ammo = 15
        elif self.weapon == "RIFLE" :
            if self.rifle_mxtotal_am != self.rifle_ammo:
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/get_bullets.wav"))
                self.last_shot = time.time()
                self.shot_delay = 4
                self.rifle_ammo = 30
        elif self.weapon == "SHOTGUN" :
            if self.shotgun_mxtotal_am != self.shotgun_shells:
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/shot_reload.wav"))
                self.last_shot = time.time()
                self.shot_delay = 4
                self.shotgun_shells = 8
        elif self.weapon == "SNIPER" :
            if self.sniper_mxtotal_am != self.sniper_ammo:
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/Sniper_reload.wav"))
                self.last_shot = time.time()
                self.shot_delay = 4.3
                self.sniper_ammo = 7

    def get_weapon(self,weapon_num) : #보급상자로부터 무기를 얻는다(main.py에서 사용)
        self.shot_delay = 0
        self.pistol_ammo = 15
        if weapon_num is 1:
            self.rifle_ammo =30
            self.rifle_mxtotal_am = 90
            self.speed = 130
            self.weapon = "RIFLE"
        if weapon_num is 2:
            self.speed = 150
            self.shotgun_mxtotal_am = 24
            self.shotgun_shells = 8
            self.weapon = "SHOTGUN"
        if weapon_num is 3:
            self.speed = 110
            self.weapon = "BAZOOKA"
        if weapon_num is 4:
            pg.mixer.Channel(0).play(pg.mixer.Sound("sound/getHP.wav"))
            self.health = PLAYER_HEALTH
        if weapon_num is 5:
            self.sniper_ammo = 7
            self.sniper_mxtotal_am = 21
            self.speed = 120
            self.weapon = "SNIPER"
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def draw_health(self):
        if self.health > 60:
            col = GREEN
        elif self.health > 30:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.health / PLAYER_HEALTH)
        self.health_bar = pg.Rect(0,0,width,2)
        if self.health <= PLAYER_HEALTH:
            pg.draw.rect(self.image, col, self.health_bar)

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        if self.health <= 0:
            self.game.player_killed = True #플레이어1의 사망을 Game클래스에 알림
        self.image = self.image


class Challenger(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites , game.challengers
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load("image/P2_Down.png")
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.dir = 0
        self.shot_delay = 0
        self.last_shot = 0
        self.drop_delay = 3
        self.last_drop = time.time()
        self.arrival = 0
        self.health = CHALLENGER_HEALTH
        self.weapon = "PISTOL"
        self.pistol_ammo = 15
        self.rifle_ammo = 30
        self.rifle_mxtotal_am = 90
        self.shotgun_shells = 8
        self.shotgun_mxtotal_am = 24
        self.sniper_ammo = 7
        self.sniper_mxtotal_am = 21
        self.bazook_mxtotal_am = 10
        self.speed = PLAYER_SPEED

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_SLASH]:
            self.use_weapon()


        if keys[pg.K_PERIOD]:
            if time.time() - self.last_drop > self.drop_delay:
                box = Box(self.game)
                box.rect.x = self.rect.x + 20
                box.rect.y = self.rect.y + 20
                self.game.all_sprites.add(box)
                self.last_drop = time.time()
                self.game.box.add(box)
                item = Item()
                item.rect.x = box.rect.x
                item.rect.y = self.rect.y - HEIGHT //2
                self.game.items.add(item)
                self.game.all_sprites.add(item)
                pg.mixer.Channel(4).play(pg.mixer.Sound("sound/BOX.wav"))
        if keys[pg.K_COMMA]:
            self.reload()
        if keys[pg.K_LEFT]:
            if self.weapon == "PISTOL" : self.image = pg.image.load("image/P2_Left.png")
            elif self.weapon == "RIFLE": self.image = pg.image.load("image/P2_Left.png")
            elif self.weapon == "BAZOOKA": self.image = pg.image.load("image/P2_Left.png")
            elif self.weapon == "SHOTGUN": self.image = pg.image.load("image/P2_Left.png")
            elif self.weapon == "SNIPER": self.image = pg.image.load("image/P2_Left.png")
            self.vx = -self.speed
            self.dir = 3

        if keys[pg.K_RIGHT]:
            if self.weapon == "PISTOL" : self.image = pg.image.load("image/P2_Right.png")
            elif self.weapon == "RIFLE": self.image = pg.image.load("image/P2_Right.png")
            elif self.weapon == "BAZOOKA": self.image = pg.image.load("image/P2_Right.png")
            elif self.weapon == "SHOTGUN": self.image = pg.image.load("image/P2_Right.png")
            elif self.weapon == "SNIPER": self.image = pg.image.load("image/P2_Right.png")
            self.vx = self.speed
            self.dir = 1
        if keys[pg.K_UP]:
            if self.weapon == "PISTOL" : self.image = pg.image.load("image/P2_Up.png")
            elif self.weapon == "RIFLE": self.image = pg.image.load("image/P2_Up.png")
            elif self.weapon == "BAZOOKA": self.image = pg.image.load("image/P2_Up.png")
            elif self.weapon == "SHOTGUN": self.image = pg.image.load("image/P2_Up.png")
            elif self.weapon == "SNIPER": self.image = pg.image.load("image/P2_Up.png")
            self.vy = -self.speed
            self.dir = 0
        if keys[pg.K_DOWN]:
            if self.weapon == "PISTOL" : self.image = pg.image.load("image/P2_Down.png")
            elif self.weapon == "RIFLE": self.image = pg.image.load("image/P2_Down.png")
            elif self.weapon == "BAZOOKA": self.image = pg.image.load("image/P2_Down.png")
            elif self.weapon == "SHOTGUN": self.image = pg.image.load("image/P2_Down.png")
            elif self.weapon == "SNIPER": self.image = pg.image.load("image/P2_Down.png")
            self.vy = self.speed
            self.dir = 2
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def use_weapon(self):

        if self.weapon == "PISTOL":
            if self.dir ==3: self.image = pg.image.load("image/P2_Left.png")
            elif self.dir ==1: self.image = pg.image.load("image/P2_Right.png")
            elif self.dir ==0: self.image = pg.image.load("image/P2_Up.png")
            elif self.dir ==2: self.image = pg.image.load("image/P2_Down.png")
            self.speed = PLAYER_SPEED
            if self.pistol_ammo == 0 and time.time() - self.last_shot > self.shot_delay:
                pg.mixer.Channel(1).play(pg.mixer.Sound("sound/pistol_reload.wav"))
                self.shot_delay = 2
                self.pistol_ammo = 15
            if time.time() - self.last_shot > self.shot_delay:
                challenger_bullet = Pistol_Bullet()
                challenger_bullet.rect.x = self.rect.x
                challenger_bullet.rect.y = self.rect.y
                challenger_bullet.dir = self.game.challenger.dir
                self.shot_delay = challenger_bullet.delay
                self.game.all_sprites.add(challenger_bullet)
                self.game.challenger_bullets.add(challenger_bullet)
                pg.mixer.Channel(1).play(pg.mixer.Sound("sound/PISTOL.wav"))
                self.pistol_ammo -= 1
                self.last_shot = time.time()

        elif self.weapon == "RIFLE":
            if self.dir ==3: self.image = pg.image.load("image/P2_Left.png")
            elif self.dir ==1: self.image = pg.image.load("image/P2_Right.png")
            elif self.dir ==0: self.image = pg.image.load("image/P2_Up.png")
            elif self.dir ==2: self.image = pg.image.load("image/P2_Down.png")
            if self.rifle_mxtotal_am == 0:
                pg.mixer.Channel(1).play(pg.mixer.Sound("sound/get_bullets.wav"))
                self.weapon = "PISTOL"
                self.pistol_ammo = 15
                self.shot_delay = -1
            elif self.rifle_ammo == 0 and time.time() - self.last_shot > self.shot_delay:
                pg.mixer.Channel(1).play(pg.mixer.Sound("sound/get_bullets.wav"))
                self.shot_delay = 4
                self.rifle_ammo = 30
            if time.time() - self.last_shot > self.shot_delay:
                challenger_bullet = Rifle_Bullet()
                challenger_bullet.rect.x = self.rect.x
                challenger_bullet.rect.y = self.rect.y
                challenger_bullet.dir = self.game.challenger.dir
                if self.shot_delay == -1:
                    self.shot_delay = 0.4
                else:
                    self.shot_delay = challenger_bullet.delay
                self.game.all_sprites.add(challenger_bullet)
                self.game.challenger_bullets.add(challenger_bullet)
                pg.mixer.Channel(1).play(pg.mixer.Sound("sound/Rifle.wav"))
                self.rifle_ammo -= 1
                self.rifle_mxtotal_am -= 1
                self.last_shot = time.time()

        elif self.weapon == "SHOTGUN":
            if self.dir ==3: self.image = pg.image.load("image/P2_Left.png")
            elif self.dir ==1: self.image = pg.image.load("image/P2_Right.png")
            elif self.dir ==0: self.image = pg.image.load("image/P2_Up.png")
            elif self.dir ==2: self.image = pg.image.load("image/P2_Down.png")
            if self.shotgun_mxtotal_am == 0:
                pg.mixer.Channel(1).play(pg.mixer.Sound("sound/get_bullets.wav"))
                self.weapon = "PISTOL"
                self.pistol_ammo = 15
                self.shot_delay = -1
            elif self.shotgun_shells == 0 and time.time() - self.last_shot > 0.5:
                pg.mixer.Channel(1).play(pg.mixer.Sound("sound/shot_reload.wav"))
                self.shot_delay = 4
                self.shotgun_shells = 8
            if time.time() - self.last_shot > self.shot_delay:
                bullet_list = []
                global c_spread_bool , c_spread_pos
                spread_num1 = -0.1
                if c_spread_bool == False:
                    for i in range(20):
                        challenger_bullet = Shotgun_Bullet()
                        bullet_list.append(challenger_bullet)
                    for b in bullet_list:
                        spread_num2 = random.randint(-10, 10)
                        b.rect.x = self.rect.x + spread_num2
                        b.rect.y = self.rect.y + spread_num2
                        c_spread_pos.append(spread_num2)
                        b.dir = self.dir
                        b.bullet_spread = spread_num1
                        self.game.all_sprites.add(b)
                        self.game.challenger_bullets.add(b)
                        if self.shot_delay == -1:
                            self.shot_delay = 0.4
                        else:
                            self.shot_delay = b.delay
                        spread_num1 += 0.2
                    pg.mixer.Channel(1).play(pg.mixer.Sound("sound/Shotgun.wav"))
                else:
                    for i in range(20):
                        challenger_bullet = Shotgun_Bullet()
                        bullet_list.append(challenger_bullet)
                    i = 0
                    for b in bullet_list:
                        b.rect.x = self.rect.x + c_spread_pos[i]
                        b.rect.y = self.rect.y + c_spread_pos[i]

                        b.dir = self.dir
                        b.bullet_spread = spread_num1
                        self.game.all_sprites.add(b)
                        self.game.challenger_bullets.add(b)
                        if self.shot_delay == -1:
                            self.shot_delay = 0.4
                        else:
                            self.shot_delay = b.delay
                        spread_num1 += 0.2
                        i += 1
                    pg.mixer.Channel(1).play(pg.mixer.Sound("sound/Shotgun.wav"))
                self.shotgun_shells -= 1
                self.shotgun_mxtotal_am -= 1
                self.last_shot = time.time()
                c_spread_bool = True
        elif self.weapon == "SNIPER":
            if self.dir ==3: self.image = pg.image.load("image/P2_Left.png")
            elif self.dir ==1: self.image = pg.image.load("image/P2_Right.png")
            elif self.dir ==0: self.image = pg.image.load("image/P2_Up.png")
            elif self.dir ==2: self.image = pg.image.load("image/P2_Down.png")
            if self.sniper_mxtotal_am == 0:
                pg.mixer.Channel(1).play(pg.mixer.Sound("sound/get_bullets.wav"))
                self.weapon = "PISTOL"
                self.pistol_ammo = 15
                self.shot_delay = -1
            elif self.sniper_ammo == 0 and time.time() - self.last_shot > 0.3:
                pg.mixer.Channel(1).play(pg.mixer.Sound("sound/Sniper_reload.wav"))
                self.shot_delay = 4.3
                self.sniper_ammo = 7
            if time.time() - self.last_shot > self.shot_delay:
                challenger_bullet = Sniper_Bullet()
                challenger_bullet.rect.x = self.rect.x
                challenger_bullet.rect.y = self.rect.y
                challenger_bullet.dir = self.game.challenger.dir
                if self.shot_delay == -1:
                    self.shot_delay = 0.4
                else:
                    self.shot_delay = challenger_bullet.delay
                self.game.all_sprites.add(challenger_bullet)
                self.game.challenger_bullets.add(challenger_bullet)
                pg.mixer.Channel(1).play(pg.mixer.Sound("sound/Sniper.wav"))
                self.sniper_ammo -= 1
                self.sniper_mxtotal_am -=1
                self.last_shot = time.time()

        elif self.weapon == "BAZOOKA":
            if self.dir ==3: self.image = pg.image.load("image/P2_Left.png")
            elif self.dir ==1: self.image = pg.image.load("image/P2_Right.png")
            elif self.dir ==0: self.image = pg.image.load("image/P2_Up.png")
            elif self.dir ==2: self.image = pg.image.load("image/P2_Down.png")
            if self.bazook_mxtotal_am == 0:
                pg.mixer.Channel(1).play(pg.mixer.Sound("sound/get_bullets.wav"))
                self.weapon = "PISTOL"
                self.pistol_ammo = 15
                self.shot_delay = -1
            if time.time() - self.last_shot > self.shot_delay:
                challenger_bullet = Bazooka()
                challenger_bullet.rect.x = self.rect.x
                challenger_bullet.rect.y = self.rect.y
                challenger_bullet.dir = self.game.challenger.dir
                if self.shot_delay == -1:
                    self.shot_delay = 0.4
                else:
                    self.shot_delay = challenger_bullet.delay
                self.game.all_sprites.add(challenger_bullet)
                self.game.challenger_bullets.add(challenger_bullet)
                pg.mixer.Channel(1).play(pg.mixer.Sound("sound/Bazooka.wav"))
                self.bazook_mxtotal_am -= 1
                self.last_shot = time.time()

    def reload(self):
        if self.weapon == "PISTOL" :
            pg.mixer.Channel(0).play(pg.mixer.Sound("sound/pistol_reload.wav"))
            self.last_shot = time.time()
            self.shot_delay = 2
            self.pistol_ammo = 15
        elif self.weapon == "RIFLE" :
            if self.rifle_mxtotal_am != self.rifle_ammo:
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/get_bullets.wav"))
                self.last_shot = time.time()
                self.shot_delay = 4
                self.rifle_ammo = 30
        elif self.weapon == "SHOTGUN" :
            if self.shotgun_mxtotal_am != self.shotgun_shells:
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/shot_reload.wav"))
                self.last_shot = time.time()
                self.shot_delay = 4
                self.shotgun_shells = 8
        elif self.weapon == "SNIPER" :
            if self.sniper_mxtotal_am != self.sniper_ammo:
                pg.mixer.Channel(0).play(pg.mixer.Sound("sound/Sniper_reload.wav"))
                self.last_shot = time.time()
                self.shot_delay = 4.3
                self.sniper_ammo = 7

    def get_weapon(self,weapon_num):
        self.shot_delay = 0
        self.pistol_ammo = 15
        if weapon_num is 1:
            self.rifle_ammo =30
            self.rifle_mxtotal_am = 90
            self.speed = 130
            self.weapon = "RIFLE"
        if weapon_num is 2:
            self.speed = 150
            self.shotgun_mxtotal_am = 24
            self.shotgun_shells = 8
            self.weapon = "SHOTGUN"
        if weapon_num is 3:
            self.speed = 110
            self.weapon = "BAZOOKA"
        if weapon_num is 4:
            pg.mixer.Channel(1).play(pg.mixer.Sound("sound/getHP.wav"))
            self.health = PLAYER_HEALTH
        if weapon_num is 5:
            self.sniper_ammo = 7
            self.sniper_mxtotal_am = 21
            self.speed = 120
            self.weapon = "SNIPER"

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def draw_health(self):
        if self.health > 60:
            col = GREEN
        elif self.health > 30:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.health / CHALLENGER_HEALTH)
        self.health_bar = pg.Rect(0,0,width,2)
        if self.health <= CHALLENGER_HEALTH:
            pg.draw.rect(self.image, col, self.health_bar)



    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        if self.health <= 0:
            self.game.challenger_killed = True #플레이어2의 사망을 Game클래스에 알림
        self.image = self.image



class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, image):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        image_path = "image/" + image + ".png"
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE




class Pistol_Bullet(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([3,3])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.dir = 0
        self.bullet_speed = 10
        self.delay = 0.4
        self.damage = 11
    def update(self):
        if self.dir == 0:
            self.rect.y -= self.bullet_speed
        elif self.dir == 1:
            self.rect.x += self.bullet_speed
        elif self.dir == 2:
            self.rect.y += self.bullet_speed
        elif self.dir == 3:
            self.rect.x -= self.bullet_speed

class Rifle_Bullet(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([3,3])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.dir = 0
        self.bullet_speed = 13
        self.delay = 0.1
        self.damage = 15
    def update(self):
        if self.dir == 0:
            self.rect.y -= self.bullet_speed
        elif self.dir == 1:
            self.rect.x += self.bullet_speed
        elif self.dir == 2:
            self.rect.y += self.bullet_speed
        elif self.dir == 3:
            self.rect.x -= self.bullet_speed


class Shotgun_Bullet(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([3,3])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.dir = 0
        self.bullet_speed = 10
        self.bullet_spread = 0
        self.delay = 1
        self.damage = 9
    def update(self):
        if self.dir == 0:
            self.rect.y -= self.bullet_speed
            self.rect.x += self.bullet_spread
        elif self.dir == 1:
            self.rect.x += self.bullet_speed
            self.rect.y += self.bullet_spread
        elif self.dir == 2:
            self.rect.y += self.bullet_speed
            self.rect.x += self.bullet_spread
        elif self.dir == 3:
            self.rect.x -= self.bullet_speed
            self.rect.y += self.bullet_spread

class Sniper_Bullet(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.dir = 0
        self.image = pg.Surface([5,5])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.bullet_speed = 20
        self.delay = 1.5
        self.damage = 120
    def update(self):
        if self.dir == 0:
            self.rect.y -= self.bullet_speed
        elif self.dir == 1:
            self.rect.x += self.bullet_speed
        elif self.dir == 2:
            self.rect.y += self.bullet_speed
        elif self.dir == 3:
            self.rect.x -= self.bullet_speed

class Bazooka(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.dir = 0
        self.image = pg.image.load("image/Bazooka.png")
        self.rect = self.image.get_rect()
        self.bullet_speed = 10
        self.delay = 4
        self.damage = 200
    def update(self):
        if self.dir == 0:
            self.rect.y -= self.bullet_speed
        elif self.dir == 1:
            self.rect.x += self.bullet_speed
        elif self.dir == 2:
            self.rect.y += self.bullet_speed
        elif self.dir == 3:
            self.rect.x -= self.bullet_speed

class Explode(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("image/explode.png")
        self.rect = self.image.get_rect()
        self.damage = 30


class Item(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("image/BOX.png")
        self.rect = self.image.get_rect()
        self.speed = 1
    def update(self):
        self.rect.y += self.speed

class Box(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.box
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([5, 5])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.game = game



