import pygame
from pygame.locals import *
from sys import exit
from main import main
from menu import menu

class game(object):
	def __init__(self):
		self.W = 12
		self.H = 20
		self.size = 40
		self.screen = pygame.display.set_mode((self.W*self.size*2, self.H*self.size))
		self.clock = pygame.time.Clock()
		self.main = main(self.screen)
		self.menu = menu(self.screen)
		self.menu_flage = True

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					return
				if event.type == MOUSEBUTTONDOWN:
					if (self.menu_flage and self.menu.click_button(event.pos)):
						self.main.run()
				else:
					pass
			self.menu.draw(self.screen)
			pygame.display.update()

if __name__ == '__main__':
	A = game()
	A.run()