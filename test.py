import random
def nameList(): #easily read name from file
    nameList = []
    f = open("dogs.txt")
    rawList = f.readlines()
    f.close()
    for name in rawList:
        nameList.append(name.strip())
    return nameList

deck = [] # 用嚟裝所有狗仔卡嘅 List

for name in nameList():
    # 幫每隻狗仔建立一張獨立嘅卡片 (Dictionary)
    card = {
        "name": name,
        "exercise": random.randrange(1, 6),      # 1 to 5
        "intelligence": random.randrange(1, 101),  # 1 to 100
        "friendliness": random.randrange(1, 11),   # 1 to 10
        "drool": random.randrange(1, 11)           # 1 to 10
    }
    deck.append(card)

print(deck)