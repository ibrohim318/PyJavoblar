#! 1
# car0 = {
#     "model": "lacetti",
#     "color": "oq",
#     "yil": 2018,
#     "narh": 130000,
#     "km": 50000,
# }

# car1 = {
#     "model": "nexia 3",
#     "color": "qora",
#     "yil": 2015,
#     "narh": 9000,
#     "km": 89000,
# }

# car2 = {
#     "model": "gentra",
#     "color": "qizil",
#     "yil": 2019,
#     "narh": 130000,
#     "km": 50000,
# }


# cars = [car0, car1, car2]
# for car in cars:
#     print(
#         f"{car["model"].title()}, {car["color"]}-rang, {car["yil"]}-yil, {car["narh"]}$"
#     )


#! 2
# malibus = []
# for n in range(10):
#     newCar = {
#         "model": "malibu",
#         "rang": None,
#         "yil": 2020,
#         "narh": None,
#         "km": 0,
#         "korobka": "avto",
#     }
#     malibus.append(newCar)


# for malibu in malibus[:3]:
#     malibu["rang"] = "qizil"

# for malibu in malibus[3:6]:
#     malibu["rang"] = "qora"

# for malibu in malibus[6:]:
#     malibu["rang"] = "qora"
#     malibu["korobka"] = "mexanika"

# for malibu in malibus:
#     if malibu["korobka"] == "avto":
#         malibu["narh"] = 40000
#     else:
#         malibu["narh"] = 35000

# for malibu in malibus:
#     print(malibu)


#! 3
# dasturchilar = {
#     "ali": ["python", "c++"],
#     "vali": ["html", "css", "js"],
#     "hasan": ["php", "sql"],
#     "husan": ["php", "ptyhon"],
#     "maryam": ["c++", "c#"],
# }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi tillarni biladi:")
#     for til in tillar:
#         print(f"{til.upper()}  ",end='')


# ? task
davlatlar = [
    {"name": "Uzbekistan", "hudud": "448978", "aholi": 3300000, "puli": "so'm"},
    {"name": "Russia", "hudud": "17098246", "aholi": 1440000, "puli": "rubl"},
    {"name": "AQSh", "hudud": "17098248", "aholi": 325774848555, "puli": "dollar"},
]

for davlat in davlatlar:
    print(f"{davlat["name"]} davlati, \n {davlat["hudud"]} kv.km, \n {davlat['aholi']} kishi,\n {davlat["puli"]}")
