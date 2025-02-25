"""def iki_tam_sayi():

    s1 = float(input("Birinci sayıyı giriniz:"))

    s2 = float(input("İkinci sayıyı giriniz:"))

    sonuc = s1 + s2

    print("sayıların toplamı:",sonuc)

iki_tam_sayi()"""

"""def pozitif_negatif():
    s = int(input("Bir sayı giriniz:"))

    if s > 0:
        print("Pozitif")
    elif s < 0:
        print("negatif")
    else :
        print("Sıfır")

pozitif_negatif()"""

"""def en_büyük_sayı(s1,s2,s3):
    if s1 >= s2 and s1 >= s2:
        return s1
    elif s2 >= s1 and s2 >=s3:
        return s2
    else:
        return s3

s1 = float(input("Birci sayıyı giriniz:"))
s2 = float(input("İkinci sayıyı giriniz:"))
s3 = float(input("Üçüncü sayıyı giriniz:"))

print("En büyük sayı:", en_büyük_sayı(s1,s2,s3))"""

"""def cift_tek_sayı():
    sayi = float(input("Lütfen bir sayı giriniz:"))

    if sayi % 2 == 0 :
        print("Çift sayı:")
    else:
        print("Tek sayı:")

cift_tek_sayı()"""


"""def sayı_gun():
    try:
        sayi = int(input("1-7 arası sayı giriniz: "))

        match sayi:
            case 1:
                print("Pazatesi")
            case 2:
                print("Salı")
            case 3:
                print("Çarşamba")
            case 4:
                print("Peşembe")
            case 5:
                print("Cuma")
            case 6:
                print("Cumartesi")
            case 7:
                print("pazar")
            case _:
                print("Gün yok")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!!!")

sayı_gun()"""

"""def mini_hesap():
    try:
        s1 = int(input("Birinci sayıyı giriniz: "))
        s2 = int(input("İkinci sayıyı giriniz: "))
        islem = input("Yapmak istediğiniz işlemi giriniz(+,-,*,/): ")

        match islem:
            case "+":
                print(f"sonuç: {s1 + s2}")
            case "-":
                print(f"sonuç: {s1 - s2}")
            case "*":
                print(f"sonuç: {s1 * s2}")
            case "/":
                if s2 != 0:
                    print(f"Sonuç: {s1 / s2}")
                else:
                    print("Sıfırdan farklı bir sayu giriniz: ")
            case _:
                print("Geçersiz işlem")
    except ValueError:
        print("Lütfen tam sayılar giriniz:")

mini_hesap()"""

"""def n_toplama():
    try:
        n = int(input("Pozitif bir tam sayı giriniz: "))
        if n < 1:
            print("Lütfen bir veya daha bütük bir sayı girin.")
            return

        t = 0
        for i in range(1, n + 1):
            t += i

        print(f"1'den {n}'ye kardar olan sayıların toplamı: {t}")
    except ValueError:
        print("Lütfen tam sayı girniz!!!")#Ufak bir dip not: Burada olan hesaplamalar bize faktöriyel kavramına götürevilcek seviyededir.
n_toplama()"""

"""def carpım_tablosu():
    try:
        s = int(input("Bir tam sayı girin: "))

        print(f"{s} sayısının çarpım tablosu:")
        for i in range(1, 11):
            print(f"{s} x {i} = {s * i}")

    except ValueError:
        print("LÜtfen geçerli bir tam sayı girin.")
carpım_tablosu()"""

"""def sayı_ortalama():
    t = 0
    adet = 5
    print("Lütfen 5 tam sayı giriniz: ")
    for i in range(adet):
        try:
            s = int(input(f"{i+1}. sayı girin:"))
            t += s
        except ValueError:
            print("Geçerli bir tam sayı ")
            return
    ortalama = t / adet
    print(f"Sayılarn ortalamarı: {ortalama}")
sayı_ortalama()"""

"""def asal_kontrol():
    try:
        s = int(input("Bir pozitif sayı giriniz:"))

        if s < 2:
            print(f"{s} asal değildir.")
            return
        for i in range(2, int(s**0.5) + 1):
            if s % i == 0:
                print(f"{s} asal değildir.")
                return
        print(f"{s} asaldır.")
    except ValueError:
        print("LÜtfen tam sayı giriniz.!!")

asal_kontrol()"""

