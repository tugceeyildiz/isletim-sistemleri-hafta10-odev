# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 19:19:47 2025

@author: TUĞÇE
"""

from multiprocessing import Process
import os
import time

def faktoriyel_hesapla(sayi):
    
    print(f"İşlem: {os.getpid()} - Sayı {sayi}: Hesaplama Başladı...")
    
    sonuc=1
    for i in range(1, sayi+1):
        sonuc*= i
    
    time.sleep(1)
    
    print(f"İşlem: {os.getpid()} - Sayı {sayi}: Sonuç Tamamlandı!!!")
    
if __name__=="__main__":
    print("Çoklu İşlemci Başlatılıyor...\n")
    
    sayilar=[5,6,7,8]
    islemler=[]
    
    for sayi in sayilar:
        islem=Process(target=faktoriyel_hesapla,args=(sayi, ))
        islemler.append(islem)
        islem.start()
    
    for islem in islemler:
        islem.join()
        
    print("\n---Tüm Paralel İşlemler Tamamlandı---")
    
    
    
    
    
    
    
    