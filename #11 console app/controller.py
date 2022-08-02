from model import *
def register(ad,soyad,yas):
    user = User(ad,soyad,yas)
    users.append(user)
    user.register()
def askingQuestion():
    point = 0
    for i in range(len(questions)):
        question = input(questions[i])
        if question.lower() == answers[i].lower():
            point+=2
            print(f"Təbriklər! Cavab Doğrudur, Sizin xalınız {point}/10-dir")
        elif question.lower() != answers[i].lower() and point == 0:
            print(f"Təəssüf! Cavab Yanlışdır, Doğru Cavab {answers[i]}, Sizin Xalınız {point}/10-dir")
        else:           
            point-=1
            print(f"Təəssüf! Cavab Yanlışdır, Doğru Cavab {answers[i]}, Sizin Xalınız {point}/10-dir")
            

