# 29
class Osimlik:
    def __init__(self, nom, turi):
        self.nom = nom
        self.turi = turi


class Bog:
    def __init__(self):
        self.osimliklar = []

    def osimlik_qosh(self, osimlik):
        self.osimliklar.append(osimlik)

    def tur_osimliklari(self, tur):
        return [o.nom for o in self.osimliklar if o.turi == tur]


o1 = Osimlik("Olma", "Meva")
o2 = Osimlik("Nok", "Meva")
o3 = Osimlik("Atirgul", "Gul")

bog = Bog()
bog.osimlik_qosh(o1)
bog.osimlik_qosh(o2)
bog.osimlik_qosh(o3)

print(bog.tur_osimliklari("Meva"))


# 30
class Sayohatchi:
    def __init__(self, ism):
        self.ism = ism
        self.manzillar = []

    def manzil_qosh(self, manzil):
        self.manzillar.append(manzil)

    def sayohatlar_soni(self):
        return len(self.manzillar)


s1 = Sayohatchi("Ali")

s1.manzil_qosh("Toshkent")
s1.manzil_qosh("Samarqand")
s1.manzil_qosh("Buxoro")

print("Ism:", s1.ism)
print("Sayohatlar soni:", s1.sayohatlar_soni())
print("Manzillar:", s1.manzillar)
