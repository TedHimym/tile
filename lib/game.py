import pygame
from pygame.locals import *
from sys import exit

clock = pygame.time.Clock()
speed = 290
distance = 0
x = 0

pygame.init()

for i in range(100):

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	clock.tick(10)
	t = clock.tick() / 1000
	distance = t * speed
	x += distance
	print x