"""def faktoriyel_hesaplama():
    sayi = int(input("Bir sayı girin: "))
    if sayi < 0:
        print("Negatif sayıların faktöriyeli hesaplanamaz!")
    else:
        faktoriyel = 1
        i = sayi
        while i > 0:
            faktoriyel *= i
            i -= 1
        print(f"{sayi}'nin faktöriyeli: {faktoriyel}")

"""
"""def sayi_tahmin_oyunu():
    tutulan_sayi = random.randint(1, 100)
    tahmin = 0
    while tahmin != tutulan_sayi:
        tahmin = int(input("1-100 arası bir tahmin girin: "))
        if tahmin < tutulan_sayi:
            print("Daha büyük bir sayı girin.")
        elif tahmin > tutulan_sayi:
            print("Daha küçük bir sayı girin.")
    print("Tebrikler! Doğru tahmin ettiniz.")

"""
"""def fibonacci_serisi():
    n = int(input("Kaç tane Fibonacci terimi görmek istiyorsunuz? "))
    if n <= 0:
        print("Lütfen pozitif bir sayı girin.")
    else:
        a, b = 0, 1
        print("Fibonacci serisi:")
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b

"""
"""def tersine_cevirme():
    sayi = int(input("Bir sayı girin: "))
    ters = 0
    while sayi > 0:
        basamak = sayi % 10
        ters = ters * 10 + basamak
        sayi //= 10
    print(f"Sayının tersi: {ters}")"""


"""def armstrong_sayisi():
    sayi = int(input("Bir sayı girin: "))
    gecici = sayi
    basamak_sayisi = len(str(sayi))
    toplam = 0
    while gecici > 0:
        basamak = gecici % 10
        toplam += basamak ** basamak_sayisi
        gecici //= 10
    if toplam == sayi:
        print(f"{sayi} bir Armstrong sayısıdır.")
    else:
        print(f"{sayi} bir Armstrong sayısı değildir.")"""




"""def cift_sayilarin_toplami():
    toplam = 0
    for i in range(1, 101):
        if i % 2 == 0:
            toplam += i
    print(f"1-100 arası çift sayıların toplamı: {toplam}")"""


"""def tek_sayilarin_carpimi():
    carpim = 1
    for i in range(1, 11):
        if i % 2 != 0:
            carpim *= i
    print(f"1-10 arası tek sayıların çarpımı: {carpim}")"""


"""def sayilarin_karesi():
    for i in range(1, 11):
        print(f"{i}'nin karesi: {i**2}")"""


"""def sifre_kontrolu():
    sifre = input("Şifrenizi girin: ")
    if sifre == "python123":
        print("Giriş başarılı")
    else:
        print("Giriş başarısız")"""


"""def yas_kontrolu():
    yas = int(input("Yaşınızı girin: "))
    if yas > 18:
        print("Reşit")
    else:
        print("Reşit değil")
"""

"""def not_ortalamasi():
    not1 = float(input("1. ders notunu girin: "))
    not2 = float(input("2. ders notunu girin: "))
    not3 = float(input("3. ders notunu girin: "))
    ortalama = (not1 + not2 + not3) / 3
    if ortalama > 50:
        print("Geçti")
    else:
        print("Kaldı")
"""

"""def vki_hesaplama():
    boy = float(input("Boyunuzu metre cinsinden girin: "))
    kilo = float(input("Kilonuzu kg cinsinden girin: "))
    vki = kilo / (boy ** 2)
    if vki > 25:
        print("Fazla kilolu")
    else:
        print("Fazla kilolu değil")
"""

