from IPK import * #memanggil seluruh isi file ipk
from tpa import * #memanggil seluruh isi file tpa
from toefl import * #memanggil seluruh isi file toefl

# Inferency #

# ipk = hsl1 sampai hsl4
# toefl = hsl5 sampai hsl8
# tpa = hsl9 sampai hsl12

#membuat variabel dengan isian

sk1 = "Kurang Layak"
sk2 = "Layak"
sk3 = "Sangat layak"

"""
membuat rule untuk inferensi
melakukan pengecekan kurang layak, layak, sangat layak. 
"""

if (ipkr is hsl1):
    print(sk1)
if (ipkr is hsl2):
    print(sk1)
elif (ipks is hsl1):
    print(sk2)
elif (ipks is hsl2):
    print(sk2)
elif (ipks is hsl3):
    print(sk2)
elif (ipks is hsl4):
    print(sk2)
elif (ipkt is hsl3):
    print(sk3)
elif (ipkt is hsl4):
    print(sk3)
elif (toeflr is hsl5):
    print(sk1)
elif (toeflr is hsl6):
    print(sk1)
elif (toefls is hsl5):
    print(sk2)
elif (toefls is hsl6):
    print(sk2)
elif (toefls is hsl7):
    print(sk2)
elif (toefls is hsl8):
    print(sk2)
elif (toeflt is hsl7):
    print(sk3)
elif (toeflt is hsl8):
    print(sk3)
elif (tpar is hsl9):
    print(sk1)
elif (tpar is hsl10):
    print(sk1)
elif (tpas is hsl11):
    print(sk2)
elif (tpas is hsl12):
    print(sk2)
elif (tpat is hsl11):
    print(sk3)
elif (tpat is hsl12):
    print(sk3)
elif (ipkr is hsl1) & (toeflr is hsl5):
    print(sk1)
elif (ipkr is hsl1) & (toeflr is hsl6):
    print(sk1)
elif (ipkr is hsl2) & (toeflr is hsl5):
    print(sk1)
elif (ipkr is hsl2) & (toeflr is hsl6):
    print(sk1)
elif (ipkr is hsl1) & (toefls is hsl5):
    print(sk1)
elif (ipkr is hsl1) & (toefls is hsl6):
    print(sk1)
elif (ipkr is hsl2) & (toefls is hsl5):
    print(sk1)
elif (ipkr is hsl2) & (toefls is hsl6):
    print(sk1)
elif (ipks is hsl1) & (toeflr is hsl5):
    print(sk1)
elif (ipks is hsl1) & (toeflr is hsl6):
    print(sk1)
elif (ipks is hsl2) & (toeflr is hsl5):
    print(sk1)
elif (ipks is hsl2) & (toeflr is hsl6):
    print(sk1)
elif (ipks is hsl3) & (toefls is hsl5):
    print(sk2)
elif (ipks is hsl3) & (toefls is hsl6):
    print(sk2)
elif (ipks is hsl4) & (toefls is hsl5):
    print(sk2)
elif (ipks is hsl4) & (toefls is hsl6):
    print(sk2)
elif (ipks is hsl3) & (toeflt is hsl7):
    print(sk2)
elif (ipks is hsl3) & (toeflt is hsl8):
    print(sk2)
elif (ipks is hsl4) & (toeflt is hsl7):
    print(sk2)
elif (ipks is hsl4) & (toeflt is hsl8):
    print(sk2)
elif (ipkt is hsl3) & (toefls is hsl5):
    print(sk3)
elif (ipkt is hsl3) & (toefls is hsl6):
    print(sk3)
elif (ipkt is hsl4) & (toefls is hsl5):
    print(sk3)
elif (ipkt is hsl4) & (toefls is hsl6):
    print(sk3)
elif (ipkt is hsl3) & (toeflt is hsl7):
    print(sk3)
elif (ipkt is hsl3) & (toeflt is hsl8):
    print(sk3)
elif (ipkt is hsl4) & (toeflt is hsl7):
    print(sk3)
elif (ipkt is hsl4) & (toeflt is hsl8):
    print(sk3)
elif (ipkr is hsl1) & (tpar is hsl9):
    print(sk1)
elif (ipkr is hsl1) & (tpar is hsl10):
    print(sk1)
elif (ipkr is hsl2) & (tpar is hsl9):
    print(sk1)
elif (ipkr is hsl2) & (tpar is hsl10):
    print(sk1)
