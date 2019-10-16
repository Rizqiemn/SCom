import fuzzy1 #memanggil file fuzzy
from fuzzy1 import * #memanggil seluruh isi dari file fuzzy1


#membuat garis singgung antara rendah, sedang dan tinggi

if fuzzy1.x in ipkr and fuzzy1.x in ipks:
    hasil1 = set(ipkr).intersection(ipks)
    hasil1 = sorted(hasil1)
    minimal = min(hasil1)
    maximal = max(hasil1)
    a = minimal
    b = maximal
    hsl1 = (b-fuzzy1.x)/(b-a)
    hsl2 = (fuzzy1.x-a)/(b-a)
    hsl1=round(hsl1 , 2)
    hsl2=round(hsl2 , 2)
    print("IPK Kecil =", hsl1)
    print("IPK Sedang", hsl2)

elif fuzzy1.x in ipks and fuzzy1.x in ipkt:
    hasil2 = set(ipks).intersection(ipkt)
    hasil2 = sorted(hasil2)
    minimal = min(hasil2)
    maximal = max(hasil2)
    a = minimal
    b = maximal
    hsl3 = (b-fuzzy1.x)/(b-a)
    hsl4 = (fuzzy1.x-a)/(b-a)
    hsl3=round(hsl3,2)
    hsl4=round(hsl4,2)
    print("IPK Sedang", hsl3)
    print("IPK Tinggi", hsl4)
