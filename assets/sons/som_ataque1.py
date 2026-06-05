import pygame

pygame.init()
pygame.mixer.init()

# carregar som
som_ataque = pygame.mixer.Sound("sons/ataque1.wav")

# tocar som
som_ataque.play()