elif (ipkr is hsl1) & (tpas is hsl9):
    print(sk1)
elif (ipkr is hsl1) & (tpas is hsl10):
    print(sk1)
elif (ipkr is hsl2) & (tpas is hsl9):
    print(sk1)
elif (ipkr is hsl2) & (tpas is hsl10):
    print(sk1)
elif (ipks is hsl1) & (tpar is hsl9):
    print(sk1)
elif (ipks is hsl1) & (tpar is hsl10):
    print(sk1)
elif (ipks is hsl2) & (tpar is hsl9):
    print(sk1)
elif (ipks is hsl2) & (tpar is hsl10):
    print(sk1)
elif (ipks is hsl3) & (tpas is hsl9):
    print(sk2)
elif (ipks is hsl3) & (tpas is hsl10):
    print(sk2)
elif (ipks is hsl4) & (tpas is hsl9):
    print(sk2)
elif (ipks is hsl4) & (tpas is hsl10):
    print(sk2)
elif (ipks is hsl3) & (tpat is hsl11):
    print(sk2)
elif (ipks is hsl3) & (tpat is hsl12):
    print(sk2)
elif (ipks is hsl4) & (tpat is hsl11):
    print(sk2)
elif (ipks is hsl4) & (tpat is hsl12):
    print(sk2)
elif (ipkt is hsl3) & (tpas is hsl9):
    print(sk3)
elif (ipkt is hsl3) & (tpas is hsl10):
    print(sk3)
elif (ipkt is hsl4) & (tpas is hsl9):
    print(sk3)
elif (ipkt is hsl4) & (tpas is hsl10):
    print(sk3)
elif (ipkt is hsl3) & (tpat is hsl11):
    print(sk3)
elif (ipkt is hsl3) & (tpat is hsl12):
    print(sk3)
elif (ipkt is hsl4) & (tpat is hsl11):
    print(sk3)
elif (ipkt is hsl4) & (tpat is hsl12):
    print(sk3)
elif (toeflr is hsl5) & (tpar is hsl9):
    print(sk1)
elif (toeflr is hsl5) & (tpar is hsl10):
    print(sk1)
elif (toeflr is hsl6) & (tpar is hsl9):
    print(sk1)
elif (toeflr is hsl6) & (tpar is hsl10):
    print(sk1)
elif (toeflr is hsl5) & (tpas is hsl9):
    print(sk1)
elif (toeflr is hsl5) & (tpas is hsl10):
    print(sk1)
elif (toeflr is hsl6) & (tpas is hsl9):
    print(sk1)
elif (toeflr is hsl6) & (tpas is hsl10):
    print(sk1)
elif (toefls is hsl5) & (tpar is hsl9):
    print(sk1)
elif (toefls is hsl5) & (tpar is hsl10):
    print(sk1)
elif (toefls is hsl6) & (tpar is hsl9):
    print(sk1)
elif (toefls is hsl6) & (tpar is hsl10):
    print(sk1)
elif (toefls is hsl7) & (tpas is hsl9):
    print(sk2)
elif (toefls is hsl7) & (tpas is hsl10):
    print(sk2)
elif (toefls is hsl8) & (tpas is hsl9):
    print(sk2)
elif (toefls is hsl8) & (tpas is hsl10):
    print(sk2)
elif (toefls is hsl7) & (tpat is hsl11):
    print(sk2)
elif (toefls is hsl7) & (tpat is hsl12):
    print(sk2)
elif (toefls is hsl8) & (tpat is hsl11):
    print(sk2)
elif (toefls is hsl8) & (tpat is hsl12):
    print(sk2)
elif (toeflt is hsl7) & (tpas is hsl9):
    print(sk3)
elif (toeflt is hsl7) & (tpas is hsl10):
    print(sk3)
elif (toeflt is hsl8) & (tpas is hsl9):
    print(sk3)
elif (toeflt is hsl8) & (tpas is hsl10):
    print(sk3)
elif (toeflt is hsl7) & (tpat is hsl11):
    print(sk3)
elif (toeflt is hsl7) & (tpat is hsl12):
    print(sk3)
elif (toeflt is hsl8) & (tpat is hsl11):
    print(sk3)
elif (toeflt is hsl8) & (tpat is hsl12):
    print(sk3)
elif (ipkr is hsl1) & (toeflr is hsl5) & (tpar is hsl9):
    print(sk1)
