# Welcome to StackEdit!

Hi! I'm your first Markdown file in **StackEdit**. If you want to learn about StackEdit, you can read me. If you want to play with Markdown, you can edit me. Once you have finished with me, you can create new files by opening the **file explorer** on the left corner of the navigation bar.


# Keylogger

Bu proje,  **istemci-sunucu** modelini kullanarak klavye olaylarını dinleyen bir Python uygulamasını içerir.
## Client

`client.py` dosyası, klavye olaylarını dinleyen ve bu olayları belirtilen bir sunucuya ileten istemci kodlarını içerir. İstemci, klavye olaylarını dinlemek için `pynput` kütüphanesini kullanır ve bu olayları bir bağlantı kurarak belirtilen sunucuya iletir.
## Client Kullanılan Kütüphaneler

-  `socket`  
-  `sys`  
-  `pynput`
## Server

`server.py` dosyası, istemcilerin bağlandığı bir sunucu uygulamasını başlatan kodları içerir. Sunucu, istemcilerden gelen klavye verilerini alır ve ekrana yazdırır.
## Server Kullanılan Kütüphaneler

-   `socket`
-   `threading`

## !
Not: Sunucu, belirtilen IP adresi ve port numarasında dinlemeye yapar.



# requirements.txt

Bu dosya, proje için gerekli olan `pynput` kütüphanesini belirtir. İstemci kodu, bu kütüphaneyi klavye olaylarını dinlemek için kullanıyor. `requirements.txt` dosyasını projenin kök dizinine kaydedebilir ve ardından bu bağımlılıkları yüklemek için aşağıdaki komutu kullanabilirsin:

    pip install -r requirements.txt


## Kullanım

 1. server.py dosyasını çalıştırın.
 2. clint.py dosyasını çalıştırın

## Önemli

Bu proje eğitim amaçlı olarak hazırlanmıştır. Aksi yöndeki kullanımlardan sorumlu değilim.
