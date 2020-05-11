import pygame


bullet_imgs = []
bullet_img_list = ["./ibox/bullet_left.png", "./ibox/bullet_right.png"]


for img in bullet_img_list:
    bullet_imgs.append(pygame.image.load(img))

class Bullet(pygame.sprite.Sprite):

    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        if self.direction == 0:
            self.image = bullet_imgs[0]
            self.image = pygame.transform.scale(bullet_imgs[0], (22, 22))

        else:
            self.image = bullet_imgs[1]
            self.image = pygame.transform.scale(bullet_imgs[1], (22, 22))

        self.rect = self.image.get_rect()
        self.speedx = 10

    def update(self):
        if self.direction == 0:
            self.rect.x -= self.speedx
        else:
            self.rect.x += self.speedx
        # # kill if it moves off the top of the screen
        # if self.rect.left < 0:
        #     self.kill()