elif (ipkr is hsl1) & (toeflr is hsl5) & (tpar is hsl10):
    print(sk1)
elif (ipkr is hsl1) & (toeflr is hsl6) & (tpar is hsl9):
    print(sk1)
elif (ipkr is hsl1) & (toeflr is hsl6) & (tpar is hsl10):
    print(sk1)
elif (ipkr is hsl2) & (toeflr is hsl5) & (tpar is hsl9):
    print(sk1)
elif (ipkr is hsl2) & (toeflr is hsl5) & (tpar is hsl10):
    print(sk1)
elif (ipkr is hsl2) & (toeflr is hsl6) & (tpar is hsl9):
    print(sk1)
elif (ipkr is hsl2) & (toeflr is hsl6) & (tpar is hsl10):
    print(sk1)
elif (ipkr is hsl1) & (toeflr is hsl5) & (tpas is hsl9):
    print(sk1)
elif (ipkr is hsl1) & (toeflr is hsl5) & (tpas is hsl10):
    print(sk1)
elif (ipkr is hsl1) & (toeflr is hsl6) & (tpas is hsl9):
    print(sk1)
elif (ipkr is hsl1) & (toeflr is hsl6) & (tpas is hsl10):
    print(sk1)
elif (ipkr is hsl2) & (toeflr is hsl5) & (tpas is hsl9):
    print(sk1)
elif (ipkr is hsl2) & (toeflr is hsl5) & (tpas is hsl10):
    print(sk1)
elif (ipkr is hsl2) & (toeflr is hsl6) & (tpas is hsl9):
    print(sk1)
elif (ipkr is hsl2) & (toeflr is hsl6) & (tpas is hsl10):
    print(sk1)
elif (ipkr is hsl1) & (toefls is hsl5) & (tpar is hsl9):
    print(sk1)
elif (ipkr is hsl1) & (toefls is hsl5) & (tpar is hsl10):
    print(sk1)
elif (ipkr is hsl1) & (toefls is hsl6) & (tpar is hsl9):
    print(sk1)
elif (ipkr is hsl1) & (toefls is hsl6) & (tpar is hsl10):
    print(sk1)
elif (ipkr is hsl2) & (toefls is hsl5) & (tpar is hsl9):
    print(sk1)
elif (ipkr is hsl2) & (toefls is hsl5) & (tpar is hsl10):
    print(sk1)
elif (ipkr is hsl2) & (toefls is hsl6) & (tpar is hsl9):
    print(sk1)
elif (ipkr is hsl2) & (toefls is hsl6) & (tpar is hsl10):
    print(sk1)
elif (ipkr is hsl1) & (toefls is hsl5) & (tpas is hsl9):
    print(sk1)
elif (ipkr is hsl1) & (toefls is hsl5) & (tpas is hsl10):
    print(sk1)
elif (ipkr is hsl1) & (toefls is hsl6) & (tpas is hsl9):
    print(sk1)
elif (ipkr is hsl1) & (toefls is hsl6) & (tpas is hsl10):
    print(sk1)
elif (ipkr is hsl2) & (toefls is hsl5) & (tpas is hsl9):
    print(sk1)
elif (ipkr is hsl2) & (toefls is hsl5) & (tpas is hsl10):
    print(sk1)
elif (ipkr is hsl2) & (toefls is hsl6) & (tpas is hsl9):
    print(sk1)
elif (ipkr is hsl2) & (toefls is hsl6) & (tpas is hsl10):
    print(sk1)
elif (ipks is hsl1) & (toeflr is hsl5) & (tpar is hsl9):
    print(sk1)
elif (ipks is hsl1) & (toeflr is hsl5) & (tpar is hsl10):
    print(sk1)
elif (ipks is hsl1) & (toeflr is hsl6) & (tpar is hsl9):
    print(sk1)
elif (ipks is hsl1) & (toeflr is hsl6) & (tpar is hsl10):
    print(sk1)
elif (ipks is hsl2) & (toeflr is hsl5) & (tpar is hsl9):
    print(sk1)
elif (ipks is hsl2) & (toeflr is hsl5) & (tpar is hsl10):
    print(sk1)
elif (ipks is hsl2) & (toeflr is hsl6) & (tpar is hsl9):
    print(sk1)
elif (ipks is hsl2) & (toeflr is hsl6) & (tpar is hsl10):
    print(sk1)
