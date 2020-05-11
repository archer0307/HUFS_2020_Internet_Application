import pygame
from pygame import *

def play(sound):
    pygame.init()

    pygame.mixer.music.load("./image/start/start_music.mp3")
    pygame.mixer.music.set_volume(sound)
    pygame.mixer.music.play(-1)
