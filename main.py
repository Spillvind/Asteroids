# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player

def main():
	pygame.init()

	updatable = pygame.sprite.Group()
	

	drawable = pygame.sprite.Group()
	

	Player.containers = (drawable, updatable)




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
		
		for drawables in drawable:
			drawables.draw(screen)

		updatable.update(dt)	
		pygame.display.flip()
		dt = clock.tick(60)/1000
if __name__ == "__main__":
		main()
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")






