# class Human:
#     def __init__(self,ad,soyad):
#         self.ad = ad
#         self.soyad = soyad
#     def printSome(self):
#         print("i am extra method")
#     def __call__(self):
#         print(self.__module__)

# a = Human('assa','sss')
# a()


# # class CustomList(list):
# #     def __init__(self):
# #         super().__init__()
# #     def multiple(self,n):
# #         myList = []
# #         for i in self:
# #             myList.append(i*n)
# #         return myList
    
# # newList = CustomList()
# # newList.append(2)
# # newList.append(4)
# # newList.append(6)
# # newList.multiple(2)
# # print(newList.multiple(3))
# # print(newList)

# class CustomTuple(tuple):
#     def __init__(self) -> None:
#         super().__init__()
#     def append(self,n):
#         mylist = list(self)
#         mylist.append(n)
#         return tuple(mylist)
        
# newTuple = CustomTuple()
# newTuple.append(2)
# print(newTuple.append(2))

