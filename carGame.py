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
display_width = 950
display_height = 700

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
SmartCarImage = [pygame.image.load(path.join(assets + '/newcar0_opt.png')),pygame.image.load(path.join(assets + '/newcar2_opt.png')),pygame.image.load(path.join(assets + '/newcar3_opt.png'))]
RivalCarImage =pygame.image.load(path.join(assets + '/Black_viper_opt.png'))
Boom =pygame.image.load(path.join(assets + '/exp.png'))
# Game windown, caption initialised
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Game icon init
pygame.display.set_caption('SmartCar')
pygame.display.set_icon(gameIcon)

# Clock init for Frames
clock = pygame.time.Clock()

# Fonts Init
smallfont = pygame.font.SysFont("comicsansms", 15)
mediumfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 60)

# Engine sound added
pygame.mixer.music.load(path.join(extras, "engine_sound.mp3"))
pygame.mixer.music.play(-1)	

# smart car image function
def carImage(x,y, which):
	gameDisplay.blit(SmartCarImage[which], (x,y))

# rival car image function
def rivalcarImage(x,y):
 	gameDisplay.blit(RivalCarImage, (x,y))

# function to init all game assets!
def init():
	grassSlip = 0

	grass_width = 170
	grass_height = 700

	# Road and Greenland seperator
	border_width = 30
	border_height = 700

	# Game basic design init [Left side] & [Right side]
	gameDisplay.fill(black)
	pygame.draw.rect(gameDisplay, grey, (grass_width, 0, border_width, border_height))
	pygame.draw.rect(gameDisplay, grey, (display_width - grass_width - border_width, 0, border_width, border_height))

	for x in range(0,12):
		gameDisplay.blit(grassRoad, (0, grassSlip))
		gameDisplay.blit(grassRoad, (780, grassSlip))
		grassSlip = grassSlip + 63

	# Road under maintainance, be safe!
	gameDisplay.blit(stripOne, (380,0))
	gameDisplay.blit(stripTwo, (560,0))
	pygame.display.update()

def Score(score):
	pygame.draw.rect(gameDisplay, green, (0,0, 170,45))
	text = smallfont.render("Score : " + str(score), True, darkBlue)
	gameDisplay.blit(text, [10,10])

def gameloop():

	global FPS
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

	# carImage Position
	carX = 225
	carY = 560
	rcarX= [225,415,605]
	rcarY= 0
	a=b=c=rcarY
	# car change variable
	which_car = 0

	# Picturising car image, sorry SmartCar image
	carImage(carX,carY, which_car)
	change_x = 0

	rivalcarImage(rcarX[0],rcarY)

	# Heart starts beating, Don't stop it!
	while gameplay:
		
		if which_car == 2:
			which_car = 0
		else:
			which_car += 1

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameplay = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					change_x = 190
				if event.key == pygame.K_LEFT:
					change_x = -190	
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					change_x = 0

		init()
		# changing position of SmartCar
		carX += change_x
		if (carX<=700 and carX>=205):
			carImage(carX, carY, which_car)
		else:
			carX -= change_x
			carImage(carX, carY, which_car)

		# controlling movements of traffic
		if score>10:
			rivalcarImage(rcarX[0],a)
			a +=20
			if a>random.randint(1000, 2000):
				a=0
		if score>32:
			rivalcarImage(rcarX[1],b)
			b +=20
			if b>random.randint(1000, 2000):
				b=0
		if score>75:
			rivalcarImage(rcarX[2],c)
			c +=20
			if c>random.randint(1700, 2000):
				c=0

		if (carX == rcarX[0] and 470 < a <700):
			gameDisplay.blit(Boom, (carX,530))

		elif (carX == rcarX[1] and 470 < b <700):
			gameDisplay.blit(Boom, (carX,530))

		elif (carX == rcarX[2] and 470 < c <700):
			gameDisplay.blit(Boom, (carX,530))

		# Updating Score
		Score(score)
	 	score = score + 1

		if Divider == True:
			gameDisplay.blit(stripTwo, (380, 0))
			gameDisplay.blit(stripOne, (560, 0))
			Divider = False
		else:
			gameDisplay.blit(stripOne, (380, 0))
			gameDisplay.blit(stripTwo, (560, 0))
			Divider = True

		pygame.display.update()

		clock.tick(FPS)
		if not score % 2000:
			FPS += 1

	# You will win, try one more time. Don't Quit.
	pygame.quit()

	# you can signoff now, everything looks good!
	quit()
	
gameloop()