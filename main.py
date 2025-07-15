# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player

def main():
	pygame.init()

	updateable = pygame.sprite.Group()
	

	drawable = pygame.sprite.Group()
	

	Player.containers = (drawable, updateable)


	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	player = Player(x, y)
	clock = pygame.time.Clock()
	dt = 0
	print("Starting Asteroids!")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		player.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000
		player.update(dt)
if __name__ == "__main__":
		main()
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")






