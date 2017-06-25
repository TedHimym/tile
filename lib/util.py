import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode()

def text(path="../data/ITCKRIST.TTF", size = 50):
	text = pygame.font.Font(path, size)
	return text

tile_image = pygame.image.load("../data/tile_image.jpg").convert()

