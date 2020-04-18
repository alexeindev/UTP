import pygame

class link(pygame.sprite.Sprite()):
    self.hoja =pygame.image.load('C:\Users\SkyStay\Google Drive\UNIVERSIDAD\SEXTO SEMESTRE\CompuGrafica\player\linksprite.png')
    self.hoja.set_clip(pygame.Rect(0,0,88,88))
    self.imagen = self.hoja.subsurface(self.hoja.get_clip())
    self.rect = self.imagen.get_rect()
    self.rect.topleft = posicion
    self.figura = 0
    self.estados_der = {0: (0,0,88,88), 1: (88,0,88,88), 2:(176,0,88,88), 3:(264,0,88,88), 4:(352,0,88,88), }
    self.estados_izq = {0: (0,88,88,88), 1: (88,88,88,88), 2:(176,88,88,88), 3:(264,88,88,88), 4:(352,88,88,88), }
    self.estados_arr = {0: (0,176,88,88), 1: (88,176,88,88), 2:(176,176,88,88), 3:(264,176,88,88), 4:(352,176,88,88), }
    self.estados_abj = {0: (0,264,88,88), 1: (88,264,88,88), 2:(176,264,88,88), 3:(264,264,88,88), 4:(352,264,88,88), }

    
    def get_figura(self, estados):
        self.figura += 1
        if self.figura > (len(estados) - 1):
            self.figura = 0
        return estados[self.figura]
    
    def corte(self, rect_cortado):
        if type(rect_cortado) is dict:
            self.hoja.set_clip(pygame.Rect(self.get_figura(rect_cortado)))
        else:
            self.hoja.set_clip(pygame.Rect(rect_cortado))
        return rect_cortado 

    def actualizacion(self, direccion):
        if direccion == 'izq':
            self.corte(self.estados_izq)
            self.rect.x -= 5
        if direccion == 'der':
            self.corte(self.estados_der)
            self.rect.x += 5
        if direccion == 'arriba':
            self.corte(self.estados_arriba)
            self.rect.y -= 5
        if direccion == 'abajo':
            self.corte(self.estados_abajo)
            self.rect.y += 5

        if direccion == 'quieto_izq':
            self.corte(self.estados_izq[0])
        if direccion == 'quieto_der':
            self.corte(self.estados_der[0])
        if direccion == 'quieto_arriba':
            self.corte(self.estados_arriba[0])
        if direccion == 'quieto_abajo':
            self.corte(self.estados_abajo[0])
        
        self.imagen = self.hoja.subsurface(self.hoja.get_clip())
    
    def evento(self, event):
        if event.type == pygame.QUIT:
            game_over = True 

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.actualizacion('izq')
            if event.key == pygame.K_RIGHT:
                self.actualizacion('der')
            if event.key == pygame.K_UP:
                self.actualizacion('arriba')
            if event.key == pygame.K_DOWN:
                self.actualizacion('abajo')
        
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.actualizacion('quieto_izq')
            if event.key == pygame.K_RIGHT:
                self.actualizacion('quieto_der')
            if event.key == pygame.K_UP:
                self.actualizacion('quieto_arriba')
            if event.key == pygame.K_DOWN:
                self.actualizacion('quieto_abajo')