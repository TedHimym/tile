import pygame
from pygame.locals import *

class tile(object):
	def __init__(self, pos, W=12, H=20, color=(60,60,90), size = 40):
		self.color = color;
		self.size = size;
		self.pos = pos;
		self.board_size_W = W;
		self.board_size_H = H;

	def get_pos(self):
		return self.pos

	def set_pos(self, commed):
		if commed == 'left':
			self.pos[0] -= 1
		elif commed == 'right':
			self.pos[0] += 1
		elif commed == 'down':
			self.pos[1] += 1
		elif commed == 'up':
			self.pos[1] -= 1
	def set_pos_local(self, set_pos):
		self.pos = set_pos
	def draw_rect(self, screen):
		rect = Rect(self.pos[0]*self.size, self.pos[1]*self.size, self.size, self.size)
		pygame.draw.rect(screen, self.color, rect)

class shape(object):
	def __init__(self, W=12, H=20):
		self.tile_list = []
		self.board_size_H = H
		self.board_size_W = W

	def left_and_right(self, commond):
		can_t_move = False
		if commond == 'left':
			for each_tile in self.tile_list:
				each_tile.set_pos('left')
				if each_tile.get_pos()[0] < 0:
					can_t_move = True
		elif commond == 'right':
			for each_tile in self.tile_list:
				each_tile.set_pos('right')
				if each_tile.get_pos()[0] > self.board_size_W-1:
					can_t_move = True
		return can_t_move

	def up_one_step(self):
		for each_tile in self.tile_list:
			each_tile.set_pos('up')

	def fall_down_one_step(self, H):
		gorund_flage = False
		for each_tile in self.tile_list:
			each_tile.set_pos('down')
			if each_tile.get_pos()[1] >= H:
				gorund_flage = True
		return gorund_flage

	def get_tile(self):
		return self.tile_list

	def fall_dwon(self):
		pass

class line(shape):
	def __init__(self, start_pos, W=12, H=20):
		shape.__init__(self, W, H)
		self.cur_poise = 0
		for i in range(4):
			base_tile = tile([start_pos[0]+i, start_pos[1]], W, H)
			self.tile_list.append(base_tile)
		self.centor_tile = self.tile_list[2]

	def change_poise(self, s='+1'):
		can_t_move = False
		self.cur_poise += int(s)
		if self.cur_poise >= 2:
			self.cur_poise = 0
		elif self.cur_poise <= -1:
			self.cur_poise = 1
		centor_pos = self.centor_tile.get_pos()
		if self.cur_poise == 0:
			for i in range(-1, 3):
				self.tile_list[i+1].set_pos_local([centor_pos[0]+i, centor_pos[1]])
		if self.cur_poise == 1:
			for i in range(-1, 3):
				self.tile_list[i+1].set_pos_local([centor_pos[0], centor_pos[1]+i])
		for tile in self.tile_list:
			pos = tile.get_pos()
			if pos[0]<0 or pos[0]>self.board_size_W:
				can_t_move = True
			if pos[1]<0 or pos[1]>self.board_size_H-1:
				can_t_move = True
		return can_t_move

class rect(shape):
	def __init__(self, start_pos, W=12, H=20):
		shape.__init__(self, W, H)
		for i in range(2):
			for j in range(2):
				base_tile = tile([start_pos[0]+i, start_pos[1]+j], W, H)
				self.tile_list.append(base_tile)
		self.centor_tile = self.tile_list[2]

	def change_poise(self, s='+1'):
		can_t_move = False
		return can_t_move
		
class line_with_point_down(shape):
	def __init__(self, start_pos, W=12, H=20):
		shape.__init__(self, W, H)
		self.cur_poise = 0
		for i in range(3):
			base_tile = tile([start_pos[0]+i, start_pos[1]], W, H)
			self.tile_list.append(base_tile)
		self.centor_tile = self.tile_list[0]
		self.tile_list.append(tile([start_pos[0], start_pos[1]+1], W, H))

	def change_poise(self, s='+1'):
		can_t_move = False
		self.cur_poise += int(s)
		if self.cur_poise >= 4:
			self.cur_poise = 0
		elif self.cur_poise <= -1:
			self.cur_poise = 1
		centor_pos = self.centor_tile.get_pos()
		if self.cur_poise == 0:
			for i in range(3):
				base_tile = self.tile_list[i].set_pos_local([centor_pos[0]+i, centor_pos[1]])
				self.tile_list[3].set_pos_local([centor_pos[0], centor_pos[1]+1],)
		elif self.cur_poise == 1:
			for i in range(3):
				base_tile = self.tile_list[i].set_pos_local([centor_pos[0], centor_pos[1]+i])
				self.tile_list[3].set_pos_local([centor_pos[0]-1, centor_pos[1]])
		elif self.cur_poise == 2:
			for i in range(3):
				base_tile = self.tile_list[i].set_pos_local([centor_pos[0]-i, centor_pos[1]])
				self.tile_list[3].set_pos_local([centor_pos[0], centor_pos[1]-1],)
		elif self.cur_poise == 3:
			for i in range(3):
				base_tile = self.tile_list[i].set_pos_local([centor_pos[0], centor_pos[1]-i])
				self.tile_list[3].set_pos_local([centor_pos[0]+1, centor_pos[1]],)
		for tile in self.tile_list:
			pos = tile.get_pos()
			if pos[0]<0 or pos[0]>self.board_size_W:
				can_t_move = True
			if pos[1]<0 or pos[1]>self.board_size_H-1:
				can_t_move = True
		return can_t_move

class line_with_point_up(shape):
	def __init__(self, start_pos, W=12, H=20):
		shape.__init__(self, W, H)
		self.cur_poise = 0
		for i in range(3):
			base_tile = tile([start_pos[0]+i, start_pos[1]], W, H)
			self.tile_list.append(base_tile)
		self.centor_tile = self.tile_list[0]
		self.tile_list.append(tile([start_pos[0], start_pos[1]-1], W, H))

	def change_poise(self, s='+1'):
		can_t_move = False
		self.cur_poise += int(s)
		if self.cur_poise >= 4:
			self.cur_poise = 0
		elif self.cur_poise <= -1:
			self.cur_poise = 1
		centor_pos = self.centor_tile.get_pos()
		if self.cur_poise == 0:
			for i in range(3):
				base_tile = self.tile_list[i].set_pos_local([centor_pos[0]+i, centor_pos[1]])
				self.tile_list[3].set_pos_local([centor_pos[0], centor_pos[1]-1],)
		elif self.cur_poise == 1:
			for i in range(3):
				base_tile = self.tile_list[i].set_pos_local([centor_pos[0], centor_pos[1]+i])
				self.tile_list[3].set_pos_local([centor_pos[0]+1, centor_pos[1]])
		elif self.cur_poise == 2:
			for i in range(3):
				base_tile = self.tile_list[i].set_pos_local([centor_pos[0]-i, centor_pos[1]])
				self.tile_list[3].set_pos_local([centor_pos[0], centor_pos[1]+1],)
		elif self.cur_poise == 3:
			for i in range(3):
				base_tile = self.tile_list[i].set_pos_local([centor_pos[0], centor_pos[1]-i])
				self.tile_list[3].set_pos_local([centor_pos[0]-1, centor_pos[1]],)
		for tile in self.tile_list:
			pos = tile.get_pos()
			if pos[0]<0 or pos[0]>self.board_size_W:
				can_t_move = True
			if pos[1]<0 or pos[1]>self.board_size_H-1:
				can_t_move = True
		return can_t_move