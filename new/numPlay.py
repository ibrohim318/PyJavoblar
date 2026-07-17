import random

#  num = r.randint(0, 100)
# print(num)
# while True:
#     userNum = input(f"\n Son kiriting:")
#     if int(userNum) == int(num):
#         print("to'gri topdigiz")
#         break
#     else:
#         print("Xato topdingiz qaytdana urinib koring")


def sontop(x=10):
    tasodifiySon = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son oyladim. Topib koring")
    taxmainlar = 0
    while True:
        taxmainlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiySon:
            print("Xato, men oylagan son kattaroq")
        elif taxmin > tasodifiySon:
            print("Xato, men oylagan son kichikroq")
        else:
            break
        return taxmainlar
    print(f"Tabriklayman {taxmainlar} taxmin bilan topdingiz")


sontop()


def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(
            f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t) , men o'ylagan son bundan kattaroq(+), yoki kichikroq(-)".lower()
        )
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim")
    return taxminlar


sontop_pc()


def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user > taxminlar_pc:
            print("Men yutdim")

        elif taxminlar_user < taxminlar_pc:
            print("Siz yutdingiz")
        else:
            print("durrang")
        yana = int(input("Yana oynaysizmi? Ha(1)/Yo'q(0):"))


play()
