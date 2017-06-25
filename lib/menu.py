import pygame
from pygame.locals import *
import util

class menu(object):
	def __init__(self, screen, size, W, H):
		self.size = size
		self.W = W
		self.H = H
		self.screen = screen
		self.text = util.text(size=100)

	def Begin(self, screen):
		screen.fill((255,255,255))
		rect = Rect(0, 100, self.W*self.size*2, 400)
		pygame.draw.rect(self.screen, (20, 20, 20), rect)
		text_surface = self.text.render("Begin!!!!!", True, (20, 50, 90))
		screen.blit(text_surface, (self.W*self.size*0.618-50, self.size*self.H*0.382))

	def click_button(self, pos):
		if (pos[1]>100) and (pos[1]<500):
			return True
		if pos[1] > 100:
			return False