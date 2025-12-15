# isletim-sistemleri-hafta10-odev
# 💻 İşletim Sistemleri Dersi - Python Yazılım Ödevi

## Ders Bilgileri
- **Ders:** İşletim Sistemleri
- **Öğrenci:** Havva Tuğçe Yıldız
- **Tarih:** 10. Hafta Çalışması (15 Aralık 2025)

---

## 📌 Ödevin Amacı
Bu çalışmanın amacı, işletim sistemlerinde eşzamanlı ve paralel programlamanın temelini oluşturan **Thread (İş Parçacığı)** ve **Process (İşlem)** kavramlarını uygulamalı olarak incelemektir. Ayrıca, çok çekirdekli sistemlerde elde edilebilecek teorik performans kazancını **Amdahl Yasası** ile analiz etmek hedeflenmiştir.

---

## 📂 İçerik ve Uygulamalar

Bu depo, dört temel kavramı gösteren ayrı Python script'lerini içermektedir:

### 1. Çoklu Programlama (Threading)
* **Dosya Adı:** `multiprogramming.py`
* **Amaç:** İş parçacıklarının (**Threads**) aynı işlem (Process) içinde **zaman paylaşımı (time-sharing)** yaparak eşzamanlı (concurrent) çalıştığını göstermek.
* **Çalışma Yapısı:** İki farklı görev (`dosya_yukle` ve `rapor_olustur`) eşzamanlı olarak başlatılır. Çıktılar, bu iki görevin işletim sistemi tarafından sırayla yürütüldüğünü gösterir.

### 2. Çoklu İşlem (Multiprocessing)
* **Dosya Adı:** `multiprocessing.py`
* **Amaç:** Birden fazla bağımsız süreç (**Processes**) kullanarak sistemdeki birden fazla CPU çekirdeğinde **gerçek paralelliğin** nasıl sağlandığını göstermek.
* **Çalışma Yapısı:** Dört farklı sayı için (`[5, 6, 7, 8]`) ayrı ayrı `Process` oluşturularak faktöriyel hesaplamaları paralel olarak yapılır. Her işlemin benzersiz bir **Process ID (PID)**'ye sahip olduğu gözlemlenir.

### 3. Thread ve Process Karşılaştırması
* **Dosya Adı:** `multikarsilastirma.py`
* **Amaç:** Aynı görevin (**kare_hesapla**) hem Threading hem de Multiprocessing ile çalıştırılmasını karşılaştırmak.
* **Gözlem:**
    * **Threading:** Tüm iş parçacıklarının **aynı PID** altında, ancak farklı **TID**'ler ile çalıştığı görülür.
    * **Multiprocessing:** Her bir işlemin **farklı PID**'ler ile çalıştığı görülür, bu da onların bağımsız bellek alanlarına sahip ayrı OS süreçleri olduğunu kanıtlar.

### 4. Amdahl Yasası Teorik Analizi
* **Dosya Adı:** `amdahlyasasi.py`
* **Amaç:** Bir uygulamanın seri kısmının (%S) performans kazancını nasıl sınırladığını **Amdahl Yasası** formülü üzerinden göstermek.
* **Çalışma Yapısı:** Farklı seri oranları (`S`) ve farklı işlemci çekirdeği sayıları (`N`) için teorik hızlanma (`Speedup`) hesaplanır ve sonuçlar tablo halinde sunulur.

---

## 🚀 Çalıştırma Talimatları
Bu uygulamaları çalıştırmak için bilgisayarınızda Python kurulu olmalıdır. İlgili dosyayı terminal veya komut istemi üzerinden çalıştırabilirsiniz:

```bash
# Örnek: Çoklu Programlama uygulamasını çalıştırmak için
python multiprogramming.py

# Örnek: Amdahl Yasası analizini çalıştırmak için
python amdahlyasasi.py
