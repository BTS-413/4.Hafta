karesi = [1,4,9,16,25]
print(karesi)
print(karesi[0])
print(karesi[-1])
print(karesi[-3:])
print(karesi[:])
print(karesi + [36,49]) #listeler toplanir.

kup = [1,8,27,65,125]
print(kup[3])
kup.append(216)
kup.append(7 ** 3)
print(kup)

harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
harfler[2:5] = ['C','D','E'] #liste arasindan belirli yerden degisim ypmak icin
print(harfler)
harfler[2:5] = [] #bosa atayarak cikarma islemi yaptik.
print(harfler)
print(len(harfler))
a = ['a','b','c']
n = [ 1 ,2  ,3]
x = [a, n] #listeler ic ice olusturabiliriz.
print(x[0]) #0'nci liste
print(x[1]) #1'nci liste
print(x[0][1]) #0'nci listenin 1'in elemani
print(x[1][0]) #1'nci listenin 0'nci listesi
x,z = 0 ,1
while x < 10:
    print(x)
    x,z = z, x+z
