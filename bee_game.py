import pygame
import random 
#import * from pygame

pygame.init()

screen_width = 600
screen_height = 800
screen = pygame.display.set_mode(screen_width,screen_height)
pygame.display.set_caption("Prevent the bees from getting to the cupcakes")

#loading images
bee = pygame.image.load("bee.png")
cupcake = pygame.image.load("cupcake.png")
character = pygame.image.load("plant.png")
bg = pygame.image.load("wood.jpg")
grass = pygame.image.load("grass.png")

#variables for the game
game_over = False 
running = True 
lives = 3
score = 0 

class Bee(pygame.sprite.Sprite):
    def __init__(self):
        self.image = bee
        self.image = pygame.transform.scale(self.image(100,100))
        self.rect = self.image.get_rect()



