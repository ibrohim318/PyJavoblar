import json

bemor = {
    "ism": "ibroxim",
    "yosh": 16,
    "oila": True,
    "farznadlar": ("ahmad", "bonu"),
    "allergiya": None,
    "dorilar": [
        {"nomi": "Analgin", "miqdori": 0.5},
        {"nomi": "Panadol", "miqdori": 1.2},
    ],
}

bemor_json = json.dumps(bemor)
# print(bemor_json)


with open("bemor.json", "w") as f:
    json.dump(bemor, f)

bemor2 = json.loads(bemor_json)


filename = "bemor.json"
with open(filename) as f:
    bemor = json.load(f)
print(type(bemor))
print(bemor)
