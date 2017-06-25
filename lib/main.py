import board
import pygame
from pygame.locals import *
 
class main():
	def __init__(self, screen,size, W, H):
		self.size = size
		self.W = W
		self.H = H
		self.screen = screen
		self.board = board.board(self.screen, self.size, self.W, self.H)
		self.clock = pygame.time.Clock()
		self.count = 0
 
	def run(self):
		self.board.new()
		while self.board.is_over != True:
			self.clock.tick(60)
			if self.count == 30:
				self.count = 0
				self.board.change_pos('down')
				self.board.check_row()

			self.screen.fill((255, 255, 255))
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_q:
						self.board.tile_list = []
						return
					elif event.key == K_LEFT:
						self.board.change_pos('left')
					elif event.key == K_RIGHT:
						self.board.change_pos('right')
					elif event.key == K_DOWN:
						self.board.change_pos('down_drect')
					elif event.key == K_SPACE:
						self.board.change_poise()
				elif event.type == QUIT:
					return
			self.board.draw_rect(self.count)
			pygame.display.update()
			self.count += 1
			pass

if __name__ == '__main__':
	a = main()
	a.run()