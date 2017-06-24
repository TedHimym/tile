import pygame
from pygame.locals import *
import shape
from sys import exit
import copy
import random

class board(object):
	def __init__(self, screen, size, W, H):
		self.W = W
		self.H = H
		self.size = size
		self.act_shape = []
		self.START = (100, 100)
		self.screen = screen
		self.tile_list = [shape.tile([10,11]), shape.tile([0,0]), shape.tile([3,6])]
		self.ground_flage = False
		self.can_t_move = False

	def change_pos(self, commond):
		can_t_move = False
		able_pos_list, not_act_tile = self.check()
		if commond == 'down':
			self.ground_flage = self.act_shape.fall_down_one_step(self.H)
		elif (commond =='right') or (commond=='left'):
			can_t_move = self.act_shape.left_and_right(commond)
		else:
			pass
		for act_tile_each in self.act_shape.get_tile():
			if (act_tile_each.get_pos() in able_pos_list) or self.ground_flage or can_t_move:
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
		able_pos_list, not_act_tile = self.check()
		can_t_move = self.act_shape.change_poise()
		for act_tile_each in self.act_shape.get_tile():
			if (act_tile_each.get_pos() in able_pos_list) or can_t_move:
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
					print count[i]
		for i in range(self.H):
			if count[i] >= self.W:
				for tile in list_tile:
					if tile.get_pos()[1] == i:
						self.tile_list.remove(tile)
		for i in range(self.H):
			if count[i] >= self.W:
				for tile in list_tile:
					if tile.get_pos()[1] <= i:
						tile.set_pos('down')
	def new(self):
		shape_num = random.randint(0, 3)
		if shape_num == 0:
			self.act_shape = shape.line([5,5], self.W, self.H)
		elif shape_num == 1:
			self.act_shape = shape.rect([5,5], self.W, self.H)
		elif shape_num == 2:
			self.act_shape = shape.line_with_point_up([5,5], self.W, self.H)
		elif shape_num == 3:
			self.act_shape = shape.line_with_point_down([5,5], self.W, self.H)
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

	def draw_rect(self):
		for each_tile in self.tile_list:
			each_tile.draw_rect(self.screen)

