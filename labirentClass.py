# -*- coding: utf-8 -*-

# Kütüphaneler
import pygame
import random

# Modüller
import config
from düğümClass import Düğüm
from labirentFonksiyonlar import duvarSil, matrixDönüştür
from depthFirstFonksiyonlar import dfs

class Labirent:
    def __init__(self, ekran, seed, x, y, sütunSayısı, satırSayısı, düğümBoyutu, düğümDuvarBoyutu):
        self.ekran = ekran
        self.seed = seed
        self.x = x
        self.xBaşlangıç = x
        self.y = y
        self.yBaşlangıç = y
        self.sütunSayısı = sütunSayısı
        self.satırSayısı = satırSayısı
        self.düğümBoyutu = düğümBoyutu
        self.düğümDuvarBoyutu = düğümDuvarBoyutu
        
        random.seed(self.seed)
        self.renk = (random.randint(15, 235), random.randint(15, 235), random.randint(15, 235))
        
        self.düğümler = [Düğüm(self, sütunSayısı, satırSayısı, düğümBoyutu, düğümDuvarBoyutu)
        for satırSayısı in range(self.satırSayısı)
        for sütunSayısı in range(self.sütunSayısı)
        ]
        
        self.labirentlerTamamlandı = False
        self.oluşumStack = []
        
        self.font = pygame.font.Font('./fontlar/mvboli.ttf', 48)
        self.bulunanNokta = self.düğümler[0]
        self.yolBul = False
        self.başlangıçDüğümü = -1
        self.bitişDüğümü = -1
    
    def pozisyonDeğiştir(self, x, y):
        self.x = x
        self.y = y
    
    def labirentiOluştur(self):
        if not self.labirentlerTamamlandı:
            self.bulunanNokta.gidildi = True
            self.bulunanNokta.düğümüÇiz(self.ekran, tuple(min(255, i + 50) for i in self.renk))
            
            sonrakiDüğüm = self.bulunanNokta.komşuSeç()
            if sonrakiDüğüm:
                sonrakiDüğüm.gidildi = True
                self.oluşumStack.append(self.bulunanNokta)
                duvarSil(self.bulunanNokta, sonrakiDüğüm)
                self.bulunanNokta = sonrakiDüğüm
            elif self.oluşumStack:
                self.bulunanNokta = self.oluşumStack.pop()
                if not self.oluşumStack:
                    self.labirentlerTamamlandı = True
                    self.gameState = 1
    
    def labirentiÇiz(self, seed = -1, çizge = False):
        for düğüm in self.düğümler:
            renk = self.renk
            if düğüm in self.oluşumStack:
                renk = config.renkAçıkGri
            
            düğüm.düğümüÇiz(self.ekran, renk, çizge)
        
        if (seed != -1):
            text = self.font.render('#' + str(seed), True, config.renkSiyah)
            textRect = text.get_rect()
            textRect.center = (self.x + 300, self.y - 30)
            self.ekran.blit(text, textRect)
    
    def labirentiÇöz(self):
        for düğüm in self.düğümler:
            düğüm.gidildiDFS = False
        yol = dfs(matrixDönüştür(self.düğümler, self.satırSayısı, self.sütunSayısı), self.başlangıçDüğümü, self.bitişDüğümü)
        
        if (yol):
            for i in yol:
                x = i % self.sütunSayısı
                y = i // self.sütunSayısı
                self.düğümler[y * self.sütunSayısı + x].gidildiDFS = True