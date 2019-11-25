print("Turkiye\'de, cok fazla kedi vardir.") # \' isareti burda kacis olarak kullanilmistir.
print("ilk satir \n ikinci satir") # asagiya gecmek icin kullanilan kacisdir.
print('C:\some\name')  # boyle seyler yazmak istedigimizde  asa satıra gececektir.
print(r'C:\some\name') # r'yi ekledigimizde bu sorundan kurtulacagiz.
print(""" \
Kullanim: goruntule [AYARLAR]
        - h
        - H hostname
        """)
print(3 * 'un' + 'ium')
print('Py''thon') #birlesik olarak yazilir.
yazi = ("Burada olanlar yazi degiskenine tanimlanmistir.")
print(yazi)
deg1='Py'
deg2='thon'
print(deg1+deg2)
kelime = 'Python'
print(kelime[0]) #kelimenin 0'inci indexini bastirir.
print(kelime[5]) #kelimenin 5'inci indexine bastirir.
print(kelime[-1]) #tersden -1inciyi basar yani [5]'se denk gelir.
print(kelime[-6]) #basa donmeye baslar artik
print(kelime[0:2]) #0 ile 2 arasini yazdir.
print(kelime[:2]) #bastan ikiye kadar bastir.
print(kelime[2:]) #bastan ikiyi yazdirma
print(kelime[:4] + kelime[4:]) #oncesi ve sonrasini yazdirinca tam yazi olur hep
print(kelime[4:]) 
print("""
+---+---+---+---+---+----+
| P | y | t | h | o | n  |
+---+---+---+---+---+----+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

""")
#print(kelime[-10]) hata aliriz range'de cikiyoruz.
print(kelime[4:42]) # 4 ile 42 arasini yazdirir. hata vermez
print(kelime[42:]) #42 'ye kadar yazdirma hata vermez bos doner
# kelime[0] = 'J' #obje hatasi verir
print('J' + kelime[1:]) #1'den sonrasini yazdirip basaa j ekleyme icin.