elif (ipks is hsl1) & (toeflr is hsl5) & (tpas is hsl9):
    print(sk2)
elif (ipks is hsl1) & (toeflr is hsl5) & (tpas is hsl10):
    print(sk2)
elif (ipks is hsl1) & (toeflr is hsl6) & (tpas is hsl9):
    print(sk2)
elif (ipks is hsl1) & (toeflr is hsl6) & (tpas is hsl10):
    print(sk2)
elif (ipks is hsl2) & (toeflr is hsl5) & (tpas is hsl9):
    print(sk2)
elif (ipks is hsl2) & (toeflr is hsl5) & (tpas is hsl10):
    print(sk2)
elif (ipks is hsl2) & (toeflr is hsl6) & (tpas is hsl9):
    print(sk2)
elif (ipks is hsl2) & (toeflr is hsl6) & (tpas is hsl10):
    print(sk2)
elif (ipks is hsl1) & (toefls is hsl5) & (tpar is hsl9):
    print(sk2)
elif (ipks is hsl1) & (toefls is hsl5) & (tpar is hsl10):
    print(sk2)
elif (ipks is hsl1) & (toefls is hsl6) & (tpar is hsl9):
    print(sk2)
elif (ipks is hsl1) & (toefls is hsl6) & (tpar is hsl10):
    print(sk2)
elif (ipks is hsl2) & (toefls is hsl5) & (tpar is hsl9):
    print(sk2)
elif (ipks is hsl2) & (toefls is hsl5) & (tpar is hsl10):
    print(sk2)
elif (ipks is hsl2) & (toefls is hsl6) & (tpar is hsl9):
    print(sk2)
elif (ipks is hsl2) & (toefls is hsl6) & (tpar is hsl10):
    print(sk2)
elif (ipks is hsl1) & (toefls is hsl5) & (tpas is hsl9):
    print(sk2)
elif (ipks is hsl1) & (toefls is hsl5) & (tpas is hsl10):
    print(sk2)
elif (ipks is hsl1) & (toefls is hsl6) & (tpas is hsl9):
    print(sk2)
elif (ipks is hsl1) & (toefls is hsl6) & (tpas is hsl10):
    print(sk2)
elif (ipks is hsl2) & (toefls is hsl5) & (tpas is hsl9):
    print(sk2)
elif (ipks is hsl2) & (toefls is hsl5) & (tpas is hsl10):
    print(sk2)
elif (ipks is hsl2) & (toefls is hsl6) & (tpas is hsl9):
    print(sk2)
elif (ipks is hsl2) & (toefls is hsl6) & (tpas is hsl10):
    print(sk2)
elif (ipks is hsl3) & (toefls is hsl7) & (tpat is hsl11):
    print(sk2)
elif (ipks is hsl3) & (toefls is hsl7) & (tpat is hsl12):
    print(sk2)
elif (ipks is hsl3) & (toefls is hsl8) & (tpat is hsl11):
    print(sk2)
elif (ipks is hsl3) & (toefls is hsl8) & (tpat is hsl12):
    print(sk2)
elif (ipks is hsl4) & (toefls is hsl7) & (tpat is hsl11):
    print(sk2)
elif (ipks is hsl4) & (toefls is hsl7) & (tpat is hsl12):
    print(sk2)
elif (ipks is hsl4) & (toefls is hsl8) & (tpat is hsl11):
    print(sk2)
elif (ipks is hsl4) & (toefls is hsl8) & (tpat is hsl12):
    print(sk2)
elif (ipks is hsl3) & (toeflt is hsl7) & (tpas is hsl11):
    print(sk2)
elif (ipks is hsl3) & (toeflt is hsl7) & (tpas is hsl12):
    print(sk2)
elif (ipks is hsl3) & (toeflt is hsl8) & (tpas is hsl11):
    print(sk2)
elif (ipks is hsl3) & (toeflt is hsl8) & (tpas is hsl12):
    print(sk2)
elif (ipks is hsl4) & (toeflt is hsl7) & (tpas is hsl11):
    print(sk2)
elif (ipks is hsl4) & (toeflt is hsl7) & (tpas is hsl12):
    print(sk2)
elif (ipks is hsl4) & (toeflt is hsl8) & (tpas is hsl11):
    print(sk2)
elif (ipks is hsl4) & (toeflt is hsl8) & (tpas is hsl12):
    print(sk2)
elif (ipkt is hsl3) & (toefls is hsl5) & (tpas is hsl9):
    print(sk2)