"""def dort_islem():
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    print("1: Toplama\n2: Çıkarma\n3: Çarpma\n4: Bölme")
    secim = int(input("Yapmak istediğiniz işlemi seçin (1-4): "))
    match secim:
        case 1:
            print(f"Sonuç: {sayi1 + sayi2}")
        case 2:
            print(f"Sonuç: {sayi1 - sayi2}")
        case 3:
            print(f"Sonuç: {sayi1 * sayi2}")
        case 4:
            if sayi2 != 0:
                print(f"Sonuç: {sayi1 / sayi2}")
            else:
                print("Sıfıra bölme hatası!")
        case _:
            print("Geçersiz seçim")

"""
"""def en_kucuk_sayi():
    a = int(input("1. sayıyı girin: "))
    b = int(input("2. sayıyı girin: "))
    c = int(input("3. sayıyı girin: "))
    d = int(input("4. sayıyı girin: "))
    en_kucuk = a
    if b < en_kucuk:
        en_kucuk = b
    if c < en_kucuk:
        en_kucuk = c
    if d < en_kucuk:
        en_kucuk = d
    print(f"En küçük sayı: {en_kucuk}")

"""
"""def artan_siralama():
    a = int(input("1. sayıyı girin: "))
    b = int(input("2. sayıyı girin: "))
    c = int(input("3. sayıyı girin: "))
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    print(f"Küçükten büyüğe: {a}, {b}, {c}")

"""
"""def while_toplami():
    n = int(input("N sayısını girin: "))
    toplam = 0
    i = 1
    while i <= n:
        toplam += i
        i += 1
    print(f"1-{n} arası toplam: {toplam}")

"""
"""def sayilarin_carpimi():
    carpim = 1
    for i in range(1, 6):
        carpim *= i
    print(f"1-5 arası sayıların çarpımı: {carpim}")

"""
"""def karelerin_toplami():
    toplam = 0
    for i in range(1, 11):
        toplam += i ** 2
    print(f"1-10 arası karelerin toplamı: {toplam}")

"""
"""def kuplerin_toplami():
    n = int(input("N sayısını girin: "))
    toplam = 0
    for i in range(1, n + 1):
        toplam += i ** 3
    print(f"1-{n} arası küplerin toplamı: {toplam}")

"""
"""def uc_ve_bes_bolunen():
    sayac = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            sayac += 1
    print(f"1-100 arası hem 3’e hem 5’e bölünen sayı adedi: {sayac}")

"""
"""def not_harfi():
    notu = int(input("Sınav notunu girin (0-100): "))
    if notu >= 90:
        print("A")
    elif notu >= 80:
        print("B")
    elif notu >= 70:
        print("C")
    elif notu >= 60:
        print("D")
    else:
        print("F")

"""
"""def uc_sayi_karsilastirma():
    a = int(input("1. sayıyı girin: "))
    b = int(input("2. sayıyı girin: "))
    c = int(input("3. sayıyı girin: "))
    if a == b == c:
        print("Tüm sayılar eşit")
    elif a == b or b == c or a == c:
        print("İki sayı eşit")
    else:
        print("Hiçbiri eşit değil")

"""
"""def artik_yil():
    yil = int(input("Yılı girin: "))
    if yil % 400 == 0:
        print("Artık yıl")
    elif yil % 100 == 0:
        print("Artık yıl değil")
    elif yil % 4 == 0:
        print("Artık yıl")
    else:
        print("Artık yıl değil")
"""

"""def bmi_kategorisi():
    boy = float(input("Boyunuzu metre cinsinden girin: "))
    kilo = float(input("Kilonuzu kg cinsinden girin: "))
    bmi = kilo / (boy ** 2)
    if bmi < 18.5:
        print("Zayıf")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Fazla Kilolu")
    else:
        print("Obez")
"""

"""def ucgen_turu():
    a = float(input("1. kenarı girin: "))
    b = float(input("2. kenarı girin: "))
    c = float(input("3. kenarı girin: "))
    if a + b <= c or b + c <= a or a + c <= b:
        print("Üçgen değil")
    elif a == b == c:
        print("Eşkenar üçgen")
    elif a == b or b == c or a == c:
        print("İkizkenar üçgen")
    else:
        print("Çeşitkenar üçgen")
"""

"""def bilet_fiyati():
    yas = int(input("Yaşınızı girin: "))
    if yas <= 5:
        print("Ücretsiz")
    elif yas <= 18:
        print("10 TL")
    elif yas <= 64:
        print("20 TL")
    else:
        print("15 TL")
"""

"""def hava_durumu():
    durum = input("Hava durumunu girin (güneşli, yağmurlu, karlı): ")
    sicaklik = float(input("Sıcaklığı girin (°C): "))
    if durum == "güneşli" and sicaklik >= 25:
        print("Piknik yapabilirsiniz.")
    elif durum == "yağmurlu":
        print("Şemsiye almayı unutmayın.")
    elif durum == "karlı" and sicaklik < 0:
        print("Kayak yapmaya gidebilirsiniz.")
    else:
        print("Evde kalabilirsiniz.")

"""
"""def sayi_kontrol():
    sayi = int(input("Bir tam sayı girin: "))
    if sayi > 0:
        print("Pozitif")
    elif sayi < 0:
        print("Negatif")
    else:
        print("Sıfır")
"""

"""def iki_sayi_karsilastirma():
    a = int(input("1. sayıyı girin: "))
    b = int(input("2. sayıyı girin: "))
    if a > b:
        print("Birinci sayı büyük")
    elif b > a:
        print("İkinci sayı büyük")
    else:
        print("Sayılar eşit")

"""
"""def uye_indirimi():
    tutar = float(input("Alışveriş tutarını girin: "))
    uye = input("Üye misiniz? (evet/hayır): ")
    if uye == "evet":
        indirim = tutar * 0.10
        print(f"İndirimli tutar: {tutar - indirim} TL")
    else:
        indirim = tutar * 0.05
        print(f"İndirimli tutar: {tutar - indirim} TL")
"""
