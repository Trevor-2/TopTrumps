import time
import random

def nameList(): #easily read name from file
    nameList = []
    f = open("dogs.txt")
    rawList = f.readlines()
    f.close()
    for name in rawList:
        nameList.append(name.strip())
    return nameList

def createCards(nameList):
    deck = [] # 用嚟裝所有狗仔卡嘅 List
    
    for name in nameList:
        # 幫每隻狗仔建立一張獨立嘅卡片 (Dictionary)
        card = {
            "name": name,
            "exercise": random.randrange(1, 6),      # 1 to 5
            "intelligence": random.randrange(1, 101),  # 1 to 100
            "friendliness": random.randrange(1, 11),   # 1 to 10
            "drool": random.randrange(1, 11)           # 1 to 10
        }
        deck.append(card)
        
    return deck

def cardShuffle(shuffledList): #shuffle the card
    random.shuffle(shuffledList)
    return shuffledList

def pickFromList(shuffledCard,card_Num):
    return shuffledCard[:card_Num]

def spiltCardInHalf(lessCard):
    mid = len(lessCard) // 2
    playerCard = lessCard[:mid]
    botCard = lessCard[mid:]
    return playerCard,botCard

def printOneCard(input_dict):
    print("\n-----CARD-----")
    # printing using For Loop
    for key, value in input_dict.items():
        print(f"{key}: {value}")

def inputCategory():
    while True: #keep repeating until user enter correct input
        category = input("""
-----CATEGORY-----
    1. Exercise
    2. Intelligence
    3. Friendliness
    4. Drool
Input a category [1-4]:
""")
        if category == "1" or category == "2" or category == "3" or category == "4":
            category = int(category)
            return category
        else:
            print("invaild input!")

"""
-->
def calCategory(categoryInput,playerCard,botCard): #compare value between com and user
    if categoryInput == 1: #compare exercise, higher win
"""

card_Num = random.randrange(4, 32, 2)

savedList = createCards(nameList()) #list of all information of dogs (randomised)
shuffledCard = cardShuffle(savedList)
lessCard = pickFromList(shuffledCard,card_Num) #amount of card that user picked
playerCard,botCard = spiltCardInHalf(lessCard) #separate player card and bot card
#loop game until someone have 0 card
for i in range (card_Num//2):
    printOneCard(playerCard[i]) #show one of the player's card
    categoryInput = random.randint(1, 5)
    printOneCard(botCard[i])
    #-->calCategory(categoryInput,playerCard[i],botCard[i])

    print(lessCard)
    print("code runned successfully!")

    """
    work to do:
    make code loop until someone have 0 card (someone lost) (IMPORTANT)
    complete def calCategory
    """