import pygame
import random
import os
__file__ = os.path.abspath(__file__)

WIDTH = 800		# width of our game window
HEIGHT = 600	# height of our game window
FPS = 30		# frames per second

# set paths to game folder / directory
main_path = os.path.dirname(__file__)
# direct 'backgrounds' folder path
bkg_path = os.path.join(main_path, "backgrounds")
# direct menu folder path containing all menus
menu_path = os.path.join(main_path, "menu")
# direct music folder path for all music
music_path = os.path.join(main_path, "music")


# initialize and create window
pygame.init()
# pygame.init.font()
pygame.mixer.init()  # sound stuff
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Awesome Card Game")
clock = pygame.time.Clock()

# Color definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (28, 210, 28)
BLUE = (173, 216, 230)
RED = (255, 144, 144)

# default defined globals
solid_color_choice = WHITE
background_image_choice = False
selected_music = os.path.join(music_path, "Alexander Ehlers - Warped.mp3")

# Font definitions
font_size = 36
font_color = BLACK
font_color_selected = BLUE

# Game states
#	Menu
#		Playing
#			Pick Game (load)
#			Play Game (from chosen)
#			Pick Music
#			Quit
#		Development
#			New Game
#			Load Game
#	Win
#	Lose
#	Undo
#	AI Stuff (i.e. player 2)
#	Quit
#	High Score

def read_menu_file(menu_file):
	# load menu choices
	if (type(menu_file) == str):
		f = open(menu_file)
		menu_lines = f.readlines()
		f.close
		return menu_lines
	else:
		return menu_file

# Game Menu
def display_menu(menu_file):
	global solid_color_choice
	menu_on = True

	menu_lines = read_menu_file(menu_file)
	menu_choices = len(menu_lines)
	selected_menu_choice = 1

	# Actual text of menu item
	font = pygame.font.Font("VertigoFLF.ttf", font_size)
	menuTextSurf = font.render("menu display", True, font_color)
	menuTextRect = menuTextSurf.get_rect()

	# make loop
	# print("running menu")
	while menu_on:
		for event in pygame.event.get():
			# Quit option
			if event.type == pygame.QUIT:
				quit()
			
			# Options to go up or down in menu
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					selected_menu_choice += 1
				if event.key == pygame.K_UP:
					selected_menu_choice -= 1
				if event.key == pygame.K_RETURN:
					return selected_menu_choice

		# Ensure menu choice is not out of bounds
		selected_menu_choice = max(1, selected_menu_choice)
		selected_menu_choice = min(menu_choices, selected_menu_choice)
	
		# Display menu background
		set_game_background()

		# Setup location and display text of menu items
		menuTextRect.centerx = int(WIDTH/3)
		menuTextRect.centery = int(HEIGHT/4)
		
		for i in menu_lines:
			# display each line 1 lower than previous
			menuTextRect.centery += font_size
			# each i has a newline character that needs to be removed
			# change color if menu choice selected
			if(int(i[0:1]) == selected_menu_choice):
				menuTextSurf = font.render(i[:-1], True, font_color_selected)
			else:
				menuTextSurf = font.render(i[:-1], True, font_color)

			# Updates to screen display
			# TODO: do we need this to be within for loop
			screen.blit(menuTextSurf, menuTextRect)

		pygame.display.flip()
		clock.tick(60)


		# Menu Reaction to key strokes

def set_background_solid():
	global solid_color_choice
	# hardcode menu choices
	# 1. White (default)
	# 2. Green
	# 3. Blue
	# 4. Red
	solid_background_choice = display_menu(os.path.join(menu_path, "background_solid_choices.txt"))

	if (solid_background_choice == 1):
		solid_color_choice = WHITE
	elif (solid_background_choice == 2):
		solid_color_choice = GREEN
	elif (solid_background_choice == 3):
		solid_color_choice = BLUE
	elif (solid_background_choice == 4):
		solid_color_choice = RED

	# TODO: doublecheck WHITE functionality

	screen.fill(solid_color_choice)
	pygame.display.update()

def set_background_artwork():
	global background_image_choice
	global solid_color_choice

	# menu located in file
	artwork_background_choice = display_menu(os.path.join(menu_path, "background_artwork_choices.txt"))

	if (artwork_background_choice == 1):
		# if the choice is campfire
		background_image_choice = pygame.image.load(os.path.join(bkg_path, "campfire.png")).convert()
	elif (artwork_background_choice == 2):
		# if the choice is space
		background_image_choice = pygame.image.load(os.path.join(bkg_path, "space.jpg")).convert()
	elif (artwork_background_choice == 3):
		# if the choice is vikings
		background_image_choice = pygame.image.load(os.path.join(bkg_path, "vikings.png")).convert()

	print(background_image_choice)

	solid_color_choice = False
	screen.blit(background_image_choice, [0, 0])
	pygame.display.flip()

def set_game_background():
	global solid_color_choice
	global background_image_choice
	global font_color
	global font_color_selected

	if (solid_color_choice != False):
		screen.fill(solid_color_choice)
		background_image_choice = False
	else:
		screen.blit(background_image_choice, [0, 0])
		solid_color_choice = False

	if (solid_color_choice == WHITE):
		font_color = BLACK
		font_color_selected = BLUE
	else:
		font_color = BLACK
		font_color_selected = WHITE

def choose_music():
	global selected_music

	music_choice = display_menu(os.path.join(menu_path, "music_menu.txt"))

	# Warped (default)
	if (music_choice == 1):
		selected_music = os.path.join(music_path, "Alexander Ehlers - Warped.mp3")
	# Spacetime
	elif (music_choice == 2):
		selected_music = os.path.join(music_path, "Alexander Ehlers - Spacetime.mp3")
	# Twists
	elif (music_choice == 3):
		selected_music = os.path.join(music_path, "Alexander Ehlers - Twists.mp3")
	# Flags
	elif (music_choice == 4):
		selected_music = os.path.join(music_path, "Alexander Ehlers - Flags.mp3")

# Game Loop
running = True
while running:
	pygame.mixer.music.load(selected_music)
	pygame.mixer.music.play(-1)

	# Display menu
	game_state = display_menu(os.path.join(menu_path, "menu.txt"))

	# Games States - MUST align with what is in "menu.txt"
	#	1. Choose Game
	#	2. Play Game
	#	3. Choose Background
	#	4. Choose Music
	#	5. Create new Game (placeholder)
	#	6. Load Game to Edit (placeholder)
	#	7. Quit

	# Switch/case on game states above
	if (game_state == 1):
		print("choosing new game")
	elif (game_state == 2):
		print("playing new game")
	elif (game_state == 3):
		print("choosing background")
		background_choice = display_menu(os.path.join(menu_path, "background_menu.txt"))
		print(background_choice)
		if (background_choice == 1):
			set_background_solid()
		elif (background_choice == 2):
			set_background_artwork()
	elif (game_state == 4):
		print("picking music")
		choose_music()
	elif (game_state == 5):
		print("creating new game")
	elif (game_state == 5):
		print("loading game to edit")
	elif (game_state == 7):
		print("Quiting game")
		quit()

# Wait for input


# Game logic
# Win logic
# Lose logic
# menu logic

# Render

# Background color
# set_game_background()


# Refresh (after draw)
# pygame.display.flip()
