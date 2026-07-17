# class Talaba:
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def get_name(self):
#         return self.ism

#     def get_fullname(self):
#         return f"{self.ism} {self.familiya}"

#     def get_age(self, yil):
#         return yil - self.tyil

#     def set_bosqich(self, yangi_bosqich):
#         self.bosqich = yangi_bosqich

#     def update_bosqich(self):
#         self.bosqich += 1

#     def tanishtir(self):
#         return f"Ismim {self.ism} {self.familiya}, Tug'ilgan yilim {self.tyil}, {self.bosqich}-bosqich talabasi"


# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []

#     def add_student(self, talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

#     def get_students(self):
#         return [talaba.get_fullname() for talaba in self.talabalar]


# # Talabalar
# talaba1 = Talaba("Ibrohim", "Rahmatullayev", 2010)
# talaba2 = Talaba("Ali", "Valiyev", 2009)

# # Fan
# fan1 = Fan("Matematika")

# fan1.add_student(talaba1)
# fan1.add_student(talaba2)

# print(fan1.get_students())
# print(fan1.talabalar_soni)


# class Shaxs:
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         info = f"{self.ism}, {self.familiya}."
#         info += f"Passport: {self.passport}, {self.tyil}-yoshda"
#         return info

#     def get_age(self, yil):
#         return yil - self.tyil


# inson = Shaxs("ibroxim", "raxmatullayev", "AAA2222", 2010)
# print(inson.get_info())


# ? telefon
# class Telefon:
#     def __init__(self, model, company, price, xotira):
#         self.model = model
#         self.company = company
#         self.price = price
#         self.xotira = xotira

#     def get_info(self):
#         info = f"{self.model} modeli {self.company} maxsuloti, narxi:{self.price}$ xotirasi:{self.xotira}gb"
#         return info

#     def get_price(self):
#         price = f"Narxi: {self.price}$"
#         return price

#     def set_price(self, new_price):
#         self.price = new_price
#         infoPrice = f"{self.model} maxsuloti  narxi {self.price}$ ga o'gardi "
#         return infoPrice

#     def discount(self, foiz):
#         res = self.price * foiz / 100
#         return res


# tel1 = Telefon("iphone", "apple", 1000, "800")
# print(tel1.discount(5))


# ? 2
# class BankAccount:
#     def __init__(self, name, card_num, balans=0):
#         self.name = name
#         self.card_num = card_num
#         self.balans = balans

#     def deposit(self, card, amount):
#         if card != self.card_num:
#             return f"{card} raqamli karta mavjud emas."

#         if amount <= 0:
#             return "Kiritilgan summa 0 dan katta bo'lishi kerak."

#         self.balans += amount
#         return f"{amount} so'm hisobingizga muvaffaqiyatli qo'shildi."

#     def withdraw(self, card, amount):
#         if card != self.card_num:
#             return f"{card} raqamli karta mavjud emas."
#         if amount <= 0:
#             return "Yechiladigan summa 0 dan katta bo'lishi kerak."
#         if amount > self.balans:
#             return "Hisobingizda mablag' yetarli emas."
#         self.balans -= amount
#         return (
#             f"{amount} so'm muvaffaqiyatli yechildi.\n"
#             f"Qolgan balans: {self.balans} so'm."
#         )

#     def get_balance(self):
#         return self.balans

#     def get_info(self):
#         return (
#             f"Ism: {self.name}\n"
#             f"Karta: {self.card_num}\n"
#             f"Balans: {self.balans} so'm"
#         )

# user = BankAccount("Ibrohim", 56146828, 1000)
# print(user.get_info())
# print()
# print(user.deposit(56146828, 500))
# print("Balans:", user.get_balance())
# print()
# print(user.withdraw(56146828, 300))
# print("Balans:", user.get_balance())
# print()
# print(user.withdraw(56146828, 5000))
# print()
# print(user.deposit(11111111, 500))


# class Shaxs:
#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info

#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil


# class Talaba(Shaxs):
#     """Talaba klassi"""

#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1

#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam

#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich

#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info


# class Shaxs:
#     def __init__(self, ism):
#         self.ism = ism


# class Talaba:
#     def __init__(self, ism, idraqam):
#         self.ism = ism
#         self.idraqam = idraqam


