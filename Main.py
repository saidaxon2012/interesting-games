import random


def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o`yladim. Topa olasizmi?")

    while True:
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Xato. Men o`ylagan son bundan kattaroq. Yana harakat qiling:")
        elif taxmin > tasodifiy_son:
            print("Xato. Men o`ylagan son bundan kichikroq. Yana harakat qiling:")
        else:
            break
    print("Tabriklaymiz. Topdingiz!")


sontop(20)