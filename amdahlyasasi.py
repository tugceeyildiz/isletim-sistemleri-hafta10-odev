# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 20:16:19 2025

@author: TUĞÇE
"""

import time

def amdahl_hesapla(S,N):
    
    if S<0 or S>1 or N<1:
        return 0.0
    
    hizlanma=1.0 / (S + (1.0 - S) / N)
    return hizlanma 

def amdahl_uygulamasi():
    print("--- Amdahl Yasası Teorik Hızlanma Analizi ---")
    
    #S
    seri_oranlari=[0.05, 0.10, 0.25, 0.50]
    
    #N
    cekirdek_sayilari=[2, 4, 8, 16, 32]
    
    header=f"{'Seri Oranı (S)':<15} | {'Paralel Kısım':<15} | {'Max Hızlanma (1/S)':<20}"
    for N in cekirdek_sayilari:
        header+= f" | N={N:<6}"
    print ("-" * len(header))
    print(header)
    print("-" * len(header))
    
    for S in seri_oranlari:
        paralel = (1.0 - S) * 100
        
        max_hizlanma = 1.0 / S if S != 0 else float('inf')
        
        row=f"{S*100:<15.0f}% | {paralel:<15.0f}% | {max_hizlanma:<20.3f}"
        
        for N in cekirdek_sayilari:
            hizlanma = amdahl_hesapla(S, N)
            row += f"| {hizlanma:<6.3f}"
        
        print(row)
        
    print("-" * len(header))
    print("\n --- Yorum: ---")
    print("Seri kısım (S) ne kadar düşükse, çekirdek sayısındaki artışın getirisi (hızlanma) o kadar büyük olur.")
    print("S=50% iken (uygulamanın yarısı seri) 32 çekirdek ile bile hızlanma sadece 1.94 kat ile sınırlıdır.")

if __name__ == "__main__":
    amdahl_uygulamasi()