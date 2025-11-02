# this allows us to use code from
# the open-source pygame library
# throughout this file h
import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()

	updatable = pygame.sprite.Group()
	
	drawable = pygame.sprite.Group()

	asteroids = pygame.sprite.Group()

	shots = pygame.sprite.Group()
	

	Player.containers = (drawable, updatable)

	Asteroid.containers = (asteroids, updatable, drawable)

	AsteroidField.containers = (updatable,)

	asteroid_field = AsteroidField()

	Shot.containers = (shots,updatable, drawable)




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

		for asteroid in asteroids:
			if player.check_collision(asteroid):
				sys.exit("Game Over!")
		
if __name__ == "__main__":
		main()
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")






