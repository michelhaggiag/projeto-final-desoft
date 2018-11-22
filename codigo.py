# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:50:18 2018

@author: miche
"""

import pygame.locals
import sys
from pygame.locals import *
from random import randrange

preto=(0,0,0)
branco=(225,225,225)
altura = 800
largura = 600

# ===============      CLASSES      ===============
gameDisplay = pygame.display.set_mode((largura,altura))

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
        
class Inimigos(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y,vel_x,vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.vx = vel_x
        self.vy = vel_y
    def update(self):     
        self.rect.x += self.vx
        if self.rect.x >= 750 or self.rect.x <= 0:
            self.rect.y +=40
            self.vx = -self.vx
        elif self.rect.y == nave.rect.y:
            nave.kill()
            inimigo1.kill()
            inimigo2.kill()
            
class vidas(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(self.image, (23, 23))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

#class tiro_inimigo:
#    def__init__(self,pos_x,pos_y)
def text_objects(text, font):
    textSurface = font.render(text, True, branco)
    return textSurface, textSurface.get_rect()

relogio = pygame.time.Clock()

 
 
# ===============   INICIALIZAÇÃO   ===============        
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Space Invaders')



fundo = pygame.image.load("800x600.jpg").convert()

nave = nave("nave2.png",0.05,480,10)
nave_group = pygame.sprite.Group()
nave_group.add(nave)

tiro_group = pygame.sprite.Group()
inimigo_group = pygame.sprite.Group()

lista = []
for k in range(10):
    lista.append(k*10)
for i in lista:
    inimigo1 = Inimigos('ini3.PNG',(i*10),15,(8.5),(0))
    inimigo_group.add(inimigo1)
    
lista2 = []
for k in range(10):
    lista2.append(k*10)
for i in lista2:
    inimigo2 = Inimigos('ini3.PNG',(i*10),120,(8.5),(0))
    inimigo_group.add(inimigo2)
    
#lista3 = []
#for k in range(10):
#    lista3.append(k*10)
#for i in lista3:
#    inimigo2 = Inimigos('ini3.PNG',(i*10),225,(8),(0))
#    inimigo_group.add(inimigo2)
#    
score=0
#inimigo3 = Inimigos('inimigo3.PNG',(900),(100),(10),(10))
#tiro = Tiro('tiro.jpg',((nave.rect.x)+57),((nave.rect.y)+40),-10)
#tiro_group.add(tiro)

def Pontuacao(score):
    fonte = pygame.font.SysFont(None, 25)
    texto = fonte.render("Score: "+str(score),True, branco)
    tela.blit(texto,(0,0))
    
def tela_inicial():
    
    tela.blit(pygame.image.load("Untitled.png").convert(), (0, 0))     
    #largeText = pygame.font.SysFont('PressStart2P', 55)
    #largeText2 = pygame.font.SysFont('PressStart2P', 15)
    #TextSurf, TextRect = text_objects("Space Invaders", largeText)
    #TextSurf2, TextRect2 = text_objects("(Pressione qualquer tecla para continuar)", largeText2)
    #TextRect.center = (((altura/2)),(largura/2))
    #TextRect2.center = (((altura/2)),((largura/2)+65))      
    #gameDisplay.blit(TextSurf, TextRect)
    #gameDisplay.blit(TextSurf2, TextRect2)
    pygame.display.update()
    relogio.tick(30)






#def make_enemies_shoot(self):
#    if (time.get_ticks() - self.timer) > 700:
#        inimigo1 = self.enemies.random_bottom()
#        if inimigo1:
#            self.enemyBullets.add(
#                Tiro(inimigo1.rect.x + 14, .rect.y + 20, 1, 5,
#                           'enemylaser', 'center'))
#            self.allSprites.add(self.tiro)
#            self.timer = time.get_ticks()

# ===============   LOOPING PRINCIPAL   ===============




estado=0


rodando = True
while rodando:
    tempo = relogio.tick(30)
    pressed_keys = pygame.key.get_pressed() 
    for event in pygame.event.get():
    # Verifica se o evento atual é QUIT (janela fechou).
        if event.type == QUIT:
            # Neste caso, marca o flag rodando como False, 
            # para sair do loop de jogo.
            rodando = False
    if estado == 0:
        if any(pressed_keys):
            estado = 1
        tela_inicial()
        
    elif estado == 1:
  
        if pygame.sprite.groupcollide(tiro_group, inimigo_group, True, True, collided = None):
            score+=1
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
    #    if inimigo1.rect.x > 675:
    #        inimigo1.rect.x = 675 
    #        inimigo1.rect.y += 35
    #        inimigo1.vx = -10
    #    elif inimigo1.rect.x < 0:
    #        inimigo1.rect.x = 0
    #        inimigo1.rect.y+=35
    #        inimigo1.vx = 10
    #    if inimigo1.rect.y > 420:
    #        nave.kill()
    #        inimigo1.kill()
    #    elif inimigo1.rect.y > 530:
    #        inimigo1.kill()
    #    if inimigo2.rect.y > 530:
    #        nave.kill()
    #        inimigo1.kill()
    #        inimigo2.kill()
            
        tiro_group.update()
        inimigo_group.update()
    
        
        
            
        
    # Check the list of colliding sprites, and add one to the score for each one
        #for block in inimigo_group_list:
         #   score +=1 
        
    
            
    #    tiro.move()
    #    nave.move()
    
        # === FIM DA SEGUNDA PARTE ===
    
        # === TERCEIRA PARTE: GERA SAÍDAS (pinta tela, etc) ===
    
        # Pinta a imagem de fundo na tela auxiliar.
        tela.blit(fundo, (0, 0))                
        Pontuacao(score)
        
        nave_group.draw(tela)
        tiro_group.draw(tela)
        inimigo_group.draw(tela)
    
        # Troca de tela na janela principal.
        pygame.display.update()
    
        # === FIM DA TERCEIRA PARTE ===
        # Agora volta para o início do loop e faz mais um passo do jogo.
pygame.display.quit()
#
