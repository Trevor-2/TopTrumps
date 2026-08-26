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
    with open("dogs.txt") as f:
        rawList = f.readlines()
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

def printCardCount(playerCardList,botCardList):
        print(f"""
-----CARD COUNT-----
    You: {len(playerCardList)}
    Bot: {len(botCardList)}""")

def printOneCard(input_dict,role): #now gonna use for show option
    count = 0
    time.sleep(0.3)
    if role == "human":
        print("\n-----YOUR CARD-----")
    elif role == "bot":
        print("\n-----BOT CARD-----")
    else:
        print("\n-----CARD-----")
    # printing using For Loop
    for key, value in input_dict.items():
        if count < 1:
            print(f"    {key}: {value}")
        else:
            print(f"    {count}. {key}: {value}")
        count += 1


def inputCategory():
    while True: #keep repeating until user enter correct input
        time.sleep(0.5)
        category = input("Guess a category that is larger than bot's [1-4]: ")
        if category == "1" or category == "2" or category == "3" or category == "4":
            category = int(category)
            return category
        else:
            print("invaild input!")


def calCategory(categoryInput,playerCardComparing,botCardComparing,
                playerCardList,botCardList): #compare value between com and user
    #if player win
    if (categoryInput == 1 and playerCardComparing['exercise'] >= botCardComparing['exercise'] or
        categoryInput == 2 and playerCardComparing['intelligence'] >= botCardComparing['intelligence'] or
        categoryInput == 3 and playerCardComparing['friendliness'] >= botCardComparing['friendliness'] or
        categoryInput == 4 and playerCardComparing['drool'] <= botCardComparing['drool']):
    #give bot card to player
        playerCardList.append(botCardComparing)
        botCardList.remove(botCardComparing)
        time.sleep(0.3)
        print("\nYou win!! One card moved to your pile.")
    #if bot win, player card will give to bot
    else:
        botCardList.append(playerCardComparing)
        playerCardList.remove(playerCardComparing)
        time.sleep(0.3)
        print("\nYou lost... One card moved to bot pile.")
    time.sleep(1)
    return playerCardList,botCardList

winner = "human"
notWinner = "bot"
while True:        
    menu() #some user can quit at this point
    card_Num = cardNum()
    while card_Num == "error": #return to menu if there are error input
        menu()
        card_Num = cardNum()
    savedList = createCards(nameList()) #list of all information of dogs (randomised)
    shuffledCard = cardShuffle(savedList)
    lessCard = pickFromList(shuffledCard,card_Num) #amount of card that user picked
    playerCard,botCard = spiltCardInHalf(lessCard) #separate player card and bot card
    print("\nTIPS: PICK THE LARGEST CATEGORY!!") #very nice tips message
    time.sleep(2)
    #loop game until someone have 0 card
    while len(playerCard) != 0 and len(botCard) != 0:
        printCardCount(playerCard,botCard)
        printOneCard(playerCard[0],winner) #show one of the player's card
        categoryInput = inputCategory()
        printOneCard(botCard[0],notWinner)
        playerCard,botCard = calCategory(categoryInput,playerCard[0],botCard[0],playerCard,botCard)
    time.sleep(1)
    print() #empty line
    if len(playerCard) != 0:

        print("You Win! You have all card in game now!! Well done;)")
        winner = "human"
        notWinner = "bot"
    else:
        print("You lost, You have lost all card in the game... ;(")
        winner = "bot"
        notWinner = "human"
    input("press enter to return to menu...")