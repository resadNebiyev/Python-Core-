
# class computer:
#     belongsTo = "Eloctronic device"
#     def __init__(self,name,cpu,ram):
#         self.name = name
#         self.cpu = cpu
#         self.ram = ram
#         self.note = self.my_notebook()
#     #instance method
#     def config(self):
#         print(f"my computer is {self.name}{self.cpu} {self.ram}")
#     @classmethod
#     def typ(cls):
#         print(cls.belongsTo)
#     @staticmethod
#     def info():
#         print("this is computer class")
#     #class inside class
#     class my_notebook:
#         def __init__(self):
#             self.brand = "HP"
#             self.color = "black"
#         def run(self):
#             print(f"{self.brand} is {self.color}")
        
# com1 = computer("HP","Core i3","4GB")
# com1.note.run()


#Inheritance Class
# class A:
#     def run(self):
#         print("i am A class")
# class B(A):
#     def run1(self):
#         print("i am B class")
# obj = B()
# obj.run1()
