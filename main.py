import pygame
from constants import *
from player import *
from asteroidfield import *
def main():
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    field = AsteroidField()
    while True:
        # Allows player to quit program via pygame interface.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        updatable.update(dt)
        # Collision checks are implemented here.
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if shot.collision_check(asteroid):
                    asteroid.split()
                    shot.kill()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)
if __name__ == "__main__":
    main()
