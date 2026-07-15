# def toliqIsm(ism, familya):
#     toliq_ism = f"{ism} {familya}"
#     return toliq_ism

# print(toliqIsm("ibroxim","raxmatullayev"))


# def toliqIsm(ism, famliya, otasiningIsmi=""):
#     if otasiningIsmi:
#         toliqIsm = f"{ism} {otasiningIsmi} {famliya}"
#     else:
#         toliqIsm = f"{ism} {famliya}"
#     return toliqIsm.title()


# print(toliqIsm("ibroxim", "raxmatullayev", "farhodivich"))


# def oraliq(min, max, qadam=1):
#     sonlar = []
#     while min <= max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar


# print(oraliq(0, 10))
# print(oraliq(0, 10, 2))
# print(oraliq(5, 20, 5))


# def avtoInfo(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {
#         "kompaniya": kompaniya,
#         "model": model,
#         "rang": rangi,
#         "korobka": korobka,
#         "yil": yili,
#         "narh": narhi,
#     }
#     return avto
# avtolar = []

# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rang = input("Rangi: ")
#     korobka = input("Korobka (mexanika/avtomat): ")
#     yili = int(input("Ishlab chiqarilgan yili: "))
#     narhi = input("Narhi (ixtiyoriy): ")
#     if narhi:
#         narhi = int(narhi)
#     else:
#         narhi = None
#     avto = avtoInfo(kompaniya, model, rang, korobka, yili, narhi)
#     avtolar.append(avto)
#     javob = input("Yana avto qo'shasizmi? (yes/no): ").lower()
#     if javob == "no":
#         break

# print("\nSalonimizdagi avtolar:")

# for avto in avtolar:
#     narhi = avto["narh"] if avto["narh"] else "Noma'lum"
#     print(
#         f"{avto['rang'].title()} "
#         f"{avto['kompaniya'].title()} "
#         f"{avto['model'].title()}, "
#         f"{avto['korobka']} korobka, "
#         f"{avto['yil']}-yil. "
#         f"Narhi: {narhi}"
#     )


# ? task1
# def userInfo(ism, familia, yili, tugilganJoyi, email, telefonRaqam):
#     user = {
#         "ism": ism,
#         "familia": familia,
#         "yili": yili,
#         "tugilganJoyi": tugilganJoyi,
#         "email": email,
#         "telefon": telefonRaqam,
#     }
#     return user

# users = []
# while True:
#     print("\nQuyidagi ma'lumotlarni to'ldiring:")
#     ism = input("Ismingizni kiriting: ")
#     familia = input("Familiyangizni kiriting: ")
#     yil = input("Tug'ilgan yilingiz: ")
#     tugilganJoyi = input("Tug'ilgan joyingiz: ")
#     email = input("Email manzil: ")
#     telefon = input("Telefon raqam: ")
#     if telefon:
#         telefon = int(telefon)
#     else:
#         telefon = None
#     user = userInfo(ism, familia, yil, tugilganJoyi, email, telefon)
#     users.append(user)
#     javob = input("\nYana qo'shasizmi? (yes/no): ")
#     if javob.lower() == "no":
#         break

# print("\nBizning o'quvchilar:")

# for user in users:
#     print(
#         f"{user['ism'].title()} "
#         f"{user['familia'].title()} "
#         f"{user['yili']}-yilda tug'ilgan, "
#         f"Tug'ilgan joyi: {user['tugilganJoyi']}, "
#         f"Email: {user['email']}, "
#         f"Telefon: {user['telefon']}"
#     )


# ? task 2
# def findMax(num1, num2, num3):
#     allNums = [num1, num2, num3]
#     print(max(allNums))

# findMax(1, 2, 3)


# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting")
#         baholar[ism] = int(baho)
#     return baholar


# print(bahola(["hasan", "husan", "mirjon"]))


# ! args
# def summa(*sonlar):
#     return sum(sonlar)


# print(summa(1, 5, 9, 8, 5, 64))


# ! kwargs
def avto_info(kompaniya, model, **malumotar):
    malumotar["kompaniya"] = kompaniya
    malumotar["model"] = model
    return malumotar


avto1 = avto_info("gm", "malibu", rang="qora", yil=2018)
avto2 = avto_info("kia", "k5", rang="qizil", narh=35000, yil=2020)
# print(avto1)
# print(avto2)


# def nums(*nums):
#     res = 1
#     for num in nums:
#         res *= num
#     return res


# print(nums(1, 2, 8))


# def studentsInfo(name, lastname, **datas):
#     datas["name"] = name
#     datas["lastname"] = lastname
#     return datas


# student = studentsInfo(
#     "Ibrohim",
#     "Rahmatullayev",
#     yosh=15,
#     sinf=9,
#     telefon="+998901234567",
#     manzil="Samarqand",
# )
# print(student)


# ? 1
# def allNums(*nums):
#     return sum(nums)
# print(allNums(1, 2, 3, 4, 5, 6, 7))


# ? 2
# def findMax(*nums):
#     res = 0
#     for num in nums:
#         if num > res:
#             res = num
#     return res
# print(findMax(1, 2, 3, 8, 6, 2))


# ? 4
# def userInfo(name, lastName, **args):
#     args["name"] = name
#     args["lastName"] = lastName
#     return args


# print(userInfo("ibroxim", "Raxmatullayev", yosh=16, telefon=918220922, kasb="IT"))


# ? 5
# def subjscts(**subjest):
#     return subjest


# print(subjscts(birinchi="matematika", ikkinchi="ona tili", uchinchi="ingiz tili"))


# # ? 6
# def student(name, **grades):
#     return {"name": name, "grades": grades}


# print(student("Ibrohim", matematika=90, fizika=85, tarix=100))


# ? 7
# def product(name, price, **parts):
#     parts["name"] = name
#     parts["price"] = price
#     return parts


# print(product("iphone16", 1200, color="white", brand="apple"))


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def cars(name, model, year, color, brend):
    car = {"name": name, "model": model, "year": year, "color": color, "brend": brend}
    return car

