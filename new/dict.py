# # car = {"model": "ferrari", "color": "red"}
# # print(car["model"])
# # print(car["color"])

# talaba = {}
# talaba["ism"] = "qobil"
# talaba["age"] = 16
# del talaba["age"]
# # print(talaba)


# translate = {"apple": "olma", "banan": "banan", "pencil": "qalam"}
# # user = input("inglizcha soz kiriitng:")
# # res = translate.get(user,'bunday soz mavjud emas')
# # print(res)

# for kalit, qiymat in translate.items():
#     print(f"kalit: {kalit}")
#     print(f"qiymat: {qiymat} \n")


# bozorlik = ["anor", "uzum", "non", "baliq"]
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")


# mahsulotlar = {
#     "olma": 10000,
#     "anor": 20000,
#     "uzum": 40000,
#     "anjir": 25000,
#     "banan": 30000,
# }
# user = input("mahsulot kiriting:").lower()
# if user in mahsulotlar:
#     print(f"{user.title()} {mahsulotlar[user]} so'm")
# else:
#     print(f"{user.title()} mahsulotidan qolmadi")


# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot)

# print(mahsulotlar.values())


# telefonlar = {
#     "ali": "iphone x",
#     "vali": "galaxy s9",
#     "olim": "mi 10 pro",
#     "orif": "nokia 3310",
#     "hamida": "galaxy s9",
#     "maryam": "huawei p30",
#     "tohir": "iphone x",
#     "umar": "iphone x",
# }

# for tel in set(telefonlar.values()):
#     print(tel)
