import socket
import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):
		# socket
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Laberinto de Moustros')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# Cargar el sonido principal 
		main_sound = pygame.mixer.Sound('../audio/main.ogg')
		main_sound.set_volume(0.2)
		main_sound.play(loops = -1)
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()