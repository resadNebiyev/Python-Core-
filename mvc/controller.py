from model import *
def registerData(ad,soyad):
    user = User(ad,soyad)
    users.append(user)
def showData():
    for user in users:
        user.showData()
    