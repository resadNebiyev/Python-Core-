users = []
questions = ['Azrbaycanin paytaxti haradir?: ',
'Azərbaycan dövlətinin rəmzləri nələrdir?: ',
'Himnimizin sözləri kimə məxsusdur?: ',
'Azərbaycan Respublikasının rəsmi dili hansı dildir?: ',
'Azərbaycan Respublikasının Valyutası hansı pul vahididir?: ',
]
answers = ["Baki","Bayraq,Gerb,Himn","Əhməd Cavad","Azərbaycan dili","Manat"]

class User:
    def __init__(self,ad,soyad,yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
    def register(self):
        print(f"{self.ad} {self.soyad} Sual-Cavab Oyununa Xoş Gəlmisən!{self.ad},Sənə 5 Sual Veriləcək,Əgər Doğru Cavab Versən Hər Suala Görə 2 Xal Qazanacaqsan,Yanlış Cavab Versən 1 Xal İtirəcəksən")
