# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:17:27 2019

@author: Stefan Draghici
"""

import pygame
import sys
import time
from pygame.locals import QUIT, KEYUP, KEYDOWN, K_ESCAPE, K_LEFT, K_RIGHT

BLUE=(0,0,155)
BOX_SIZE=20
SCREEN_WIDTH=640
SCREEN_HEIGHT=480
BOARD_WIDTH=10

def run_tetris_game():
	pygame.init()
	screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Tetris')
	game_matrix=create_game_matrix()
	last_time_piece_moved=time.time()
	piece=create_piece()
	
	while True:
		screen.fill((0,0,0))
		
		if(time.time()-last_time_piece_moved>1):
			piece['row']+=1
			last_time_piece_moved=time.time()
		draw_moving_piece(screen, piece)
		pygame.draw.rect(screen, BLUE, [100, 50, 210, 410], 5)
		draw_board(screen, game_matrix)
		draw_score(screen, score)
		listen_to_user_input(game_matrix, piece)
		
		if(piece['row']==19 or game_matrix[piece['row']+1][piece['column']]!='.'):
			game_matrix[piece['row']][piece['column']]='c'
			lines_removed=remove_completed_lines(game_matrix)
			score+=lines_removed
			piece=create_piece()
			
		pygame.display.update()
		
		for event in pygame.event.get(QUIT):
			pygame.quit()
			sys.exit()
            
            
def create_game_matrix():
    game_matrix_columns=10
    game_matrix_rows=20
    matrix=[]
    for row in range(game_matrix_rows):
        new_row=[]
        for column in range(game_matrix_columns):
            new_row.append('.')
        matrix.append(new_row)
    return matrix


def create_piece():
    piece={}
    piece['row']=0
    piece['column']=4
    return piece


def draw_moving_piece(screen, piece):
	draw_single_tetris_box(screen, piece['row'], piece['column'], (255, 255, 255), (217, 222, 226))
	
	
def draw_single_tetris_box(screen, matrix_cell_row, matrix_cell_column, color, shadow_color):
	origin_x=105+(matrix_cell_column*20+1)
	origin_y=55+(matrix_cell_row*20+1)
	pygame.draw.rect(screen, shadow_color, [origin_x, origin_y, 20, 20])
	pygame.draw.rect(screen, color, [origin_x, origin_y, 18, 18])
	
	
def draw_board(screen, matrix):
	game_matrix_columns=10
	game_matrix_rows=20
	
	for row in range(game_matrix_rows):
		for column in range(game_matrix_columns):
			if(matrix[row][column]!='.'):
				draw_single_tetris_box(screen, row, column, (255, 255, 255), (217, 222, 226))
				
				
def listen_to_user_input(game_matrix, piece):
	for event in pygame.event.get():
		if event.type==KEYDOWN:
			if event.key==K_LEFT and is_valid_position(game_matrix, piece['row'], piece['column']-1):
				piece['column']-=1
			elif event.key==K_RIGHT and is_valid_position(game_matrix, piece['row'], piece['column']+1):
				piece['column']+=1
				
				
def is_valid_position(game_matrix, row, column):
	if not column>=0 and column<10 and row<20:
		return False
	if game_matrix[row][column]!='.':
		return False
	else:
		return True


def draw_score(screen, score):
	font=pygame.font.Font('feesansbold.ttf', 18)
	score_surf=font.render('Score: ', score, True, (255, 255, 255))
	sreen.blit(score_surf, (640-150, 20))


def is_line_completed(game_matrix, row):
	for column in range(10):
		if game_matrix[row][column]=='.':
			return False
	return True
	
	
def remove_completed_lines(game_matrix):
	num_lines_removed=0
	for row in range(20):
		if is_line_completed(game_matrix, row):
			for row_to_move_down in range(row, 0, -1):
				for column in range(10):
					game_matrix[row_to_move_down][column]=game_matrix[row_to_move_down-1][column]
			for x in range(10):
				game_matrix[0][x]='.'
			num_lines_removed+=1
	return num_lines_removed
	
	
#run the game
run_tetris_game()