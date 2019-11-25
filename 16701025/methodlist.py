zel = [4, 1, 5, 2, 10, 4]
print(zel.index(2)) #numaranin index adresini verir
print(zel.index(4,2)) #aramaya 2ci indexden basla dedik ve bize sondaki 4'u verdi.
randlis = [4,1,5,2,10,8]
print(randlis.count(5)) #listede kac adet bes oldugnu bulur.
s = [8,4,5,2,7]
s.sort() #siralama islemi yapar
print(s)
s.sort(reverse=True)
print(s)#tersden siralar
s.append(8) #listeye ekleme yaptik
print(s)
s.remove(5) #listeden silme islemei
print(s)
s.pop(0) #index numarasi vererek silme islemi
print(s)
s.extend([4,5,6])#listeye coklu eleman ekleme
print(s)
s.insert(4,[1,2]) #listeye liste ekleme. indexi 4 olan yere listeyi ekler
print(s)
del s[1] #indexi 1 olan elemani siler.
print(s)
"""
a[start:end:step]
a[start:end] 
a[:] 

"""

