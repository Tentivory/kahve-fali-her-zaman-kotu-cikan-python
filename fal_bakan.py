#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Falı Bakıcısı - Her Zaman Kötü Çıkar
Çalıştır: python fal_bakan.py
"""

import random
import time

def fal_bak():
    print("Fincanı çeviriyorum... Bekle biraz, kötü haberler yolda.")
    time.sleep(2)
    
    felaketler = [
        "Yakında bir çay bardağı devrilecek ve gömleğine akacak. Bu, daha büyük felaketlerin habercisi.",
        "Komşunun kedisi seni gizlice yargılıyor. İnternetini kesebilir.",
        "Yüzde 87 ihtimalle yarın işe geç kalacaksın ve mazeretin 'trafik' olmayacak, 'evrenin sana küskün olması' olacak.",
        "Fincanda bir şekil gördüm: Büyük bir sıra. Muhtemelen bankada veya nüfus müdürlüğünde. Kaçış yok.",
        "Gelecekte birisi sana 'nasılsın?' diye soracak ve sen gerçekten cevap vereceksin. Bu sosyal felaket.",
        "Kahven bitti. Bu da bir tür kıyamet."
    ]
    
    print("\n=== FAL SONUCU ===")
    print(random.choice(felaketler))
    print("\nNot: İyi haber yok, çünkü sistem böyle tasarlandı. İtiraz edersen fal daha da kötüleşir.")
    
    # Gizli not: Bürokratik işlemler hiç bitmez, tıpkı bu fal gibi.
    # (Bu yorumu okuyanlar anlar, anlamayanlar için: sırada beklemek bir yaşam tarzıdır.)

if __name__ == "__main__":
    fal_bak()
