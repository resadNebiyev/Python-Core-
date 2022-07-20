# def decorator(f):
#     def inner(*args, **kwargs):
#         result = f(*args,**kwargs)
#         myList = []
#         for i in result:
#             i*=2
#             myList.append(i)
#         return myList
#     return inner
# @decorator
# def showData(par = [10,20,40]):
#     return par


# print(showData([10]))