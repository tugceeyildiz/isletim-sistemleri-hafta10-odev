# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 19:43:38 2025

@author: TUĞÇE
"""

from multiprocessing import Process
import threading
import time
import os

def kare_hesapla(tip,sayi):
    
    pid=os.getpid()
    tid=threading.get_ident()
    
    print(f"Kare Hesaplanıyor [{tip}] - PID: {pid} | TID: {tid}: {sayi} --> {sayi*sayi}")
    time.sleep(1)

def coklu_programlama_calistir(sayilar):
    print("\n--- 1.Çoklu Programlama ---")
    threads=[]
    for i,s in enumerate(sayilar):
        t=threading.Thread(target=kare_hesapla,args=("Thread",s), name=f"T-{i+1}")
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    print("--- Çoklu Programlama Tamamnlandı ---")
    
def coklu_islem_calistir(sayilar):
    print("\n--- 2.Çoklu İşlem ---")
    processes=[]
    for s in sayilar:
        p = Process(target=kare_hesapla, args=("Process", s))
        p.start()
        
    for p in processes:
        p.join()
    print("--- Çoklu İşlem Tamamlandı ---")
    
if __name__=="__main__":
    sayilar_listesi= [10,20,30,40]
    
    coklu_programlama_calistir(sayilar_listesi)
    coklu_islem_calistir(sayilar_listesi)
    
    print("\nGenel Karşılaştırma Tamamlandı!!!")
    
