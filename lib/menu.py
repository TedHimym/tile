import pygame
from pygame.locals import *
import util

class menu(object):
	def __init__(self, screen):
		self.screen = screen
		self.text = util.text(size=150)

	def draw(self, screen):
		screen.fill((255,255,255))
		rect = Rect(0, 100, 40*12*2, 400)
		pygame.draw.rect(self.screen, (20, 20, 20), rect)
		text_surface = self.text.render("Begin!!!!!", True, (20, 50, 90))
		screen.blit(text_surface, (40*6, 220))

	def click_button(self, pos):
		if (pos[1]>100) and (pos[1]<500):
			print 'but'
			return True
		if pos[1] > 100:
			return False