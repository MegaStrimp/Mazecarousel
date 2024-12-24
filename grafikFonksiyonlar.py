# -*- coding: utf-8 -*-

# Kütüphaneler
import math

def sinüsDalgası(genlik, frekans, zaman, tamSayı = False):
    if (tamSayı):
        return math.floor(genlik * math.sin(2 * math.pi * frekans * zaman))
    else:
        return genlik * math.sin(2 * math.pi * frekans * zaman)