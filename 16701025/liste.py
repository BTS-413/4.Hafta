#ogrenciler = list()
#derslist = ["abc",2,10,5]  #listelere ekleme yapilabilir.cikartilabilir.

derslist = ["matematik","fizik","bioloji","kimya"]  #listelere ekleme yapilabilir.cikartilabilir.

string = "a"
string += "b"

for i in derslist:
    print("Ders adi: {}".format(i))
ekle = input("Kitap Adi:")

#derslist.append(ekle)
derslist += [ekle] #+= ile eklenmesi -= ile cikarilacagi anlamina gelmez
print(derslist)
print(string)
#string = str()


