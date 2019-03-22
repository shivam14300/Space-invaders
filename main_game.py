import pygame
from pygame.locals import *
import random
import time
from random import randint
import ship
from ship import *
import enemy
from enemy import *
import main_bullet
from main_bullet import *


score = 0
start = time.time()


class Game():

    def __init__(self):

        pygame.init()

        w, h = 1000, 1000
        self.screen = pygame.display.set_mode((w, h))

        pygame.mouse.set_visible(False)

        self.ship = Ship(self.screen.get_rect())

        self.enemies = []
        xpos = random.randint(1, 8)*100
        ypos = random.randint(1, 2)*100
        start_new = time.time()
        self.enemies.append(Enemy(xpos, ypos, start_new))

        font = pygame.font.SysFont("", 72)
        self.text_paused = font.render("PAUSED", True, (255, 0, 0))
        self.text_paused_rect = self.text_paused.get_rect(center=self.screen.get_rect().center)

    def run(self):
        global start
        global score
        clock = pygame.time.Clock()

        RUNNING = True
        PAUSED = False
        while RUNNING:

            clock.tick(60)
            font1 = pygame.font.SysFont("Comic Sans MS", 40)
            self.score_game = font1.render("score = {}".format(score), True, (255, 255, 255))   
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    RUNNING = False

                if event.type == KEYDOWN:
                    if event.key == K_q:
                        RUNNING = False

                    if event.key == K_p:
                        PAUSED = not PAUSED

                if not PAUSED:
                    self.ship.event_handler(event)

            if not PAUSED:

                self.ship.update()

                self.ship.bullet_detect_collison(self.enemies)

                for i in range(len(self.enemies)-1, -1, -1):
                    if not self.enemies[i].is_alive:
                        del self.enemies[i]

                self.ship.Bbullet_detect_collison(self.enemies)

                for i in range(len(self.enemies)-1, -1, -1):
                    end_time = time.time()
                    if self.enemies[i].is_alive == 0:
                        del self.enemies[i]
                        score += 1
                    elif end_time - self.enemies[i].start_new > self.enemies[i].life:
                        del self.enemies[i]

            self.screen.fill((0, 0, 0))

            self.ship.draw(self.screen)

            end = time.time()
            if end-start > 10:
                xpos = random.randint(1, 8) * 100
                ypos = random.randint(1, 2) * 100
                start_new = time.time()
                self.enemies.append(Enemy(xpos, ypos, start_new))
                start = time.time()

            for e in self.enemies:
                e.draw(self.screen)
            if PAUSED:
                self.screen.blit(self.text_paused, self.text_paused_rect)

            self.screen.blit(self.score_game, (0, 100))
            pygame.display.update()

        pygame.quit()

Game().run()
