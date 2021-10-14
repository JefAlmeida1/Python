#Desenvolva um programa para tocar audio de um arquivo mp3.

import pygame
pygame.initc()
pygame.mixer.load()
pygame.mixer.music.play()
pygame.event.wait()