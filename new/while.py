#! 1
# son = 1
# while son <= 5:
#     print(son, end="")
#     son += 1

# print("sonni kvadratini aniqlash uchun son kiriting:")
# savol = "son kiriting:"
# savol += "(dastur toxtashi uchun exit deb yozing):"

# while True:
#     qiymat = input(savol)
#     if qiymat == "exit":
#         break
#     else:
#         print(float(qiymat) ** 2)

# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == "exit":
#         ishora = False
#     else:
#         print(float(qiymat) ** 2)


# while qiymat != "exit":
#     qiymat = input(savol)
#     if qiymat != "exit":
#         print(float(qiymat) ** 2)


#! 2
# nums = list(range(1, 11))
# for num in nums:
#     if num == 5:
#         continue
#     print(f"{num} ning kvadrati {num**2}")


# #! 3
# num = 0
# while num <= 10:
#     num += 1
#     if num % 2 != 0:
#         continue
#     else:
#         print(num)


#! 4
# print("do'stlaringiz royxatini tuzamiz.")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n}-do'stingizni ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("yana ism qoshasizmmi? (ha/yo'q)")
#     n += 1
#     if takrorlash != "ha":
#         break
# print("do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

#!  5
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizni ismini kiriting:")
#     yosh = input(f"{ism.title()}ning yoshini kiriting")
#     dostlar[ism] = int(yosh)

#     javob = input("Yana malumot qoshasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
# for ism,yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# * 1
# names = {}
# ishora = True
# while ishora:
#     ism = input("ism kiriting:")
#     names[ism] = str(ism)
#     print(f"salom {ism}")

#     chiqish = input("toxtash ucun STOP yozing:")
#     if chiqish == "stop":
#         ishora: False


# * 2
# ishora = True
# nums = 0
# while ishora:
#     user = int(input("son kiriting:"))
#     nums += user

#     stop = input("dasrutni toxtatishni xoxlaysizmi (ha/yo'q)")
#     if stop == "ha":
#         ishora = False

# print(f"siz kiritgan sonlar yigindisi {nums}")

# * 3
# parol = "python123"
# while True:
#     user = input("Parolni kriting:")
#     if parol == user:
#         print("xush kelibsiz")
#     else:
#         print("parol xato")

# * 4
# while True:
#     user = int(input("musbat son kiriting:"))
#     if user < 0:
#         print("qayat kiriting")
#         break

#     else:
#         print("raxmat")
#     break

# * 5
# num = 100
# while num > 1:
#     if num % 2 == 0:
#         print(num)
#     num -= 1


# * 6
# print("ismlar:")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n}-dostingzini kiritng"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("yana ism qoshasizmi(ha/yoq)")
#     n += 1
#     if takrorlash != "ha":
#         break

# for ism in ismlar:
#     print(ism)


# ? 1
# login = "admin"
# password = "12345"
# limit = 0
# while True:
#     user_login = input("Loginni kiriting: ")
#     user_password = input("Parolni kiriting: ")
#     if user_login == login and user_password == password:
#         print("Xush kelibsiz!")
#         break
#     else:
#         limit += 1
#         if limit == 3:
#             print("Hisob bloklandi!")
#             break
#         print(f"Login yoki parol xato! Yana {3 - limit} ta urinish qoldi.")

# dostlar = {}  
# while True:
#     ism = input("ismin kiritng:")
#     yosh = input(f"{ism.title()}ning yoshini kiriting")
#     dostlar[ism] = int(yosh)

#     javob = input("yana malumot qoshaszmi (ha/yo'q)")
#     if javob == "yo'q":
#         break

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")


# cars = ["lacetti", "nexia", "toyota", "nexia", "audi", "bmw"]
# print(cars)
# while "nexia" in cars:
#     cars.remove("nexia")

# print(cars)


talabalar = ["hasan", "husan", "olim", "botir"]
baholangan_talabaler = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi \n")
    baholangan_talabaler[talaba] = int(baho)
print(baholangan_talabaler)
