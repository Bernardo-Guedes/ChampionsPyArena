import pygame

pygame.init()
pygame.mixer.init()

# carregar som
som_ataque = pygame.mixer.Sound("sons/ataque1.wav")

# tocar som
som_ataque.play()

import pygame

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

som_ataque = pygame.mixer.Sound("ataque.wav")

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                som_ataque.play()

    tela.fill((30, 30, 30))
    pygame.display.update()
    clock.tick(60)

pygame.quit()