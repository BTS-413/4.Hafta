kitapListesi = list()

menu = """
[1] Kitap Ekle
[2] Kitap Cikar
[3] Kitaplari listele
[Q] Cikis

"""

def kitapEkle(kitap,liste):
    liste += [kitap]
    print("Kitap eklendi")
    input("Ana menu icin 'enter'e basin ")

def kitapCikar():
    pass

def listeler(liste):
    for i in liste:
        print("Kitap adi ----> {}".format(i))
def cikis():
    quit()

while True:
    print(menu)

    secim = input("Seciminiz.")

    if secim == "1":
        kitapAdi = input("Kitap Adi: ")
        kitapEkle(kitapAdi,kitapListesi)
    elif secim == "2":
        kitapCikar()
    elif secim == "3":
        listeler(kitapListesi)
    elif secim == "quit":
        break
    else:
        print("Hatalı girdi")
