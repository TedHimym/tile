import pygame
from pygame.locals import *
import shape
from sys import exit
import copy
import random
import util

class board(object):
	def __init__(self, screen, size, W, H):
		self.W = W
		self.H = H
		self.grade = 0
		self.size = size
		self.act_shape = []
		self.start_pos = [self.W/2-1, 0]
		self.START = (100, 100)
		self.screen = screen
		self.tile_list = []
		self.ground_flage = False
		self.can_t_move = False
		self.text = util.text(size=80)
		self.is_over = False
	def change_pos(self, commond):
		can_t_move = False
		not_hit = True
		unable_pos_list, not_act_tile = self.check()
		if commond == 'down':
			self.ground_flage = self.act_shape.fall_down_one_step(self.H)
		elif (commond =='right') or (commond=='left'):
			can_t_move = self.act_shape.left_and_right(commond)
		elif (commond == 'down_drect'):
			while True:
				for act_tile_each in self.act_shape.get_tile():
					if (act_tile_each.get_pos() in unable_pos_list) or self.ground_flage or can_t_move:
						self.act_shape.up_one_step()
						return
				self.ground_flage = self.act_shape.fall_down_one_step(self.H)
			self.check_row()
			self.draw_rect(-1)

		for act_tile_each in self.act_shape.get_tile():
			if (act_tile_each.get_pos() in unable_pos_list) or self.ground_flage or can_t_move:
				if commond == 'down':
					self.act_shape.up_one_step()
					self.new()
					return
				elif commond == 'right':
					self.act_shape.left_and_right('left')
					return
				elif commond == 'left':
					self.act_shape.left_and_right('right')
					return

	def change_poise(self):
		provious_act_shape = copy.deepcopy(self.act_shape.get_tile())
		unable_pos_list, not_act_tile = self.check()
		can_t_move = self.act_shape.change_poise()
		for act_tile_each in self.act_shape.get_tile():
			if (act_tile_each.get_pos() in unable_pos_list) or can_t_move:
				for i in range(len(provious_act_shape)):
					self.act_shape.get_tile()[i].set_pos_local(provious_act_shape[i].get_pos())
				return

	def check(self):
		not_act_tile_pos = []
		not_act_tile = []
		act_tile_list = self.act_shape.get_tile()
		for each_tile in self.tile_list:
			if each_tile not in act_tile_list:
				not_act_tile_pos.append(each_tile.get_pos())
				not_act_tile.append(each_tile)
		for pos in not_act_tile_pos:
			if pos[1] <= 0:
				self.is_over = True
		return not_act_tile_pos, not_act_tile

	def check_row(self):
		count = []
		for i in range(0, self.H):
			count.append(0)
		list_pos, list_tile = self.check()
		for each_pos in list_pos:
			for i in range(0, self.H):
				if each_pos[1] == i:
					count[i] += 1
		for i in range(self.H):
			if count[i] >= self.W:
				for tile in list_tile:
					if tile.get_pos()[1] == i:
						self.tile_list.remove(tile)
				self.grade += 1
		for i in range(self.H):
			if count[i] >= self.W:
				for tile in list_tile:
					if tile.get_pos()[1] <= i:
						tile.set_pos('down')
	def new(self):
		shape_num = random.randint(0, 4)
		if shape_num == 0:
			self.act_shape = shape.line(self.start_pos, self.W, self.H, self.size)
		elif shape_num == 1:
			self.act_shape = shape.rect(self.start_pos, self.W, self.H, self.size)
		elif shape_num == 2:
			self.act_shape = shape.line_with_point_up(self.start_pos, self.W, self.H, self.size)
		elif shape_num == 3:
			self.act_shape = shape.line_with_point_down(self.start_pos, self.W, self.H, self.size)
		elif shape_num == 4:
			self.act_shape = shape.Z_shape_right(self.start_pos, self.W, self.H, self.size)
		elif shape_num == 5:
			self.act_shape = shape.Z_shape_left(self.start_pos, self.W, self.H, self.size)
		self.add_tile()

	def add_tile(self):
		act_tile = self.act_shape.get_tile()
		for tile in act_tile:
			self.tile_list.append(tile)

	def _get_rect(self):
		rect_list = []
		for tile in self.tile_list:
			pos = tile.get_pos()
			rect = Rect(pos[0]*self.size, pos[1]*self.size, self.size, self.size)
			rect_list.append(rect)
		return rect_list

	def draw_rect(self, count):
		for each_tile in self.tile_list:
			each_tile.draw_rect(self.screen)
		if count < 0:
			return
		text_surface_grade = self.text.render(str(self.grade), True, (20, 50, 90))
		text_surface_time = self.text.render(str(count), True, (20, 50, 90))
		self.screen.blit(text_surface_grade, (self.W*self.size*1.5, self.H*self.size*(0.382)))
		self.screen.blit(text_surface_time, (self.W*self.size*1.5, self.H*self.size*(0.618)))

