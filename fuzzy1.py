import numpy #memanggil library numpy untuk mempermudah operasi array

i = input("Masukkan IPK Anda : ")
j = input("Masukkan Toefl Anda : ")
k = input("Masukkan TPA Anda : ")
#---IPK---#

#inisialisasi array
ipkr=[]
ipks=[]
ipkt=[]
#pembuatan grafik dan batas-batasnya
for i in numpy.arange(0, 2.3, 0.1):
    x = i
    x = round(x,2)
    ipkr.append(x)
for i in numpy.arange(1.5, 3.6, 0.1):
    x = i
    x=round(x,2)
    ipks.append(x)

for i in numpy.arange(2.6, 4.0, 0.1):
    x = i
    x=round(x,2)
    ipkt.append(x)

#---Toefl---#

#inisialisasi array
toeflr=[]
toefls=[]
toeflt=[]
#pembuatan grafik dan batas-batasnya
for j in numpy.arange(0, 475, 10):
    y = j
    y = round(y,2)
    toeflr.append(y)
for j in numpy.arange(350, 600, 10):
    y = j
    y=round(y,2)
    toefls.append(y)
for j in numpy.arange(525, 675, 10):
    y = j
    y=round(y,2)
    toeflt.append(y)

#---TPA---#

#inisialisasi array
tpar=[]
tpas=[]
tpat=[]
#pembuatan grafik dan batas-batasnya
for k in numpy.arange(0, 475, 10):
    z = k
    z = round(z,2)
    tpar.append(z)
for k in numpy.arange(250, 750, 10):
    z = k
    z=round(z,2)
    tpas.append(z)
for k in numpy.arange(525, 820, 10):
    z = k
    z = round(z,2)
    tpat.append(z)

"""Defuzzyfication"""
