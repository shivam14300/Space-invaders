import pygame
from pygame.locals import *
import random
import time
from random import randint
import enemy
from enemy import *
import main_bullet
from main_bullet import *


class Ship():

    def __init__(self, screen_rect):

        self.image = pygame.image.load("battleship.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.bottom = screen_rect.bottom
        self.rect.centerx = screen_rect.centerx

        self.move_x = 0

        self.shots = []
        self.shots_count = 0
        self.max_shots = 1000

        self.Bshots = []
        self.Bshots_count = 0
        self.max_Bshots = 1000

    def event_handler(self, event):

        if event.type == KEYDOWN:
            if event.key == K_a:
                self.move_x = -20
            elif event.key == K_d:
                self.move_x = 20
            elif event.key == K_s:
                if len(self.shots) < self.max_shots:
                    self.shots.append(Bullet(self.rect.centerx, self.rect.top))
            elif event.key == K_SPACE:
                if len(self.Bshots) < self.max_Bshots:
                    self.Bshots.append(BBullet(self.rect.centerx, self.rect.top))

        if event.type == KEYUP:
            if event.key in (K_a, K_d):
                self.move_x = 0

    def update(self):

        self.rect.x += self.move_x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 900:
            self.rect.x = 900

        for s in self.shots:
            s.update()

        for i in range(len(self.shots)-1, -1, -1):
            if self.shots[i].is_alive == 0:
                del self.shots[i]
        for s in self.Bshots:
            s.update()

        for i in range(len(self.Bshots)-1, -1, -1):
            if not self.Bshots[i].is_alive:
                del self.Bshots[i]

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)

        for s in self.shots:
            s.draw(screen)

        for s in self.Bshots:
            s.draw(screen)

    def bullet_detect_collison(self, enemy_list):

        for s in self.shots:
            for e in enemy_list:
                end = time.time()
                if pygame.sprite.collide_circle(s, e):
                    s.is_alive = False
                    e.life += 5
                    e.image = pygame.image.load("ww.png")
                    e.image = pygame.transform.scale(e.image, (150, 150))

    def Bbullet_detect_collison(self, enemy_list):

        for s in self.Bshots:
            for e in enemy_list:
                if pygame.sprite.collide_circle(s, e):
                    s.is_alive = False
                    e.is_alive = 0
