import board
import pygame
from pygame.locals import *

class main():
	def __init__(self):
		self.size = 40
		self.W = 12
		self.H = 20
		self.screen = pygame.display.set_mode((self.W*self.size, self.H*self.size))
		self.board = board.board(self.screen, self.size, self.W, self.H)
		self.clock = pygame.time.Clock()
		self.count = 0
 
	def run(self):
		self.board.new()
		while True:
			self.clock.tick(30)
			if self.count == 30:
				self.count = 0
				self.board.change_pos('down')
				self.board.check_row()

			self.screen.fill((255, 255, 255))
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_q:
						return
					elif event.key == K_LEFT:
						self.board.change_pos('left')
					elif event.key == K_RIGHT:
						self.board.change_pos('right')
					elif event.key == K_DOWN:
						self.board.change_pos('down')
					elif event.key == K_SPACE:
						self.board.change_poise()
				elif event.type == QUIT:
					return
			self.board.draw_rect()
			pygame.display.update()
			self.count += 1
			pass

if __name__ == '__main__':
	a = main()
	a.run()