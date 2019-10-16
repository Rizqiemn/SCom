import fuzzy1 #memanggil file fuzzy
from fuzzy1 import * #memanggil seluruh isi dari file fuzzy1

#membuat garis singgung antara rendah, sedang dan tinggi

if fuzzy1.y in toeflr and fuzzy1.y in toefls:
    hasil3 = set(toeflr).intersection(toefls)
    hasil3=sorted(hasil3)
    minimal = min(hasil3)
    maximal = max(hasil3)
    a = minimal
    b = maximal
    hsl5 = (b-fuzzy1.y)/(b-a)
    hsl6 = (fuzzy1.y-a)/(b-a)
    hsl5=round(hsl5,2)
    hsl6=round(hsl6,2)
    print("Toefl Kecil", hsl5)
    print("Toefl Sedang", hsl6)
elif fuzzy1.y in toefls and fuzzy1.y in toeflt:
    hasil4 = set(toefls).intersection(toeflt)
    hasil4=sorted(hasil4)
    minimal = min(hasil4)
    maximal = max(hasil4)
    a = minimal
    b = maximal
    hsl7 = (b-fuzzy1.y)/(b-a)
    hsl8 = (fuzzy1.y-a)/(b-a)
    hsl7=round(hsl7,2)
    hsl8=round(hsl8,2)
    print("Toefl Sedang", hsl7)
    print("Toefl Besar", hsl8)
