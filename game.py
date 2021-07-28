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
        self.is_jump = False
        self.jump_vel = 10
        self.jump_mass = 1


    #Movimenta player e define limites
    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.player_x < 720:
            self.player_x += 3
        if keys[pygame.K_LEFT] and self.player_x > 0:
            self.player_x -= 3

    #Pulo
    def jump_player(self):
        keys = pygame.key.get_pressed()
        if not self.is_jump:
            if keys[pygame.K_SPACE]:
                self.is_jump = True
                jump.play()

        if self.is_jump:
            # Verifica se o objeto atingiu a altura máxima
            if self.jump_vel < 0:
                self.jump_mass = -1
            #Calculo de força do pulo
            F = (1/2)*self.jump_mass*(self.jump_vel**2)
            self.player_y -= F
            self.jump_vel -= 1

            if self.jump_vel < -10:
                self.is_jump = False
                self.jump_vel = 10
                self.jump_mass = 1

player = Player()

class Seringa():
    def __init__(self):
        self.seringaimg = pygame.image.load("seringa.png").convert_alpha()
        self.seringa_x = player.player_x + 45
        self.seringa_y = player.player_y + 50
        self.throw = False

    def throw_seringa(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.throw = True
            throw.play()

        if not self.throw:
            self.seringa_x = player.player_x + 45
            self.seringa_y = player.player_y + 50
            self.throw = False

        else:
            self.seringa_x += 20
            if self.seringa_x > 850:
                self.seringa_x = player.player_x + 45
                self.seringa_y = player.player_y + 50
                self.throw = False      
            


seringa = Seringa()


def main_loop():
    # Main game loop
    
    running = True
    while running:
        # Fps
        clock.tick(80)


        # Handling Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # screen blits
        screen.blit(background, (0, 0))
        screen.blit(player.playerimg, (player.player_x, player.player_y))
        screen.blit(seringa.seringaimg, (seringa.seringa_x, seringa.seringa_y))

        # Class functions
        player.move_player()
        player.jump_player()
        seringa.throw_seringa()

        # refresh window
        pygame.display.update()


main_loop()