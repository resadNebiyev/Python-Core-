users = []
class User:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad
    def showData(self):
        print(f"ad:{self.ad} soyad:{self.soyad}")
    
        