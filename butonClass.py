# -*- coding: utf-8 -*-

# Kütüphaneler
import pygame

# Modüller
import config

class Buton:
    def __init__(self, ekran, x, y, genişlik, yükseklik, kenarBoyutu, hedefResim = -1, yazı = -1, hedefFont = './fontlar/GOTHIC.TTF', hedefPunto = 24):
        self.ekran = ekran
        self.x = x
        self.y = y
        self.genişlik = genişlik
        self.yükseklik = yükseklik
        self.kenarBoyutu = kenarBoyutu
        self.hedefResim = hedefResim
        self.yazı = yazı
        
        if (hedefResim != -1):
            self.resim = pygame.image.load(hedefResim).convert_alpha()
        
        if (yazı != -1):
            self.font = pygame.font.Font(hedefFont, hedefPunto)
            self.text = self.font.render(self.yazı, True, config.renkSiyah)
            self.textRect = self.text.get_rect()
            self.textRect.center = (self.x + (self.genişlik // 2), self.y + (self.yükseklik // 2))
    
    def butonÇiz(self):
        pygame.draw.rect(self.ekran, pygame.Color(config.renkBeyaz), (self.x, self.y, self.genişlik, self.yükseklik), border_radius = 8)
        pygame.draw.rect(self.ekran, pygame.Color(config.renkSiyah), (self.x, self.y, self.genişlik, self.yükseklik), width = self.kenarBoyutu, border_radius = 8)
        
        if (self.hedefResim != -1):
            self.ekran.blit(self.resim, (self.x,self.y))
        
        if (self.yazı != -1):
            self.ekran.blit(self.text, self.textRect)
    
    def mouseButonunÜzerinde(self):
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        
        return ((mouseX > self.x) and (mouseX < self.x + self.genişlik) and (mouseY > self.y) and (mouseY < self.y + self.yükseklik))