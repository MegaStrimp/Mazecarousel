# -*- coding: utf-8 -*-

def dfs(grafMatrixi, başlangıçDüğümü, bitişDüğümü, gidilenDüğümler = None, yol = None):
    if gidilenDüğümler is None:
        gidilenDüğümler = set()
    if yol is None:
        yol = []
    
    # Şimdiki Noktayı İşaretle
    gidilenDüğümler.add(başlangıçDüğümü)
    yol.append(başlangıçDüğümü)
    
    # Sona Gelince Yolu Döndür ve Bitir
    if başlangıçDüğümü == bitişDüğümü:
        return yol
    
    # Tüm Komşuları Ziyaret Et
    for komşu, bağlı in enumerate(grafMatrixi[başlangıçDüğümü]):
        if bağlı and komşu not in gidilenDüğümler:
            sonuç = dfs(grafMatrixi, komşu, bitişDüğümü, gidilenDüğümler, yol)
            if sonuç:
                return sonuç
            
    yol.pop()
    return None