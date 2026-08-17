import time
import random

def menu():
    menu = """
MENU:

1. Play Game
2. Quit

Enter Your Option [1/2]: """
    error = "Input must be either 1 or 2\n"
    choice = input(menu)
    while choice != "1" and choice != "2":
        print(error)
        time.sleep(0.3)
        choice = input(menu)
    if choice == "1":
        return
    elif choice == "2":
        print("Game quitting...")
        time.sleep(1)
        quit()
    else:
        print(f"congratulations!! You just find a bug in my code, pls report the input ({choice}) that you entered to the developer of this program.")
        input()
        quit()

def cardNum():
    #lot of error message
    inputQuestion = "Input a even number of cards between 4 - 30: "
    numberError = "Input must be a number."
    lowError = "Input should be greater than 4."
    highError = "Input should be less than 30."
    oddError = "Input can't be odd number."

    #check if there are error
    try:
        numInput = int(input(inputQuestion))
    except:
        print(numberError)
        time.sleep(1)
        return "error"
    
    if numInput < 4:
        print(lowError)
        time.sleep(1)
        return "error"
    if numInput > 30:
        print(highError)
        time.sleep(1)
        return "error"
    if numInput % 2 != 0:
        print(oddError)
        time.sleep(1)
        return "error"
    
    #if no error there
    return numInput

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

def spiltCardInHalf():

menu() #some user can quit at this point
card_Num = cardNum()
while card_Num == "error": #return to menu if there are error input
    menu()
    card_Num = cardNum()

savedList = createCards(nameList()) #list of all information of dogs (randomised)
shuffledCard = cardShuffle(savedList)
lessCard = pickFromList(shuffledCard,card_Num) #amount of card that user picked
spiltedCard = spiltCardInHalf(less)
