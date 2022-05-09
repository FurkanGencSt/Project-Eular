import time

urunler = {"KOLA": 10, "SPRITE": 10, "FANTA": 10, "REDBULL": 10, "KRISPI": 10, "GOFRET": 10, "KRUVASAN": 10,
           "CIKOLATALI_BISKUVI": 10}
fiyatlar = {"KOLA": 9.5, "SPRITE": 8.5, "FANTA": 7.5, "REDBULL": 12, "KRISPI": 4, "GOFRET": 2, "KRUVASAN": 4.5,
            "CIKOLATALI_BISKUVI": 6.5}


def kontrol():
    admin_password = 1234
    password = int(input("Şifreyi giriniz: "))
    hak = 3
    if password == admin_password:
        admin()
    elif password != admin_password:
        hak -= 1
        print("Hatalı şifre, yeniden deneyiniz.")
        admin()
        if hak == 0:
            print("Çok fazla hatalı giriş yaptınız. Bir süre bekleyiniz.")
            for i in range(1, 6):
                print(i, "...")
                time.sleep(1)
            kontrol()


def admin():
    print("1-Urun ekle/cıkar.\n2-Fiyat guncelle.\n3-Cıkış.")
    secim = int(input("Lütfen birisini seciniz: "))
    if secim == 1:
        secim = int(input("Eklemek icin '1', cıkarmak icin '2' e basınız."))
        if secim == 1:
            urun = input("Eklemek istediğiniz ürünü yazınız: ").upper()
            adet = int(input("Kaç adet eklemek istersiniz: "))
            fiyat = float(input("Fiyatı kaç tl olacak: "))
            if urun in urunler:
                urunler[urun] += adet
                fiyatlar[urun] = fiyat
                admin()
            elif urun not in urunler:
                urunler[urun] = adet
                fiyatlar[urun] = fiyat
                admin()

        elif secim == 2:
            urun = input("Çıkarmak istediğiniz ürünü yazınız: ").upper()
            urunler.pop(urun)
            fiyatlar.pop(urun)
            admin()

    elif secim == 2:
        urun = input("Fiyatını değiştirmek istediğiniz ürünü yazınız: ").upper()
        fiyat = float(input("Yeni fiyatı giriniz: "))

        fiyatlar[urun] = fiyat
        admin()
    elif secim == 3:
        print("Ana ekrana yönlendiriliyorsunuz...")
        time.sleep(3)
        anaekran()
    else:
        print("Hatalı bir giriş yaptınız. Lütfen tekrar deneyin.")
        admin()


def musteri():
    print(urunler)
    print("**********************")
    secim = input("Lütfen bir secim yapınız (Eğer çıkmak isterseniz '*' tusuna basınız.): ").upper()
    para = float(input("Para ekle: "))
    para2 = 0
    para2 += para

    if secim == "*":  # Çıkmak isterse
        print("Cıkıs yapılıyor...")
        time.sleep(3)
        anaekran()

    if urunler[secim] >= 0:  # Eğer ürün var ise:
        fiyat = fiyatlar[secim]

        if para2 == fiyat:
            urunler[secim] -= 1
            print("Ürününüz hazırlanıyor...")
            time.sleep(2)
            para2 = 0
            anaekran()

        elif para2 > fiyat:
            urunler[secim] -= 1
            print("Ürününüz ve Para üstünüz hazırlanıyor...")
            print("Para üstünüz: ", int(para2) - fiyat, "tl' dir.")
            time.sleep(2)
            para2 = 0
            anaekran()

        elif para2 < fiyat:
            secim = int(input(
                "Eksik para. Lütfen bir secim yapınız.\n**********\n1- Para ekle veya ürün değistir.\n2-Vazgeç\nSecim: "))
            if secim == 1:

                musteri()
            elif secim == 2:
                print("Verdiğiniz para iade ediliyor...")
                time.sleep(3)
                anaekran()
    elif urunler[secim] < 0:
        print("Maalesef elimizde o üründen kalmamoştır. Lütfen başka bir ürün seciniz.")
        musteri()


def anaekran():
    secim = int(input("1-Admin\n2-Musteri\nBir secim yapınız: "))

    if secim == 1:
        kontrol()
    elif secim == 2:
        musteri()
    else:
        print("Hatalı bir sayı girdiniz.")
        time.sleep(2)
        anaekran()


anaekran()
