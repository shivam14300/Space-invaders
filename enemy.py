import pygame
from pygame.locals import *
import random
import time
from random import randint
import ship
from ship import *
import main_bullet
from main_bullet import *


class Enemy():

    def __init__(self, x, y, start_new):

        self.image = pygame.image.load("thanos.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.is_alive = 1
        self.time = 1
        self.life = 8
        self.start_new = start_new

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)

    def lifeTime(self):
        self.time += 1

    def giveTime(self):
        return self.time / 60
