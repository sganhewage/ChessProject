#this is where the player does their inputs
#Initialize global directory of the images
import pygame
from Chess import ChessEngine

width = height = 748
dimension = 8
square_size = height//dimesnion
max_fps = 15
IMAGES = {}

def loadImages():
	pieces = ['wp', 'wR', 'wKn', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bKn', 'bB', 'bK', 'bQ',]
	for piece in pieces:
		IMAGES[piece] = pygame.transform.scale(pygame.image.load("Chess Graphics/chess board/chess pieces/" + piece + ".png"),(square_size, square_size))
		#we can access an image by saying "IMAGES['wp']"

#the main dirver of the code; handles user input and graphics updates
def main():
	# initialize pygame
	pygame.init()

	# define constants for the screen width and height
	screen_width = 1376
	screen_height = 768

	# create the screen object; size determined by screen_width and screen_height
	screen = pygame.display.set_mode((screen_width, screen_height))
	screen.fill(pygame.Color("white"))
	gs = ChessEngine.GameState()
	print(gs.board)

main()
