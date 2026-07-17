# ValueError

# yosh = input("Yoshingizni kiritnf:")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Siz butun son kiritmadiz")
# else:
#     print(f"siz {2026-yosh} yilda tu'gilgansiz")

# print(True)
# print(True)


# ! ZeroDivisionError
# x, y = 5, 10
# try:
#     y / (x - 5)

# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")


# ! IndexError
# mevalar = ["olma", "anor", "anjir", "uzum"]
# try:
#     print(mevalar[4])
# except IndexError:
#     print(f"Ro'yxatda faqar {len(mevalar)}ta mevalar bor ")


# ! KeyError
# user = {
#     "username": "ibroxim",
#     "status": "admin",
#     "email": "ibroxim.dev",
#     "phone": 918220922,
# }

# key = "status"
# try:
#     print(f"Foydalanuvchi {user[key]}")
# except KeyError:
#     print("Bunday kalit mevjud emas")

# ! file
# fileName = "data.txt"
# try:
#     with open(fileName) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(False)


import json

files = ["talaba1.json", "talaba2.json", "talaba3.json", "talaba4.json"]
for fileName in files:
    try:
        with open(fileName) as f:
            talab = json.load(f)
    except FileNotFoundError:
        pass
    else:
        print(talab["ism"])
