import pygame

pygame.init()

height = 480
width = 640
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pac Man")

pacman_img = pygame.image.load("tiamarcelle.png").convert_alpha()
pacman_img = pygame.transform.scale(pacman_img, (32,32))
pacman_rect = pacman_img.get_rect()
pacman_rect.topleft = (height // 2, width // 2)


speed = 5
direction = 0

rotations = {
   "right": 0,
   "left": 180,
   "up": 90,
   "down": -90
}







