# -*- coding: utf-8 -*-

# Kütüphaneler
import pygame
import random
from random import choice
from grafikFonksiyonlar import sinüsDalgası

# Modüller
import config

class Düğüm:
    def __init__(self, labirent, x, y, boyut, duvarBoyutu):
        self.labirent = labirent
        self.x = x
        self.çizimX = x
        self.y = y
        self.çizimY = y
        self.boyut = boyut
        self.duvarBoyutu = duvarBoyutu
        
        self.index = x + (y * self.labirent.sütunSayısı)
        self.duvarlar = {'üst': True, 'alt': True, 'sol': True, 'sağ': True}
        self.gidildi = False
        self.gidildiDFS = False
        self.başlangıçDüğümü = False
        self.bitişDüğümü = False
        
        random.seed(self.labirent.seed)
    
    def düğümüÇiz(self, ekran, renk, çizge = False):
        x = self.labirent.x + (self.çizimX * self.boyut)
        y = self.labirent.y + (self.çizimY * self.boyut)
        
        if (self.başlangıçDüğümü):
            renk = config.renkMavi
        elif (self.bitişDüğümü):
            renk = config.renkKırmızı
        elif ((self.labirent.yolBul) and (self.gidildiDFS)):
            renkDalga = sinüsDalgası(20, .001, pygame.time.get_ticks(), True)
            renk = tuple(min(255, i + renkDalga) for i in config.renkTuruncu)
        
        if (çizge):
            if not self.duvarlar['üst']:
                pygame.draw.line(ekran, pygame.Color(config.renkSiyah), (x + (self.boyut // 2) - (self.duvarBoyutu // 2), y + self.boyut // 4), (x + (self.boyut // 2) - (self.duvarBoyutu // 2), y + self.boyut // 4 - self.boyut // 2), self.duvarBoyutu)
            
            if not self.duvarlar['alt']:
                pygame.draw.line(ekran, pygame.Color(config.renkSiyah), (x + (self.boyut // 2) - (self.duvarBoyutu // 2), y + (self.boyut // 2) - (self.duvarBoyutu // 2)), (x + (self.boyut // 2) - (self.duvarBoyutu // 2), y + self.boyut // 4 + self.boyut), self.duvarBoyutu)
            
            if not self.duvarlar['sol']:
                pygame.draw.line(ekran, pygame.Color(config.renkSiyah), (x + self.boyut // 4, y + (self.boyut // 2) - (self.duvarBoyutu // 2)), (x + self.boyut // 4 - self.boyut // 2, y + (self.boyut // 2) - (self.duvarBoyutu // 2)), self.duvarBoyutu)
                
            if not self.duvarlar['sağ']:
                pygame.draw.line(ekran, pygame.Color(config.renkSiyah), (x + (self.boyut // 2) - (self.duvarBoyutu // 2), y + (self.boyut // 2) - (self.duvarBoyutu // 2)), (x + self.boyut // 4 + self.boyut, y + (self.boyut // 2) - (self.duvarBoyutu // 2)), self.duvarBoyutu)
            
            pygame.draw.circle(ekran, pygame.Color(renk), (x + (self.boyut // 2), y + (self.boyut // 2)), self.boyut // 4)
            pygame.draw.circle(ekran, pygame.Color(config.renkSiyah), (x + (self.boyut // 2), y + (self.boyut // 2)), self.boyut // 4, width = self.duvarBoyutu)
        else:
            if self.gidildi:
                pygame.draw.rect(ekran, pygame.Color(renk), (x, y, self.boyut, self.boyut))
            
            if self.duvarlar['üst']:
                pygame.draw.line(ekran, pygame.Color(config.renkSiyah), (x, y), (x + self.boyut, y), self.duvarBoyutu)
            
            if self.duvarlar['alt']:
                pygame.draw.line(ekran, pygame.Color(config.renkSiyah), (x + self.boyut, y + self.boyut), (x , y + self.boyut), self.duvarBoyutu)
            
            if self.duvarlar['sol']:
                pygame.draw.line(ekran, pygame.Color(config.renkSiyah), (x, y + self.boyut), (x, y), self.duvarBoyutu)
                
            if self.duvarlar['sağ']:
                pygame.draw.line(ekran, pygame.Color(config.renkSiyah), (x + self.boyut, y), (x + self.boyut, y + self.boyut), self.duvarBoyutu)
    
    def noktayiKontrolEt(self, x, y):
        if x < 0 or x > self.labirent.sütunSayısı - 1 or y < 0 or y > self.labirent.satırSayısı - 1:
            return False
        
        return self.labirent.düğümler[x + (y * self.labirent.sütunSayısı)] 
    
    def komşuSeç(self):
        komsular = []
        
        üsttekiKomşu = self.noktayiKontrolEt(self.x, self.y - 1)
        alttakiKomşu = self.noktayiKontrolEt(self.x, self.y + 1)
        soldakiKomşu = self.noktayiKontrolEt(self.x - 1, self.y)
        sağdakiKomşu = self.noktayiKontrolEt(self.x + 1, self.y)
        
        if (üsttekiKomşu and not üsttekiKomşu.gidildi):
            komsular.append(üsttekiKomşu)
        if (alttakiKomşu and not alttakiKomşu.gidildi):
            komsular.append(alttakiKomşu)
        if (soldakiKomşu and not soldakiKomşu.gidildi):
            komsular.append(soldakiKomşu)
        if (sağdakiKomşu and not sağdakiKomşu.gidildi):
            komsular.append(sağdakiKomşu)
        
        return choice(komsular) if komsular else False

    def mouseDüğümünÜzerinde(self):
        x = self.labirent.x + (self.çizimX * self.boyut)
        y = self.labirent.y + (self.çizimY * self.boyut)
        
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        
        return ((mouseX > x) and (mouseX < x + self.boyut) and (mouseY > y) and (mouseY < y + self.boyut))