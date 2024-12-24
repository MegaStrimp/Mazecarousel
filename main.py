# -*- coding: utf-8 -*-

# Kütüphaneler
import pygame
import random
import sys

# Modüller
import config
from ekranSetup import uygulamaEkranı
from labirentClass import Labirent
from butonClass import Buton

# Fontlar
fontGothic36 = pygame.font.Font('./fontlar/GOTHIC.TTF', 36)
fontGothic48 = pygame.font.Font('./fontlar/GOTHIC.TTF', 48)
fontGothic48Bold = pygame.font.Font('./fontlar/GOTHICB.TTF', 48)

# Değişkenler
uygulamaDurumu = 0
durumBaşlat = True
mouseBasıldı = False
seedGirilebilir = False
girilenSeed = ''
başlangıçDüğümü = -1
başlangıçDüğümüSeçiliyor = False
bitişDüğümü = -1
bitişDüğümüSeçiliyor = False

while True:
    # Arka Planı Çiz
    uygulamaEkranı.fill(pygame.Color(config.renkBeyaz))
    
    for event in pygame.event.get():
        # Uygulamayı Kapat
        if (event.type == pygame.QUIT):
            pygame.quit();
            sys.exit()
        
        # Mouse'a Tıkla
        if (event.type == pygame.MOUSEBUTTONDOWN):
            mouseBasıldı = True
        
        # Klavyede Tuşa Bas
        if (event.type == pygame.KEYDOWN):
            if (seedGirilebilir):
                if (event.key == pygame.K_BACKSPACE):
                    girilenSeed = girilenSeed[:-1]
                elif (event.unicode.isdigit() and len(girilenSeed) < 6):
                    girilenSeed += event.unicode
    
    match uygulamaDurumu:
        # Ana Menü
        case 0:
            if (durumBaşlat):
                # Değişkenler
                durumBaşlat = False
                
                # Butonları Yarat
                başlatButonu = Buton(uygulamaEkranı, 320, 300, 150, 50, 2, -1, 'BAŞLAT')
                
                # Görselleri ve Yazıları Oluştur
                logo = pygame.image.load('./görseller/BeykozLogo.png').convert_alpha()
                logo = pygame.transform.scale(logo, (140, 140))
                
                textDers = fontGothic48.render('Çizge Teorisi Uygulamaları', True, config.renkSiyah)
                textRectDers = textDers.get_rect()
                textRectDers.center = (config.ekranGenişliği // 2 + 60, 40)
                
                textBaşlık = fontGothic48Bold.render('Mazecarousel', True, config.renkSiyah)
                textRectBaşlık = textBaşlık.get_rect()
                textRectBaşlık.center = (config.ekranGenişliği // 2 - 70, 100)
                
                textİsim = fontGothic36.render('Anıl Berk Bakır ~ 2024', True, config.renkSiyah)
                textRectİsim = textİsim.get_rect()
                textRectİsim.center = (195, config.ekranYüksekliği - 30)
            
            # Sayfa Arayüzü
            uygulamaEkranı.blit(logo, (10,10))
            uygulamaEkranı.blit(textDers, textRectDers)
            uygulamaEkranı.blit(textBaşlık, textRectBaşlık)
            uygulamaEkranı.blit(textİsim, textRectİsim)
            
            # Başlat Butonu
            başlatButonu.butonÇiz()
            
            if ((başlatButonu.mouseButonunÜzerinde()) and (mouseBasıldı)):
                # Labirent Classlarını Oluştur
                xAdet = 1
                yAdet = 1
                sütunSayısı = 10
                satırSayısı = 10
                düğümBoyutu = 40
                düğümDuvarBoyutu = 4
                labirentSeed = random.choice(range(0, 999999))
                
                labirentler = [Labirent(uygulamaEkranı,
                labirentSeed,
                200,
                80,
                #düğümBoyutu * (1 + x * (sütunSayısı + 1)),
                #düğümBoyutu * (1 + y * (satırSayısı + 1)),
                sütunSayısı,
                satırSayısı,
                düğümBoyutu,
                düğümDuvarBoyutu)
                for x in range(xAdet)
                for y in range(yAdet)
                ]
                
                # Durum Değiştir
                durumBaşlat = True
                uygulamaDurumu = 1
        
        # Labirent Oluştur
        case 1:
            if (durumBaşlat):
                # Değişkenler
                durumBaşlat = False
                seedGirilebilir = True
                
                # Butonları Yarat
                oluşturButonu = Buton(uygulamaEkranı, 330, 538, 220, 50, 2, -1, 'YENİ OLUŞTUR')
                grafButonu = Buton(uygulamaEkranı, 670, 150, 100, 100, 4, './görseller/grafButon.png')
                aramaButonu = Buton(uygulamaEkranı, 670, 350, 100, 100, 4, './görseller/aramaButon.png')
            
            # Labirenti Oluştur ve Çiz
            labirentlerTamamlandı = True
            for labirent in labirentler:
                labirent.labirentiÇiz(labirent.seed)
                labirent.labirentiOluştur()
                if not (labirent.labirentlerTamamlandı):
                    labirentlerTamamlandı = False
            
            # Seed Girişi
            seedGirişHedefText = girilenSeed
            seedGirişRenk = config.renkSiyah
            if (girilenSeed == ''):
                seedGirişHedefText = 'Seed Giriniz'
                seedGirişRenk = config.renkGri
            
            seedGirişText = fontGothic48.render(seedGirişHedefText, True, seedGirişRenk)
            seedGirişRect = seedGirişText.get_rect()
            seedGirişRect.center = (160, 560)
            uygulamaEkranı.blit(seedGirişText, seedGirişRect)
            
            # Oluştur Butonu
            oluşturButonu.butonÇiz()
            
            if ((oluşturButonu.mouseButonunÜzerinde()) and (mouseBasıldı)):
                # Labirent Classlarını Oluştur
                xAdet = 1
                yAdet = 1
                sütunSayısı = 10
                satırSayısı = 10
                düğümBoyutu = 40
                düğümDuvarBoyutu = 4
                labirentSeed = girilenSeed
                if (girilenSeed == ''):
                    labirentSeed = random.choice(range(0, 999999))
                
                labirentler = [Labirent(uygulamaEkranı,
                labirentSeed,
                200,
                80,
                #düğümBoyutu * (1 + x * (sütunSayısı + 1)),
                #düğümBoyutu * (1 + y * (satırSayısı + 1)),
                sütunSayısı,
                satırSayısı,
                düğümBoyutu,
                düğümDuvarBoyutu)
                for x in range(xAdet)
                for y in range(yAdet)
                ]
                
                girilenSeed = ''
            
            if (labirentlerTamamlandı):
                # Graf Butonu
                grafButonu.butonÇiz()
                
                if ((grafButonu.mouseButonunÜzerinde()) and (mouseBasıldı)):
                    # Durum Değiştir
                    seedGirilebilir = False
                    durumBaşlat = True
                    uygulamaDurumu = 2
                
                # Arama Butonu
                aramaButonu.butonÇiz()
                
                if ((aramaButonu.mouseButonunÜzerinde()) and (mouseBasıldı)):
                    # Durum Değiştir
                    seedGirilebilir = False
                    durumBaşlat = True
                    uygulamaDurumu = 3
        
        # Labirent Graf Görünümü
        case 2:
            if (durumBaşlat):
                # Değişkenler
                durumBaşlat = False
                
                # Butonları Yarat
                labirentButonu = Buton(uygulamaEkranı, 670, 150, 100, 100, 4, './görseller/labirentButon.png')
                aramaButonu = Buton(uygulamaEkranı, 670, 350, 100, 100, 4, './görseller/aramaButon.png')
            
            # Labirenti Çiz
            for labirent in labirentler:
                labirent.labirentiÇiz(labirent.seed, True)
            
            # Labirent Butonu
            labirentButonu.butonÇiz()
            
            if ((labirentButonu.mouseButonunÜzerinde()) and (mouseBasıldı)):
                # Durum Değiştir
                durumBaşlat = True
                uygulamaDurumu = 1
            
            # Arama Butonu
            aramaButonu.butonÇiz()
            
            if ((aramaButonu.mouseButonunÜzerinde()) and (mouseBasıldı)):
                # Durum Değiştir
                durumBaşlat = True
                uygulamaDurumu = 3
        
        # Labirent Yol Arama
        case 3:
            if (durumBaşlat):
                # Değişkenler
                durumBaşlat = False
                
                # Butonları Yarat
                başlangıçButonu = Buton(uygulamaEkranı, 150, 500, 200, 80, 4, './görseller/başlangıçButon.png')
                bitişButonu = Buton(uygulamaEkranı, 450, 500, 200, 80, 4, './görseller/bitişButon.png')
                grafButonu = Buton(uygulamaEkranı, 670, 150, 100, 100, 4, './görseller/grafButon.png')
                labirentButonu = Buton(uygulamaEkranı, 670, 350, 100, 100, 4, './görseller/labirentButon.png')
            
            # Labirenti Çiz
            for labirent in labirentler:
                labirent.labirentiÇiz(labirent.seed)
            
            if (başlangıçDüğümüSeçiliyor):
                # Başlangıç Durumu Seç
                if (mouseBasıldı):
                    for labirent in labirentler:
                        for düğüm in labirent.düğümler:
                            if (düğüm.mouseDüğümünÜzerinde()):
                                başlangıçDüğümü = düğüm.index
                                labirent.başlangıçDüğümü = düğüm.index
                                düğüm.başlangıçDüğümü = True
                                düğüm.bitişDüğümü = False
                                başlangıçDüğümüSeçiliyor = False
                                if (bitişDüğümü != -1):
                                    labirent.yolBul = True
                                    labirent.labirentiÇöz()
                                break
            elif (bitişDüğümüSeçiliyor):
                # Bitiş Düğümü Seç
                if (mouseBasıldı):
                    for labirent in labirentler:
                        for düğüm in labirent.düğümler:
                            if (düğüm.mouseDüğümünÜzerinde()):
                                bitişDüğümü = düğüm.index
                                labirent.bitişDüğümü = düğüm.index
                                düğüm.bitişDüğümü = True
                                düğüm.başlangıçDüğümü = False
                                bitişDüğümüSeçiliyor = False
                                if (başlangıçDüğümü != -1):
                                    labirent.yolBul = True
                                    labirent.labirentiÇöz()
                                break
            else:
                # Başlangıç Butonu
                başlangıçButonu.butonÇiz()
                
                if ((başlangıçButonu.mouseButonunÜzerinde()) and (mouseBasıldı)):
                    başlangıçDüğümüSeçiliyor = True
                    
                    for labirent in labirentler:
                        yolBul = False
                        labirent.başlangıçDüğümü = -1
                    if (başlangıçDüğümü != -1):
                        for labirent in labirentler:
                            for düğüm in labirent.düğümler:
                                if düğüm.başlangıçDüğümü:
                                    düğüm.başlangıçDüğümü = False
                                    başlangıçDüğümü = -1
                
                # Bitiş Butonu
                bitişButonu.butonÇiz()
                
                if ((bitişButonu.mouseButonunÜzerinde()) and (mouseBasıldı)):
                    bitişDüğümüSeçiliyor = True
                    
                    for labirent in labirentler:
                        yolBul = False
                        labirent.bitişDüğümü = -1
                    if (bitişDüğümü != -1):
                        for labirent in labirentler:
                            for düğüm in labirent.düğümler:
                                if düğüm.bitişDüğümü:
                                    düğüm.bitişDüğümü = False
                                    bitişDüğümü = -1
                
                # Graf Butonu
                grafButonu.butonÇiz()
                
                if ((grafButonu.mouseButonunÜzerinde()) and (mouseBasıldı)):
                    # Durum Değiştir
                    for labirent in labirentler:
                        labirent.yolBul = False
                        labirent.başlangıçDüğümü = -1
                        labirent.bitişDüğümü = -1
                        for düğüm in labirent.düğümler:
                            düğüm.gidildiDFS = False
                            düğüm.başlangıçDüğümü = False
                            düğüm.bitişDüğümü = False
                    başlangıçDüğümü = -1
                    bitişDüğümü = -1
                    başlangıçDüğümüSeçiliyor = False
                    bitişDüğümüSeçiliyor = False
                    durumBaşlat = True
                    uygulamaDurumu = 2
                
                # Labirent Butonu
                labirentButonu.butonÇiz()
                
                if ((labirentButonu.mouseButonunÜzerinde()) and (mouseBasıldı)):
                    # Durum Değiştir
                    for labirent in labirentler:
                        labirent.yolBul = False
                        labirent.başlangıçDüğümü = -1
                        labirent.bitişDüğümü = -1
                        for düğüm in labirent.düğümler:
                            düğüm.gidildiDFS = False
                            düğüm.başlangıçDüğümü = False
                            düğüm.bitişDüğümü = False
                    başlangıçDüğümü = -1
                    bitişDüğümü = -1
                    başlangıçDüğümüSeçiliyor = False
                    bitişDüğümüSeçiliyor = False
                    durumBaşlat = True
                    uygulamaDurumu = 1
    
    # Değişkenleri Yenile
    mouseBasıldı = False
    
    # Ekranı Yenile
    pygame.display.flip()
    pygame.time.Clock().tick()