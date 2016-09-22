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

# Pygame module initialised 
pygame.init()

# Material color init
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
grey = (211,211,211)

# Display width and height are defined
display_width = 700
display_height = 600

# Frames per second
FPS = 5

# Folder path init
assets = path.join(path.dirname(__file__), 'assets/image')
extras = path.join(path.dirname(__file__), 'extras')

# Init images & sounds
gameIcon = pygame.image.load(path.join(assets + '/gameicon.png'))
grassRoad = pygame.image.load(path.join(assets + '/grassslip.png'))
stripOne = pygame.image.load(path.join(assets + '/stripone.png'))
stripTwo = pygame.image.load(path.join(assets + '/striptwo.png'))
coverImage = pygame.image.load(path.join(assets + '/cover.png'))
SmartCarImage = pygame.image.load(path.join(assets + '/smartcar.png'))

# Game windown, caption initialised
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Game icon init
pygame.display.set_caption('SmartCar')
pygame.display.set_icon(gameIcon)

# Image transformation 
SmartCarImage = pygame.transform.rotate(SmartCarImage, 90)

# Clock init for Frames
clock = pygame.time.Clock()

# Fonts Init
smallfont = pygame.font.SysFont("comicsansms", 30)
mediumfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 60)

# Display updated
pygame.display.update()

def init():
	# Engine sound added
	menu_song = pygame.mixer.music.load(path.join(extras, "engine_sound.mp3"))
	pygame.mixer.music.play(-1)	

	grassSlip = 0

	grass_width = 170
	grass_height = 600

	# Road and Greenland seperator
	border_width = 30
	border_height = 600

	# Images position locations
	carLeftPosiitonX = 240
	carLeftPosiitonY = 480

	# Game basic design init [Left side] & [Right side]
	pygame.draw.rect(gameDisplay, grey, (grass_width, 0, border_width, border_height))
	pygame.draw.rect(gameDisplay, grey, (display_width - grass_width - border_width, 0, border_width, border_height))

	for x in range(0,10):
		gameDisplay.blit(grassRoad, (0, grassSlip))
		gameDisplay.blit(grassRoad, (530, grassSlip))
		grassSlip = grassSlip + 63

	# Picturising car image, sorry SmartCar image
	gameDisplay.blit(SmartCarImage, (carLeftPosiitonX,carLeftPosiitonY))
	gameDisplay.blit(stripOne, (340,0))
	pygame.display.update()

def Score(score):
	pygame.draw.rect(gameDisplay, green, (0,0, 170,45))
	text = smallfont.render("Score : " + str(score), True, darkBlue)
	gameDisplay.blit(text, [10,10])

def gameloop():
	# All necessary variable initalised
	init()
	# Kickstart variable
	gameplay = True
	score = 0
	# Grass 2D image & Road Divider
	Divider = True

	# Road's divider width and height
	divider_width = 20
	divider_height = 80

	# Images position locations
	carLeftPosiitonX = 240
	carLeftPosiitonY = 480
	carRightPosiitonX = 400
	carRightPosiitonY = 480

	# Heart starts beating, Don't stop it!
	while gameplay:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameplay = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					gameDisplay.blit(coverImage, (carLeftPosiitonX-40,carLeftPosiitonY))
					gameDisplay.blit(SmartCarImage, (carRightPosiitonX,carRightPosiitonY))
					pygame.display.update()
				if event.key == pygame.K_LEFT:
					gameDisplay.blit(coverImage, (carRightPosiitonX-40,carRightPosiitonY))
					gameDisplay.blit(SmartCarImage, (carLeftPosiitonX,carLeftPosiitonY))
					pygame.display.update()
			else:
				print event
		
		# Updating Score
		Score(score)
		score = score + 1

		if Divider == True:
			gameDisplay.blit(stripTwo, (340, 0))
			Divider = False
		else :
			gameDisplay.blit(stripOne, (340, 0))
			Divider = True

		pygame.display.update()

		clock.tick(FPS)

	# You will win, try one more time. Don't Quit.
	pygame.quit()

	# you can signoff now, everything looks good!
	quit()

gameloop()
