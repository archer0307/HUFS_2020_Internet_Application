import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *
from pygame.locals import *
import time

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.music.load("sound/BackgroundSound.mp3")
        pg.mixer.music.play(1)
        # self.screen1 = pg.display.set_mode((WIDTH, HEIGHT+10), FULLSCREEN | HWSURFACE | DOUBLEBUF)
        # self.screen2 = pg.display.set_mode((WIDTH, HEIGHT + 10), FULLSCREEN | HWSURFACE | DOUBLEBUF)
        self.screen1 = pg.display.set_mode((WIDTH, HEIGHT+10))
        self.screen2 = pg.display.set_mode((WIDTH, HEIGHT+10))
        pg.display.set_caption("Battle Grounds 2D")
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.pkcount = 0 #플레이어1 킬수
        self.ckcount = 0 #플레이어2 킬수
        self.player_killed = False
        self.player_suicide = False
        self.challenger_killed = False
        self.challenger_suicide = False
        self.running = True
        self.start_image = pg.image.load("image/start2.png").convert()
        self.control_image = pg.image.load("image/control.png").convert()
        self.win1_image = pg.image.load("image/win1.png").convert()
        self.win2_image = pg.image.load("image/win2.png").convert()

        map_num = random.randint(0, 2)

        if map_num == 0: self.filename = "city.txt"
        if map_num == 1: self.filename = "desert.txt"
        if map_num == 2: self.filename = "forest.txt"

        self.load_data()

    def load_data(self): #데이터를 불러온다
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, self.filename))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.players = pg.sprite.Group()
        self.challengers = pg.sprite.Group()
        self.player_bullets = pg.sprite.Group()
        self.challenger_bullets = pg.sprite.Group()
        self.items = pg.sprite.Group() #랜덤한 아이템을 주는 아이템 상자
        self.box = pg.sprite.Group() #아이템이 떨어질 지점(빨간색으로 표시되는 픽셀)
        self.player_explosions = pg.sprite.Group()
        self.challenger_explosions = pg.sprite.Group()
        self.p_last_ex = 0
        self.c_last_ex = 0
        self.ex_lasting_t = 0.04
        pg.font.init()  # you have to call this at the start,
        # if you want to use this module.


        if self.filename == "city.txt":
            for row, tiles in enumerate(self.map.data): #맵과 두플레이어 생성
                for col, tile in enumerate(tiles):
                    if tile == 'c': #벽생성
                        Wall(self, col, row,'c')
                    if tile == 'v': #벽생성
                        Wall(self, col, row,'v')
                    if tile == 'b': #벽생성
                        Wall(self, col, row,'b')
                    if tile == 'P': #플레이어1 스폰위치에 플레이어1 생성
                        self.player = Player(self, col, row)
                    if tile == 'C': #플레이어2 스폰위치에 플레이어2 생성
                        self.challenger = Challenger(self, col, row)
        if self.filename == "desert.txt":
            for row, tiles in enumerate(self.map.data): #맵과 두플레이어 생성
                for col, tile in enumerate(tiles):
                    if tile == 'a': #벽생성
                        Wall(self, col, row,'a')
                    if tile == 'g': #벽생성
                        Wall(self, col, row,'g')
                    if tile == 'h': #벽생성
                        Wall(self, col, row,'h')
                    if tile == 's': #벽생성
                        Wall(self, col, row,'s')
                    if tile == 'd':  # 벽생성
                        Wall(self, col, row, 'd')
                    if tile == 'f': #벽생성
                        Wall(self, col, row,'f')
                    if tile == 'P': #플레이어1 스폰위치에 플레이어1 생성
                        self.player = Player(self, col, row)
                    if tile == 'C': #플레이어2 스폰위치에 플레이어2 생성
                        self.challenger = Challenger(self, col, row)
        if self.filename == "forest.txt":
            for row, tiles in enumerate(self.map.data): #맵과 두플레이어 생성
                for col, tile in enumerate(tiles):
                    if tile == '0': #벽생성
                        Wall(self, col, row,'0')
                    if tile == '1': #벽생성
                        Wall(self, col, row,'1')
                    if tile == '2': #벽생성
                        Wall(self, col, row,'2')
                    if tile == '3': #벽생성
                        Wall(self, col, row,'3')
                    if tile == '4':  # 벽생성
                        Wall(self, col, row, '4')
                    if tile == '5': #벽생성
                        Wall(self, col, row,'5')
                    if tile == '6': #벽생성
                        Wall(self, col, row,'6')
                    if tile == '7': #벽생성
                        Wall(self, col, row,'7')
                    if tile == '8': #벽생성
                        Wall(self, col, row,'8')
                    if tile == '9': #벽생성
                        Wall(self, col, row,'9')
                    if tile == 't':  # 벽생성
                        Wall(self, col, row, 't')
                    if tile == 'P': #플레이어1 스폰위치에 플레이어1 생성
                        self.player = Player(self, col, row)
                    if tile == 'C': #플레이어2 스폰위치에 플레이어2 생성
                        self.challenger = Challenger(self, col, row)


        self.camera1 = Camera1(self.map.width, self.map.height)
        self.camera2 = Camera2(self.map.width, self.map.height)
        self.run()
        if self.pkcount >= 10: #10킬이상시 게임종료
            self.pkcount = 0
            self.ckcount = 0
            self.show_player1_win()
        elif self.ckcount >= 10:
            self.pkcount = 0
            self.ckcount = 0
            self.show_player2_win()

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        pKill = pg.font.SysFont('Comic Sans MS', 17)
        cKill = pg.font.SysFont('Comic Sans MS', 17)
        self.pKillText = pKill.render("Kills: "+str(self.pkcount)+"  Weapon: "+str(self.player.weapon), False, (0, 0, 0))
        self.cKillText = cKill.render("Kills: "+str(self.ckcount)+"  Weapon: "+str(self.challenger.weapon), False, (0, 0, 0))

        self.all_sprites.update()
        self.camera1.update(self.player)
        self.camera2.update(self.challenger)
        if self.pkcount >= 10: #10킬이상시 게임종료
            self.challenger_killed = False
            self.playing = False
        elif self.ckcount >= 10:
            self.player_killed = False
            self.playing = False


    def draw(self):
        # self.screen1.fill(BGCOLOR)
        if self.filename == "city.txt":
            self.screen1.fill(CITY)
        if self.filename == "desert.txt":
            self.screen1.fill(DESERT)
        if self.filename == "forest.txt":
            self.screen1.fill(FOREST)

        for sprite in self.all_sprites:
            if isinstance(sprite, Player):
                sprite.draw_health()
            if isinstance(sprite, Challenger):
                sprite.draw_health()

        for sprite in self.all_sprites:
            self.screen1.blit(sprite.image, self.camera1.apply(sprite))
            self.screen2.blit(sprite.image, self.camera2.apply(sprite))

        self.screen1.blit(self.pKillText, (16, 0))
        self.screen1.blit(self.cKillText, (528, 0))
        pg.display.flip()

    def events(self):
        # catch all events here
        if self.player_killed == True: #player 사망시 부활
            self.player_killed = False
            if self.player_suicide == False:
                self.ckcount += 1
            else:
                self.player_suicide = False
            for player in self.players:
                player.kill()
            for row, tiles in enumerate(self.map.data):
                for col, tile in enumerate(tiles):
                    if tile == 'P':
                        self.player = Player(self, col, row)
            self.player_killed = False

        if self.challenger_killed == True:#challenger 사망시 부활
            self.challenger_killed = False
            if self.challenger_suicide == False:
                self.pkcount += 1
            else:
                self.challenger_suicide = False
            for challenger in self.challengers:
                challenger.kill()
            for row, tiles in enumerate(self.map.data):
                for col, tile in enumerate(tiles):
                    if tile == 'C':
                        self.challenger = Challenger(self, col, row)
            self.challenger_killed = False

        if time.time() - self.p_last_ex > self.ex_lasting_t:
            for explosion in self.player_explosions:
                self.player_explosions.remove(explosion)
                self.all_sprites.remove(explosion)

        if time.time() - self.c_last_ex > self.ex_lasting_t:
            for explosion in self.challenger_explosions:
                self.challenger_explosions.remove(explosion)
                self.all_sprites.remove(explosion)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

        for player_ex in self.player_explosions:
            challenger_exd = pg.sprite.spritecollide(player_ex, self.challengers, False)
            suicide_p = pg.sprite.spritecollide(player_ex, self.players,False)
            for challenger in challenger_exd:
                challenger.health -= player_ex.damage
            for player in suicide_p:
                player.health -= player_ex.damage
                if player.health <= 0:
                    self.player_suicide = True

        for player_bullet in self.player_bullets:
            wall_hits = pg.sprite.spritecollide(player_bullet, self.walls, False)
            challenger_hits = pg.sprite.spritecollide(player_bullet, self.challengers, False)
            for wall in wall_hits:
                if type(player_bullet) is Bazooka:
                    explode = Explode()
                    explode.rect.centerx = player_bullet.rect.centerx
                    explode.rect.centery = player_bullet.rect.centery
                    if player_bullet.dir == 0:
                        explode.rect.y += 20
                    elif player_bullet.dir == 1:
                        explode.rect.x -= 20
                    elif player_bullet.dir == 2:
                        explode.rect.y -= 20
                    elif player_bullet.dir == 3:
                        explode.rect.x += 20
                    self.all_sprites.add(explode)
                    self.player_explosions.add(explode)
                    self.p_last_ex = time.time()
                self.player_bullets.remove(player_bullet)
                self.all_sprites.remove(player_bullet)
            for challenger in challenger_hits:
                if type(player_bullet) is Bazooka:
                    explode = Explode()
                    explode.rect.centerx = player_bullet.rect.centerx
                    explode.rect.centery = player_bullet.rect.centery
                    if player_bullet.dir == 0:
                        explode.rect.y += 20
                    elif player_bullet.dir == 1:
                        explode.rect.x -= 20
                    elif player_bullet.dir == 2:
                        explode.rect.y -= 20
                    elif player_bullet.dir == 3:
                        explode.rect.x += 20
                    self.all_sprites.add(explode)
                    self.player_explosions.add(explode)
                    self.p_last_ex = time.time()
                challenger.health -= player_bullet.damage
                self.player_bullets.remove(player_bullet)
                self.all_sprites.remove(player_bullet)

        for challenger_ex in self.challenger_explosions:
            player_exd = pg.sprite.spritecollide(challenger_ex, self.players, False)
            suicide_c = pg.sprite.spritecollide(challenger_ex, self.challengers, False)
            for player in player_exd:
                player.health -= challenger_ex.damage
            for challenger in suicide_c:
                challenger.health -= challenger_ex.damage
                if challenger.health <= 0:
                    self.challenger_suicide = True

        for challenger_bullet in self.challenger_bullets:
            wall_hits = pg.sprite.spritecollide(challenger_bullet, self.walls, False)
            player_hits = pg.sprite.spritecollide(challenger_bullet, self.players, False)
            for wall in wall_hits:
                if type(challenger_bullet) is Bazooka:
                    explode = Explode()
                    explode.rect.centerx = challenger_bullet.rect.centerx
                    explode.rect.centery = challenger_bullet.rect.centery
                    if challenger_bullet.dir == 0:
                        explode.rect.y += 20
                    elif challenger_bullet.dir == 1:
                        explode.rect.x -= 20
                    elif challenger_bullet.dir == 2:
                        explode.rect.y -= 20
                    elif challenger_bullet.dir == 3:
                        explode.rect.x += 20
                    self.all_sprites.add(explode)
                    self.challenger_explosions.add(explode)
                    self.c_last_ex = time.time()
                self.challenger_bullets.remove(challenger_bullet)
                self.all_sprites.remove(challenger_bullet)
            for player in player_hits:
                if type(challenger_bullet) is Bazooka:
                    explode = Explode()
                    explode.rect.centerx = challenger_bullet.rect.centerx
                    explode.rect.centery = challenger_bullet.rect.centery
                    if challenger_bullet.dir == 0:
                        explode.rect.y += 20
                    elif challenger_bullet.dir == 1:
                        explode.rect.x -= 20
                    elif challenger_bullet.dir == 2:
                        explode.rect.y -= 20
                    elif challenger_bullet.dir == 3:
                        explode.rect.x += 20
                    self.all_sprites.add(explode)
                    self.challenger_explosions.add(explode)
                    self.c_last_ex = time.time()
                player.health -= challenger_bullet.damage
                self.challenger_bullets.remove(challenger_bullet)
                self.all_sprites.remove(challenger_bullet)

        for item in self.items:
            arrival_hits = pg.sprite.spritecollide(item, self.box, False)
            player_took = pg.sprite.spritecollide(item, self.players,False)
            challenger_took = pg.sprite.spritecollide(item, self.challengers, False)
            if arrival_hits:
                item.rect.y = arrival_hits[0].rect.top - item.rect.height
                item.speed = 0
                for box in arrival_hits:
                    self.box.remove(box)
                    self.all_sprites.remove(box)
            if item.speed == 0:
                for player in player_took: #1P가 박스 획득시
                    self.items.remove(item)
                    self.all_sprites.remove(item)
                    weapon_num = random.randint(0,5)
                    for player in self.players:
                        player.get_weapon(weapon_num)
                for challenger in challenger_took: #2P가 박스 획득시
                    self.items.remove(item)
                    self.all_sprites.remove(item)
                    weapon_num = random.randint(0, 5)
                    for challenger in self.challengers:
                        challenger.get_weapon(weapon_num)


    def show_start_screen(self):
        start = True
        pg.display.init()
        while start:
            for event in pg.event.get():
                # print(event)
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        start = False
                    elif event.key == pg.K_q:

                        pg.quit()
                        quit()

            self.screen1.blit(self.start_image, [0,0])

            self.button("play", 580, 280, 280, 40, LIGHTGREY, YELLOW2, action="play")
            self.button("controls", 580, 340, 280, 40, LIGHTGREY, YELLOW2, action="controls")
            self.button("quit", 580, 400, 280, 40, LIGHTGREY, YELLOW2, action="quit")

            pg.display.update()

    def show_player1_win(self):
        player1_win = True

        while player1_win:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            self.screen1.blit(self.win1_image, [0, 0])

            self.button2("play", 270, 370, 110, 50, LIGHTGREY, YELLOW2, action="play")
            self.button2("controls", 470, 370, 110, 50, LIGHTGREY, YELLOW2, action="controls")
            self.button2("quit", 670, 370, 110, 50, LIGHTGREY, YELLOW2, action="quit")

            pg.display.update()

    def show_player2_win(self):
        player2_win = True

        while player2_win:
            for event in pg.event.get():
                # print(event)
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            self.screen1.blit(self.win2_image, [0, 0])

            self.button2("play", 270, 370, 110, 50, LIGHTGREY, YELLOW2, action="play")
            self.button2("controls", 470, 370, 110, 50, LIGHTGREY, YELLOW2, action="controls")
            self.button2("quit", 670, 370, 110, 50, LIGHTGREY, YELLOW2, action="quit")

            pg.display.update()


    def game_controls(self):
        gcont = True

        while gcont:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            self.screen1.blit(self.control_image, [0, 0])

            self.button("play", 580, 280, 280, 40, LIGHTGREY, YELLOW2, action="play")
            self.button("main", 580, 340, 280, 40, LIGHTGREY, YELLOW2, action="main")
            self.button("quit", 580, 400, 280, 40, LIGHTGREY, YELLOW2, action="quit")

            pg.display.update()



    def draw_text(self, text,  size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen1.blit(text_surface, text_rect)

    def text_to_button(self, msg, size,color,  x, y):
        self.draw_text(msg, size, color, x, y)

    def button(self,text, x, y, width, height, inactive_color, active_color, action=None):
        cur = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if x + width > cur[0] > x and y + height > cur[1] > y:
            pg.draw.rect(self.screen1, active_color, (x, y, width, height))
            if click[0] == 1 and action != None:
                if action == "quit":
                    pg.quit()
                    quit()

                if action == "controls":
                    self.game_controls()

                if action == "play":
                    pg.mixer.music.stop()
                    self.new()

                if action == "main":
                    self.show_start_screen()

        else:
            pg.draw.rect(self.screen1, inactive_color, (x, y, width, height))

        self.text_to_button(text, 28, WHITE, x+140, y)

    def button2(self,text, x, y, width, height, inactive_color, active_color, action=None):
        cur = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        # print(click)
        if x + width > cur[0] > x and y + height > cur[1] > y:
            pg.draw.rect(self.screen1, active_color, (x, y, width, height))
            if click[0] == 1 and action != None:
                if action == "quit":
                    pg.quit()
                    quit()

                if action == "controls":
                    self.player1_win = False
                    self.player2_win = False
                    self.game_controls()

                if action == "play":
                    self.player1_win = False
                    self.player2_win = False
                    self.game_controls()

                if action == "main":
                    self.player1_win = False
                    self.player2_win = False
                    self.show_start_screen()

        else:
            pg.draw.rect(self.screen1, inactive_color, (x, y, width, height))

        self.text_to_button(text, 25, WHITE, x+55, y+5)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        waiting = False
                    if event.key == pg.K_ESCAPE:
                        self.quit()
# create the game object
g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
