import pygame
pygame.int()
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Exemplo de jogo')
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((255,255,255))
    pygame.display.update()

pygame.quit()