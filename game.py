import pygame
import sys
import math
import random


pygame.init()

pygame.mixer.init(size=16, channels=2) #Inicializa Sound Mixer
pygame.mixer.set_num_channels(16) # Seta canais para 16
jump = pygame.mixer.Sound('jump.wav')
throw = pygame.mixer.Sound('throw.wav')
covid = pygame.mixer.Sound('covid.wav')

pygame.mixer.Sound.set_volume(jump, .2)
pygame.mixer.Sound.set_volume(throw, .2)
pygame.mixer.Sound.set_volume(covid, .4)

clock = pygame.time.Clock()

#Screen
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load('background.png').convert_alpha()

class Player():
    def __init__(self):
        self.playerimg = pygame.image.load("player.png").convert_alpha()
        self.player_x = 50
        self.player_y = 400

def main_loop():
    #fps
    clock.tick(80)

    player = Player()

    running = True
    while running:
        screen.blit(background, (0,0))
        screen.blit(player.playerimg, (player.player_x, player.player_y))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main_loop()