import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((500, 500))

def text(path="../data/ITCKRIST.TTF", size = 50):
	text = pygame.font.Font(path, size)
	return text

tile_image = pygame.image.load("../data/tile_image_lovelive.jpg").convert()

