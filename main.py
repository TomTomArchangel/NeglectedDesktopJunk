import pygame
import os
import time
import random
import math
import player_libary
import level_libary
screen = pygame.display.set_mode((800, 450))
pygame.init()

class HealthBar():
	def __init__(self, x, y, w, h, max_hp):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.hp = max_hp
		self.max_hp = max_hp

	def draw(self, surface):
		#calculate health ratio
		ratio = self.hp / self.max_hp
		pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
		pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

health_bar = HealthBar(200, 200, 400, 10, 100)
start_img = pygame.image.load('start_button.png').convert_alpha()

class Button:
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		
	def draw(self):
		screen.blit(self.image, (self.rect.x, self.rect.y))
		

start_button = Button(200, 0, start_img)

#game variables
level_counter = 1
run = True

#setting up the player name
playername = input("What is your name? -> ")
player1 = player_libary.player_Human(str(playername))
print("Hello " + playername + "!")


while run:
	screen.fill("indigo")
	#draw health bar
	health_bar.hp = 75
	health_bar.draw(screen)
	start_button.draw()
	pygame.display.flip()
    #check for exit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
