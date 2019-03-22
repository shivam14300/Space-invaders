import pygame
from pygame.locals import *
import random
import time
from random import randint
import ship
from ship import *
import enemy
from enemy import *


class main_bullet():

    def __init__(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y
        self.is_alive = True


class Bullet(main_bullet):

    def __init__(self, x, y):

        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        main_bullet.__init__(self, x, y)

    def update(self):

        self.rect.y -= 5

        if self.rect.y < 0:
            self.is_alive = False

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)


class BBullet(main_bullet):

    def __init__(self, x, y):

        self.image = pygame.image.load("Bbullet.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        main_bullet.__init__(self, x, y)

    def update(self):

        self.rect.y -= 3

        if self.rect.y < 0:
            self.is_alive = False

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)
