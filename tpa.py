import fuzzy1 #memanggil file fuzzy
from fuzzy1 import * #memanggil seluruh isi dari file fuzzy1

#membuat garis singgung antara rendah, sedang dan tinggi

if fuzzy1.z in tpar and fuzzy1.z in tpas:
    hasil5 = set(tpar).intersection(tpas)
    hasil5=sorted(hasil5)
    minimal = min(hasil5)
    maximal = max(hasil5)
    a = minimal
    b = maximal
    hsl9 = (b-fuzzy1.z)/(b-a)
    hsl10 = (fuzzy1.z-a)/(b-a)
    hsl9=round(hsl9,2)
    hsl10=round(hsl10,2)
    print("TPA Kurang Cerdas",hsl9)
    print("TPA Normal", hsl10)

elif fuzzy1.z in tpas and fuzzy1.z in tpat:
    hasil6 = set(tpas).intersection(tpat)
    hasil6=sorted(hasil6)
    minimal = min(hasil6)
    maximal = max(hasil6)
    a = minimal
    b = maximal
    hsl11 = (b-fuzzy1.z)/(b-a)
    hsl12 = (fuzzy1.z-a)/(b-a)
    hsl11=round(hsl11,2)
    hsl12=round(hsl12,2)
    print("TPA Normal", hsl11)
    print("TPA Cerdas", hsl12)