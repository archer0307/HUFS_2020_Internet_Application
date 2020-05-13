import pygame

class Menu:

    index = 0
    mode = "menu"

    def __init__(self, game):

        self.game = game
        self.image = pygame.image.load('./ibox/candybg.jpg')
        # 메뉴 선택하는 창의 높이 80으로 지정
        self.surf_ind = pygame.Surface([game.width, 80])
        self.surf_ind.set_alpha(128)
        self.surf_ind.fill((0, 0, 0))

        self.game_name = game.font.render("THE SWEET COLLECTOR", 1, (199, 21, 133))

        self.menu_items = [
            game.font.render("PLAY", 1, (255, 255, 255)),
            game.font.render("QUIT", 1, (255, 255, 255))
            ]


    def run(self):

        clock = pygame.time.Clock()

        running = True
        while running:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.mode == "menu":
                            running = False
                        else:
                            self.mode = "menu"
                            self.index = 0

                    elif event.key == pygame.K_UP:
                        if self.index > 0:
                            self.index -= 1
                    elif event.key == pygame.K_DOWN:
                        if self.index < 1:
                            self.index += 1
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:

                        # quit
                        if self.mode == "menu" and self.index == 1:
                            running = False
                        # play -> select map
                        elif self.mode == "menu" and self.index == 0:
                            self.game.run()

            if running:
                self.draw()

    def draw(self):
        # draw bg
        self.game.screen.blit(self.image, (0, 0))
        # 게임 이름의 위치 지정
        self.game.screen.blit(self.game_name, (50, 20))

        if self.mode == "menu":
            self.game.screen.blit(self.surf_ind, (0, self.index * 80 + 140))
            for ind in range(2):
                self.game.screen.blit(self.menu_items[ind], (250, 140 + ind * 80))

        self.game.real_screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()