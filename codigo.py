# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:50:18 2018

@author: miche
"""

import pygame.locals
import sys
from pygame.locals import *
from random import randrange

# ===============      CLASSES      ===============
class nave(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x):
        pygame.sprite.Sprite.__init__(self)

        self.vx = vel_x
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def move(self):
        self.rect.x += self.vx
    
class Inimigos(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y,vel_x,vel_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y    
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
class Tiro(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y,vel_y):
        pygame.sprite.Sprite.__init__(self)        
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y 
        self.vy = vel_y
    
    def update(self):
        self.rect.y += self.vy
        
relogio = pygame.time.Clock()
    
        
# ===============   INICIALIZAÇÃO   ===============        
pygame.init()

tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Space Invaders')

altura = 800
largura = 600

fundo = pygame.image.load("800x600.jpg").convert()

nave = nave("nave2.png",0.05,480,10)
nave_group = pygame.sprite.Group()
nave_group.add(nave)

inimigo1 = Inimigos('inimigo.PNG',(nave.rect.x),(nave.rect.y),(1),(1))
#inimigo3 = Inimigos('inimigo3.PNG',(900),(100),(10),(10))
#tiro = Tiro('tiro.jpg',((nave.rect.x)+57),((nave.rect.y)+40),-10)
#tiro_group.add(tiro)
tiro_group = pygame.sprite.Group()
# ===============   LOOPING PRINCIPAL   ===============

rodando = True
while rodando:
    tempo = relogio.tick(30)

    # === PRIMEIRA PARTE: LIDAR COM EVENTOS ===

    # Para cada evento não-processado na lista de eventos:
    for event in pygame.event.get():
        # Verifica se o evento atual é QUIT (janela fechou).
        if event.type == QUIT:
            # Neste caso, marca o flag rodando como False, 
            # para sair do loop de jogo.
            rodando = False
    pressed_keys = pygame.key.get_pressed() 
    if pressed_keys[K_RIGHT]:  
        nave.rect.x += 10
    elif pressed_keys[K_LEFT]:  
        nave.rect.x -= 10
    elif pressed_keys[K_SPACE]:
        tiro = Tiro('tiro.jpg',((nave.rect.x)+57),((nave.rect.y)+40),-10)
        tiro_group.add(tiro)
        for tiro in tiro_group:
            if tiro.rect.y > altura:
                tiro.kill()    
    if nave.rect.x > 675:
        if pressed_keys[K_RIGHT]:  
             nave.rect.x =675
#             tiro.rect.x =675
    elif nave.rect.x < 0:
        if pressed_keys[K_LEFT]:  
            nave.rect.x =0
#            tiro.rect.x =0
    tiro_group.update()
    

        
#    tiro.move()
#    nave.move()

    # === FIM DA SEGUNDA PARTE ===

    # === TERCEIRA PARTE: GERA SAÍDAS (pinta tela, etc) ===

    # Pinta a imagem de fundo na tela auxiliar.
    tela.blit(fundo, (0, 0))
    nave_group.draw(tela)
    tiro_group.draw(tela)

    # Troca de tela na janela principal.
    pygame.display.update()

    # === FIM DA TERCEIRA PARTE ===
    # Agora volta para o início do loop e faz mais um passo do jogo.

pygame.display.quit()