# talaba = Talaba("Ibrohim", 101)

# print(talaba.ism)
# print(talaba.idraqam)


# # ! class
# class Shaxs:
#     def __init__(self, ism):
#         self.ism = ism


# class Talaba(Shaxs):
#     def __init__(self, ism, idraqam):
#         super().__init__(ism)
#         self.idraqam = idraqam


# talaba = Talaba("Ibrohim", 101)

# print(talaba.ism)
# print(talaba.idraqam)


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_info(self):
#         return print(f"{self.name} {self.age} yoshda")


# sher = Animal("sher", 15)
# # print(sher.get_info())


# class Sher(Animal):
#     def __init__(self, name, age, kg):
#         super().__init__(name, age)
#         self.kg = kg

#     def get_info_lion(self):
#         info = super().get_info()
#         return f"{info}, {self.kg} kilogram"

# lion = Sher("sher", 15, 500)
# print(lion.get_info_lion())


# ! Inkapsulyatsiya
# from avtoClass import Avto

# avto1 = Avto("gm", "malinu", "qora", "2015", 2000, 100)
# avto2 = Avto("bmw", "m5", "oq", "2014", 6000, 199900)
# avto3 = Avto("mers", "gelik", "kok", "2010", 5000, 102960)
# print(Avto.get_num_avto())


# ! dunder
# class Avto:
#     __num_avto = 0

#     def __init__(self, make, model, rang, yil, narh):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1

#     def __repr__(self):
#         return f"Avto({self.make}, {self.model})"

#     def __eq__(self, y):
#         return self.narh == y.narh

#     def __lt__(self, y):
#         return self.narh < y.narh

#     def __le__(self, y):
#         return self.narh <= y.narh


# class AvtoSalon:
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"

#     def __getitem__(self, index):
#         return self.avtolar[index]

#     def add_avto(self, *qiymat):
#         for avto in qiymat:
#             if isinstance(avto, Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto kiriting")


# avtoName = AvtoSalon("MaxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
# avto2 = Avto("bmw", "M5", "oq", 2025, 40000)
# avtoName.add_avto(avto1, avto2)
# # print(avtoName[1])


# ? 2
# class Book:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __repr__(self):
#         return f"{self.name} kitobi {self.price} so'm,"


# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.allName = []

#     def __repr__(self):
#         return f"{self.name} kutubxonasi"

#     def get_item(self, index):
#         return self.allName[index]

#     def add_book(self, *value):
#         for book in value:
#             if isinstance(book, Book):
#                 self.allName.append(book)
#             else:
#                 print("Kitib kiritng")

#     def get_info(self):
#         info = f"{self.name}-kutubxonasida quyidgi kitoblar bor: \n {self.allName}"
#         return info


# libraryName = Library("Nur")
# book1 = Book("men", 10000)
# book2 = Book("sir", 30000)
# book3 = Book("aso", 50000)
# libraryName.add_book(book1, book3)
# # print(libraryName.get_item(1))


# class Movie:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __repr__(self):
#         return f"{self.name} filmi - narxi {self.price} so'm"

#     def __call__(self):
#         return f"{self.name} filmi - narxi {self.price} so'm"


# class Cinema:
#     def __init__(self, name):
#         self.name = name
#         self.movies = []

#     def add_film(self, *films):
#         for film in films:
#             if isinstance(film, Movie):
#                 self.movies.append(film)
#             else:
#                 print(f"{film} nomli film mavjud emas")

#     def remove_film(self, name):
#         for movie in self.movies:
#             if movie.name == name:
#                 self.movies.remove(movie)
#                 return
#             else:
#                 print(f"{name} nomli film mavjud emas.")

#     def get_info(self):
#         info = f"Bizni kinolar: \n"
#         for movie in self.movies:
#             info += f"{movie.name} kinosi - {movie.price} so'm, \n"
#         return info


# cinema = Cinema("UZB")
# movie1 = Movie(f"taxlar o'yini", 20000)
# movie2 = Movie(f"breaking bad", 25000)
# movie3 = Movie(f"soul", 1000)
# cinema.add_film(movie1, movie2, movie3)
# cinema.remove_film("soul")
# # print(cinema.get_info())
# print(movie1())
