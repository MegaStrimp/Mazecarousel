# -*- coding: utf-8 -*-

def duvarSil(bulunanDüğüm, sonrakiDüğüm):
    xx = bulunanDüğüm.x - sonrakiDüğüm.x
    yy = bulunanDüğüm.y - sonrakiDüğüm.y
    
    if (xx == 1):
        bulunanDüğüm.duvarlar['sol'] = False
        sonrakiDüğüm.duvarlar['sağ'] = False
    elif (xx == -1):
        bulunanDüğüm.duvarlar['sağ'] = False
        sonrakiDüğüm.duvarlar['sol'] = False
    if (yy == 1):
        bulunanDüğüm.duvarlar['üst'] = False
        sonrakiDüğüm.duvarlar['alt'] = False
    elif (yy == -1):
        bulunanDüğüm.duvarlar['alt'] = False
        sonrakiDüğüm.duvarlar['üst'] = False

def matrixDönüştür(düğümler, satırSayısı, sütunSayısı):
    boyut = len(düğümler)
    matrix = [[0] * boyut for i in range(boyut)]

    for düğüm in düğümler:
        bulunanDüğüm = düğüm.x + düğüm.y * sütunSayısı
        
        if ((düğüm.duvarlar['üst'] == False) and (düğüm.y > 0)):
            komşuDüğüm = düğüm.x + (düğüm.y - 1) * sütunSayısı
            matrix[bulunanDüğüm][komşuDüğüm] = 1
            matrix[komşuDüğüm][bulunanDüğüm] = 1

        if ((düğüm.duvarlar['alt'] == False) and (düğüm.y < satırSayısı - 1)):
            komşuDüğüm = düğüm.x + (düğüm.y + 1) * sütunSayısı
            matrix[bulunanDüğüm][komşuDüğüm] = 1
            matrix[komşuDüğüm][bulunanDüğüm] = 1

        if ((düğüm.duvarlar['sol'] == False) and (düğüm.x > 0)):
            komşuDüğüm = (düğüm.x - 1) + düğüm.y * sütunSayısı
            matrix[bulunanDüğüm][komşuDüğüm] = 1
            matrix[komşuDüğüm][bulunanDüğüm] = 1

        if ((düğüm.duvarlar['sağ'] == False) and (düğüm.x < sütunSayısı - 1)):
            komşuDüğüm = (düğüm.x + 1) + düğüm.y * sütunSayısı
            matrix[bulunanDüğüm][komşuDüğüm] = 1
            matrix[komşuDüğüm][bulunanDüğüm] = 1
    
    return matrix