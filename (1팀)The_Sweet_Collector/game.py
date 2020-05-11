import pygame
import random
import menu as menu
from player import Player
from enemy import *
from bullet import Bullet

model = []

model.append({
    "player": (300, 200),
    "platform": (
        (160, 150, 320, 30),
        (160, 330, 320, 30),
        (-10, 420, 170, 30),
        (490, 420, 170, 30),
        (-10, 240, 170, 30),
        (490, 240, 170, 30),
        (0, 450, 290, 30),
        (350, 450, 290, 30)),
    "background" : "bar.png"
    })

SETTINGS = {
    'music_volume': 50,
    'sb_volume': 90,
    'fullscreen': False,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'jump': pygame.K_UP,
    'shoot' : pygame.K_SPACE
}

FPS = 30


class Platform (pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

class Sweet(pygame.sprite.Sprite):

    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./ibox/sweet/%s.png' % name)
        self.rect = self.image.get_rect()


class Mixer:

    def __init__(self, has_sound=False):
        self.has_sound = has_sound

        if has_sound:
            self.sb = {
                "jump": pygame.mixer.Sound("./sbox/jump.wav"),
                "crunch": pygame.mixer.Sound("./sbox/crunch.wav"),
                "flip": pygame.mixer.Sound("./sbox/flip.wav"),
                "no": pygame.mixer.Sound("./sbox/no.wav"),
                "shoot" : pygame.mixer.Sound("./sbox/shoot.wav")
            }

    def play_sb(self, name):
        if self.has_sound:
            self.sb[name].set_volume(SETTINGS["sb_volume"]/100.0)
            self.sb[name].play()

    def play_track(self):
        if self.has_sound:
            self.track.set_volume(SETTINGS["music_volume"]/100.0)
            self.track.play()

class Score:

    value = 0
    best = 0
    text = {}

    def __init__(self, game):
        self.game = game
        self.game.font = pygame.font.SysFont("consolas", 50)
        self.text = {
            "gameover": game.font.render("GAME OVER", 1, (255, 0, 0)),
            "txt_score": game.font.render("SCORE", 1, (255, 255, 255)),
            "txt_best": game.font.render("BEST", 1, (255, 255, 255)),
            "pause": game.font.render("PAUSE", 1, (0, 0, 255)),
        }

        self.surf = pygame.Surface([game.width, game.height/2])
        self.surf.set_alpha(128)
        self.surf.fill((0, 0, 0))

    def update(self):
        self.value += 1
        if self.value > self.best:
            self.best = self.value
        self.render_score()

    def reset(self):
        self.value = 0
        self.render_score()

    def render(self):
        self.text["gameover"] = self.game.font.render("GAME OVER", 1, (255, 255, 255))
        self.text["best"] = self.game.font.render(str(self.best), 1, (255, 255, 255))

    def render_score(self):
        self.text["score"] = self.game.font.render(str(self.value), 1, (255, 255, 255))

    def draw(self, screen):
        screen.blit(self.text["score"], (310, 0))

    def draw_resume(self, screen):
        offset = self.game.height / 3
        screen.blit(self.surf, (0, offset))

        screen.blit(self.text["gameover"], (180, offset + 20))
        screen.blit(self.text["txt_score"], (180, offset + 80))
        screen.blit(self.text["score"], (420, offset + 80))
        screen.blit(self.text["txt_best"], (180, offset + 140))
        screen.blit(self.text["best"], (420, offset + 140))

    def draw_pause(self, screen):
        offset = self.game.height / 3
        screen.blit(self.surf, (0, offset))

        screen.blit(self.text["pause"], (240, offset + 80))


class Game:

    width = 640
    height = 480
    map_ind = 0
    state = ""
    enemy_timer = 0
    enemy_next_timer = 0
    gameover_delay = 2000
    gameover_timer = 0


    def __init__(self):

        if SETTINGS["fullscreen"]:
            flags = pygame.FULLSCREEN
        else:
            flags = 0
        pygame.init()

        try:
            pygame.mixer.init()
            self.has_sound = True
        except:
            self.has_sound = False
        pygame.mouse.set_visible(0)

        # 실제화면
        self.screen = pygame.Surface([self.width, self.height])
        self.real_screen = pygame.display.set_mode([self.width, self.height], flags, 32)
        pygame.display.set_caption("The Sweet Collector")


        self.score = Score(self)

        # sweet 이미지 로딩
        self.sweet = {
            "sweet1": Sweet("sweet_1"),
            "sweet2": Sweet("sweet_2"),
            "sweet3": Sweet("sweet_3"),
            "sweet4": Sweet("sweet_4"),
            "sweet5": Sweet("sweet_5"),
            "sweet6": Sweet("sweet_6"),
            "sweet7": Sweet("sweet_7"),
        }

        self.mixer = Mixer(self.has_sound)
        # 게임 메뉴
        self.menu = menu.Menu(self)
        self.player = Player(self)

        self.menu.run()

    def init_game(self):
        # game player 값 초기화
        self.state = "play"
        self.player.rect.x, self.player.rect.y = self.player.start_pos
        self.sweet_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.enemy_list2 = pygame.sprite.Group()

        self.add_sweet(1)
        self.add_enemy()
        self.score.reset()
        self.enemy_next_timer = 2 + random.random()*10
        #게임시작될 때 배경음악재생
        self.music = pygame.mixer.Sound("./sbox/festival.wav")
        pygame.mixer.Sound.play(self.music)

    def run(self):
        # 메인 게임 루프
        self.map_load(self.map_ind)
        self.init_game()
        clock = pygame.time.Clock()

        running = True
        while running:
            dt = clock.tick(30)

            # 게임 오버될 때
            if self.state == "gameover":
                if self.gameover_timer < self.gameover_delay:
                    self.gameover_timer += dt
                    pygame.event.clear()
                else:
                    self.gameover_timer = 0
                    self.state = "waiting"
                #게임오버 될때 배경음악 중단
                pygame.mixer.Sound.stop(self.music)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.Sound.stop(self.music)
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.Sound.stop(self.music)
                        if self.state == "pause":
                            running = False
                        elif self.state == "play":
                            self.state = "pause"
                            self.draw()
                        elif self.state == "waiting":
                            self.state = "menu"
                            running = False
                    elif self.state == "waiting":
                        self.init_game()

                    elif self.state == "pause":
                        self.state = "play"
                        #puase상태에서 재시작할때 배경음악 다시 재생
                        pygame.mixer.Sound.play(self.music)


            if self.state == "play":
                # Enemy
                self.enemy_timer += dt / 600.0
                if self.enemy_timer >= self.enemy_next_timer:
                    self.enemy_next_timer = 2 + random.random()*5
                    self.enemy_timer = 0
                    self.add_enemy()

                key = pygame.key.get_pressed()

                if key[SETTINGS["left"]]:
                    self.player.move_left()
                if key[SETTINGS["right"]]:
                    self.player.move_right()
                if key[SETTINGS["jump"]]:
                    self.player.jump()
                if key[SETTINGS["shoot"]]:
                    #shooting 소리
                    self.mixer.play_sb("shoot")
                    #bullet_list 공백이 none일때 bullet생성
                    if self.bullet_list.empty() is None:
                        bullet = Bullet(self.player.direction)
                    #Player의 좌표를 받아 bullet의 좌표 지정함
                        bullet.rect.x = self.player.rect.x
                        bullet.rect.y = self.player.rect.y
                    #bullet 이미지
                        self.bullet_list.add(bullet)

                self.bullet_list.update()




                # 플레이어가 죽을 때
                if self.player.is_dead:
                    pygame.mixer.Sound.stop(self.music)
                    self.state = "gameover"
                    self.score.render()
                    self.draw()
                    self.player.reset()
                    self.score.reset()

                elif running:
                    self.player.update(dt / 1000., self)
                    for enemy in self.enemy_list:
                        enemy.update(dt / 1000., self)
                        if enemy.is_dead:
                            self.enemy_list.remove(enemy)
                    for enemy in self.enemy_list2:
                        enemy.update(dt / 1000., self)
                        if enemy.is_dead:
                            self.enemy_list2.remove(enemy)
                    self.draw()

            for bullet in self.bullet_list:

                #bullet이 enemy에 맞았는지 확인
                enemy_hit_list = pygame.sprite.spritecollide(bullet, self.enemy_list, True)
                enemy_hit_list2 = pygame.sprite.spritecollide(bullet, self.enemy_list2, False)

                # For each block hit, remove the bullet
                if enemy_hit_list:
                    #enemy,enemy1이 bullet에 맞았을 때 각각 리스트에서 지움
                    self.bullet_list.remove(bullet)
                    self.enemy_list.remove(bullet)

                if enemy_hit_list2:
                    #enemy2가 bullet에 맞았을 때 리스트에서 꺼내 속도를 줄임 ,enemy2는 bullet에 맞아도 죽지않음(유령)
                    enemy = enemy_hit_list2.pop()
                    enemy.dx = 80


                # bullet이 화면 밖으로 나갔을 때 제거
                if bullet.rect.x < -10:
                    self.bullet_list.remove(bullet)





    def draw(self):
        # background
        self.screen.blit(self.map_image, (0, 0))
        # score
        self.score.draw(self.screen)
        # player
        rect = self.player.anim_pos + (30, 30)
        pos = (self.player.rect.x, self.player.rect.y - 4)
        self.screen.blit(self.player.image, self.player.rect, rect)
        # sweet
        self.sweet_list.draw(self.screen)
        # enemy
        self.enemy_list.draw(self.screen)
        self.enemy_list2.draw(self.screen)
        #bullets
        self.bullet_list.draw(self.screen)

        if self.state == "gameover":
            self.score.draw_resume(self.screen)
        elif self.state == "pause":
            self.score.draw_pause(self.screen)

        self.real_screen.blit(self.screen, (0, 0))
        pygame.display.flip()

    def map_load(self, map_ind):
        self.block_list = pygame.sprite.Group()
        mod = model[self.map_ind]
        self.player.start_pos = mod["player"]

        for block in mod["platform"]:
            p = Platform(block[0], block[1], block[2], block[3])
            self.block_list.add(p)

        self.map_image = pygame.image.load('./ibox/%s' % mod["background"])

    def add_sweet(self, num):

        for ind in range(num):
            name = random.choice(list(self.sweet))
            sweet = self.sweet[name]
            sweet.rect.x = random.randint(2, 61) * 10
            sweet.rect.y = 100 + random.randint(0, 3) * 90
            self.sweet_list.add(sweet)

    def add_enemy(self):

        enemy = Enemy()
        self.enemy_list.add(enemy)

        #상태추가, 스코어가 3점이상이면 enemy,enemy1 중에 랜덤으로 발생,스코어가 5점이상이면 enemy,enemy1,enemy2 랜덤하게 발생
        if self.score.value>=5:
            state=random.randrange(3)
        elif self.score.value>=3:
            state=random.randrange(2)
        else:
            state = 0

        if state==0:
            enemy = Enemy()
            self.enemy_list.add(enemy)
        elif state==1:
            enemy = Enemy2()
            self.enemy_list.add(enemy)
        elif state==2:
            enemy = Enemy3()
            self.enemy_list2.add(enemy)


if __name__ == "__main__":

    game = Game()
    pygame.quit()