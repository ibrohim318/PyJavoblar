# ! 1
# class Talaba:
#     def __init__(self, name, lastName, age):
#         self.name = name
#         self.lastName = lastName
#         self.age = age

#     def get_info(self):
#         info = f"{self.name} {self.lastName}, {self.age} yosh"
#         return info


# user = Talaba("Ibroxim", "Raxmatullayev", 15)
# print(user.get_info())

# ! 4
# import math


# class Doira:
#     def __init__(self, radius):
#         self.radius = radius

#     def diametr(self):
#         res = 2 * int(self.radius)
#         info = f"Doiraning diametri {res}"
#         return info

#     def perimetr(self):
#         res = 2 * math.pi * self.radius
#         info = f"Doiraning perimetri {res}"
#         return info

#     def yuza(self):
#         res = math.pi * self.radius * self.radius
#         info = f"Doiraning yuzasi {res}"
#         return info


# doira = Doira(5)
# print(doira.diametr())
# print(doira.perimetr())
# print(doira.yuza())


# ! 6
# class Bank:
#     def __init__(self, owner, balans, creditCard):
#         self.owner = owner
#         self.balans = balans or 0
#         self.creditCard = creditCard

#     def pul_qosh(self, summa, userCard):
#         if userCard == self.creditCard:
#             self.balans += summa
#             print(
#                 f"Hisobingizga {summa} so'm pul tushdi, hozirda balansingizda {self.balans} so'm pul bor"
#             )
#         else:
#             print(f"{userCard} raqamli plastik karta yo'q")


# user1 = Bank("Ibroxim", 1000, 56146828)
# user2 = Bank("Ibroxim", 1000, 56146829)
# user3 = Bank("Ibroxim", 1000, 56146830)
# print(user1.pul_qosh(3000, 5614688))


# ! 7
