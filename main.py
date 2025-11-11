# 1
def kalitlar_royxati(lugat):
    return list(lugat.keys())

lugat = {"ism": "Ali", "yosh": 20, "shahar": "Toshkent"}
print(kalitlar_royxati(lugat))





# 2
def qiymatlar_yigindisi(lugat):
    return sum(lugat.values())

lugat = {"a": 10, "b": 20, "c": 30}
print(qiymatlar_yigindisi(lugat))





# 3
def kalit_mavjudmi(lugat, kalit):
    return kalit in lugat

lugat = {"ism": "Ali", "yosh": 20}
print(kalit_mavjudmi(lugat, "yosh"))
print(kalit_mavjudmi(lugat, "manzil"))




# 4
def saralangan_qiymatlar(lugat):
    saralangan = dict(sorted(lugat.items(), key=lambda item: item[1]))
    return saralangan

lugat = {"a": 5, "b": 2, "c": 8}
print(saralangan_qiymatlar(lugat))




# 5
def harf_takrorlanishi(matn):
    natija = {}
    for harf in matn:
        natija[harf] = natija.get(harf, 0) + 1
    return natija

print(harf_takrorlanishi("salom"))




# 6
def lugatlarni_birlashtirish(l1, l2):
    yangi = l1.copy()
    yangi.update(l2)
    return yangi

l1 = {"a": 1, "b": 2}
l2 = {"c": 3, "d": 4}
print(lugatlarni_birlashtirish(l1, l2))




# 7
def eng_katta_qiymat(lugat):
    eng_katta = max(lugat, key=lugat.get)
    return eng_katta, lugat[eng_katta]


lugat = {"a": 10, "b": 25, "c": 18}
print(eng_katta_qiymat(lugat))




# 8
def kalit_qiymat_almashish(lugat):
    return {v: k for k, v in lugat.items()}


lugat = {"ism": "Ali", "yosh": 20}
print(kalit_qiymat_almashish(lugat))




# 9
def juft_qiymatlar(lugat):
    yangi = {k: v for k, v in lugat.items() if v % 2 == 0}
    return yangi

lugat = {"a": 1, "b": 2, "c": 4, "d": 7}
print(juft_qiymatlar(lugat))




# 10
def eng_uzun_kalit(lugat):
    eng_uzun = max(lugat, key=len)
    return eng_uzun

lugat = {"ism": "Ali", "familiya": "Valiyev", "yosh": 25}
print(eng_uzun_kalit(lugat))
