background_image_filename = '/home/sachin/Desktop/background.jpg'
mouse_image_filename = '/home/sachin/Desktop/Helloworld.png'
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((600, 428), 0, 32)

pygame.display.set_caption("Hello, World!")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0,0))
    x, y = pygame.mouse.get_pos()
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    screen.blit(mouse_cursor, (x, y))
    pygame.display.update()
