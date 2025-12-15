# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 11:00:29 2025

@author: TUĞÇE
"""

import threading
import time

def dosya_yukle(kullanici_id):
    print(f"[{threading.current_thread().name}] Kullanıcı {kullanici_id}: Dosya yükleniyor...")
    time.sleep(1)
    
def rapor_olustur():
    print(f"[{threading.current_thread().name}] Rapor oluşturma tamamlandı")
    
if __name__== "__main__":
    print("--- Çoklu Programlama Başlatılıyor ---")
    
    thread1=threading.Thread(target=dosya_yukle , name="Thread-Dosya")
    thread2=threading.Thread(target=rapor_olustur , name="Thread-Rapor")
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("\n---Tüm Programlar Tamamlandı---")