elif (ipkt is hsl3) & (toefls is hsl5) & (tpas is hsl10):
    print(sk2)
elif (ipkt is hsl3) & (toefls is hsl6) & (tpas is hsl9):
    print(sk2)
elif (ipkt is hsl3) & (toefls is hsl6) & (tpas is hsl10):
    print(sk2)
elif (ipkt is hsl4) & (toefls is hsl5) & (tpas is hsl9):
    print(sk2)
elif (ipkt is hsl4) & (toefls is hsl5) & (tpas is hsl10):
    print(sk2)
elif (ipkt is hsl4) & (toefls is hsl6) & (tpas is hsl9):
    print(sk2)
elif (ipkt is hsl4) & (toefls is hsl6) & (tpas is hsl10):
    print(sk2)
elif (ipks is hsl3) & (toeflt is hsl7) & (tpat is hsl11):
    print(sk3)
elif (ipks is hsl3) & (toeflt is hsl7) & (tpat is hsl12):
    print(sk3)
elif (ipks is hsl3) & (toeflt is hsl8) & (tpat is hsl11):
    print(sk3)
elif (ipks is hsl3) & (toeflt is hsl8) & (tpat is hsl12):
    print(sk3)
elif (ipks is hsl4) & (toeflt is hsl7) & (tpat is hsl11):
    print(sk3)
elif (ipks is hsl4) & (toeflt is hsl7) & (tpat is hsl12):
    print(sk3)
elif (ipks is hsl4) & (toeflt is hsl8) & (tpat is hsl11):
    print(sk3)
elif (ipks is hsl4) & (toeflt is hsl8) & (tpat is hsl12):
    print(sk3)
elif (ipkt is hsl3) & (toefls is hsl5) & (tpat is hsl11):
    print(sk3)
elif (ipkt is hsl3) & (toefls is hsl5) & (tpat is hsl12):
    print(sk3)
elif (ipkt is hsl3) & (toefls is hsl6) & (tpat is hsl11):
    print(sk3)
elif (ipkt is hsl3) & (toefls is hsl6) & (tpat is hsl12):
    print(sk3)
elif (ipkt is hsl4) & (toefls is hsl5) & (tpat is hsl11):
    print(sk3)
elif (ipkt is hsl4) & (toefls is hsl5) & (tpat is hsl12):
    print(sk3)
elif (ipkt is hsl4) & (toefls is hsl6) & (tpat is hsl11):
    print(sk3)
elif (ipkt is hsl4) & (toefls is hsl6) & (tpat is hsl12):
    print(sk3)
elif (ipkt is hsl3) & (toeflt is hsl7) & (tpas is hsl9):
    print(sk3)
elif (ipkt is hsl3) & (toeflt is hsl7) & (tpas is hsl10):
    print(sk3)
elif (ipkt is hsl3) & (toeflt is hsl8) & (tpas is hsl9):
    print(sk3)
elif (ipkt is hsl3) & (toeflt is hsl8) & (tpas is hsl10):
    print(sk3)
elif (ipkt is hsl4) & (toeflt is hsl7) & (tpas is hsl9):
    print(sk3)
elif (ipkt is hsl4) & (toeflt is hsl7) & (tpas is hsl10):
    print(sk3)
elif (ipkt is hsl4) & (toeflt is hsl8) & (tpas is hsl9):
    print(sk3)
elif (ipkt is hsl4) & (toeflt is hsl8) & (tpas is hsl10):
    print(sk3)
elif (ipkt is hsl3) & (toeflt is hsl7) & (tpat is hsl11):
    print(sk3)
elif (ipkt is hsl3) & (toeflt is hsl7) & (tpat is hsl12):
    print(sk3)
elif (ipkt is hsl3) & (toeflt is hsl8) & (tpat is hsl11):
    print(sk3)
elif (ipkt is hsl3) & (toeflt is hsl8) & (tpat is hsl12):
    print(sk3)
elif (ipkt is hsl4) & (toeflt is hsl7) & (tpat is hsl11):
    print(sk3)
elif (ipkt is hsl4) & (toeflt is hsl7) & (tpat is hsl12):
    print(sk3)
elif (ipkt is hsl4) & (toeflt is hsl8) & (tpat is hsl11):
    print(sk3)
elif (ipkt is hsl4) & (toeflt is hsl8) & (tpat is hsl12):
    print(sk3)



