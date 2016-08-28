# -*- coding: utf-8 -*-
# @Author: Amar Prakash Pandey
# @Date: 25-08-2016 
# @Email: amar.om1994@gmail.com  
# @Github username: @amarlearning 
# MIT License. You can find a copy of the License
# @http://amarlearning.mit-license.org

# import library here
import pygame
import time
import random
from os import path

# Material color init
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
grey = (211,211,211)

# Pygame module initialised 
pygame.init()

# Folder path init
assets = path.join(path.dirname(__file__), 'assets')
extras = path.join(path.dirname(__file__), 'extras')

# constants are defined
display_width = 700
display_height = 600

grass_width = 170
grass_height = 600

border_width = 30
border_height = 600

divider_width = 20
divider_height = 20

block = 40

# Frames per second
FPS = 5

# Init images & sounds
gameIcon = pygame.image.load(path.join(assets + '/gameicon.png'))
clock = pygame.time.Clock()

# Game windown, caption initialised
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SmartCar')

pygame.display.update()

# Game icon init
pygame.display.set_icon(gameIcon)
gameplay = True

# Heart starts beating, Don't stop it!
while gameplay:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameplay = False
		else:
			print event


	# Dividing th road, not the people 
	pygame.draw.rect(gameDisplay, white, ((display_width/2 - 10),20 + block,divider_width,divider_height))
	if(block == 40):
		block = 180
	else:
		block = 40

	# Game basic design init [Left side]
	pygame.draw.rect(gameDisplay, green, (0, 0, grass_width, grass_height))
	pygame.draw.rect(gameDisplay, grey, (grass_width, 0, border_width, border_height))

	# Game basic design init [Right side]
	pygame.draw.rect(gameDisplay, green, (display_width - grass_width, 0, grass_width, grass_height))
	pygame.draw.rect(gameDisplay, grey, (display_width - grass_width - border_width, 0, border_width, border_height))

	pygame.display.update()

	clock.tick(FPS)

# You will win, try one more time. Don't Quit.
pygame.quit()

# you can signoff now, everything looks good!
quit()
