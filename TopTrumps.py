import time
import random
import os
import urllib.request

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
        time.sleep(0.5)
        choice = input(menu)
    if choice == "1":
        return
    elif choice == "2":
        print("Game quitting...")
        time.sleep(1)
        quit()

def cardNum():
    #lot of error message
    inputQuestion = "Input a even number of cards between 4 - 30: "
    numberError = "Input must be a number."
    lowError = "Input should be greater or equal 4."
    highError = "Input should be less or equal 30."
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
    # 設定本地儲存的檔案名稱與 GitHub Raw 檔案網址
    LOCAL_FILE = "dogs.txt"
    GITHUB_RAW_URL = "https://raw.githubusercontent.com/Trevor-2/TopTrumps/refs/heads/main/dogs.txt"
    # 檢查檔案是否已存在
    if not os.path.exists(LOCAL_FILE):
        print(f"'{LOCAL_FILE}' is lost. Downloading from Github...")
        try:
            # 執行下載並儲存至本地
            urllib.request.urlretrieve(GITHUB_RAW_URL, LOCAL_FILE)
            print("Download Done!")
        except Exception as e:
            print(f"Download Failed. Reason: {e}")
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
    winnerCard = lessCard[:mid]
    notwinnerCard = lessCard[mid:]
    return winnerCard,notwinnerCard

def printCardCount(card_winner,card_notwinner):
    print(f"""
-----CARD COUNT-----
    You: {len(card_winner)}
    Bot: {len(card_notwinner)}""")
    time.sleep(0.5)

def printOneCard(input_dict,role): #now gonna use for show option
    count = 0
    if role == "human":
        print("\n-----YOUR CARD-----")
    else: #role = bot
        print("\n-----BOT CARD-----")
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
        category = input("Guess a category [1-4]: ")
        if category == "1" or category == "2" or category == "3" or category == "4":
            category = int(category)
            return category
        else:
            print("invaild input!")

def turn_numInput_to_text(categoryInput):
    if categoryInput == 1:
        categoryInput = "exercise"
    if categoryInput == 2:
        categoryInput = "intelligence"
    if categoryInput == 3:
        categoryInput = "friendliness"
    if categoryInput == 4:
        categoryInput = "drool"
    return categoryInput

def compare_result(categoryInput,cardComparing_winner,cardComparing_notwinner,winner,winner_this_round):
    if winner == "human":
        print (f"""    
-----YOUR CARD vs BOT CARD-----
    Your {categoryInput}: {cardComparing_winner[categoryInput]}
    Bot {categoryInput}: {cardComparing_notwinner[categoryInput]}""")
    else:
        print (f"""    
    Your {categoryInput}: {cardComparing_notwinner[categoryInput]}
    Bot {categoryInput}: {cardComparing_winner[categoryInput]}""")
    time.sleep(0.5)
    if winner_this_round == "human":
        print(f"\nYou Win!! You have more {categoryInput}:)")
    else:
        print(f"\nYou lost!! You have less {categoryInput}:(")
    time.sleep(2)

def calCategory(categoryInput,winner,card_winner,card_notwinner,cardComparing_winner,cardComparing_notwinner): #compare value between com and user
    if winner == "human":
        #if human win, and winner last rount is human
        if (cardComparing_winner[categoryInput] >= cardComparing_notwinner[categoryInput] and categoryInput != "drool" or
            cardComparing_winner[categoryInput] <= cardComparing_notwinner[categoryInput] and categoryInput == "drool"):
        #give give bot card to human
            card_winner += [cardComparing_winner,cardComparing_notwinner]
            winner_this_round = "human"
        #if human lost, and winner last rount is human
        else:
            card_notwinner += [cardComparing_winner,cardComparing_notwinner]
            winner_this_round = "bot" #give human card to bot
    else:
        #if not bot win, and winner last rount is bot (human win anyway)
        if not (cardComparing_winner[categoryInput] >= cardComparing_notwinner[categoryInput] and categoryInput != "drool" or
                cardComparing_winner[categoryInput] <= cardComparing_notwinner[categoryInput] and categoryInput == "drool"):
        #give bot card to human
            card_notwinner += [cardComparing_winner,cardComparing_notwinner]
            winner_this_round = "human"
        else:
            card_winner += [cardComparing_winner,cardComparing_notwinner]
            winner_this_round = "bot"
    time.sleep(0.5)
    return card_winner,card_notwinner,winner_this_round

winner = "human" #testing human
notWinner = "bot" #testing bot
while True:        
    menu() #some user can quit at this point
    card_Num = cardNum()
    while card_Num == "error": #return to menu if there are error input
        menu()
        card_Num = cardNum()
    savedList = createCards(nameList()) #list of all information of dogs (randomised)
    shuffledCard = cardShuffle(savedList)
    lessCard = pickFromList(shuffledCard,card_Num) #amount of card that user picked
    card_winner,card_notwinner = spiltCardInHalf(lessCard) #separate player card and bot card
    print("\nTIPS: PICK THE CATEGORY YOU THINK IS STRONGEST!!") #very nice tips message
    time.sleep(2)
    #loop game until someone have 0 card
    while len(card_winner) != 0 and len(card_notwinner) != 0:
        printCardCount(card_winner,card_notwinner)
        cardComparing_winner = card_winner.pop(0)
        cardComparing_notwinner = card_notwinner.pop(0)
        printOneCard(cardComparing_winner,winner) #show winner card
        categoryInput = inputCategory()
        categoryInput = turn_numInput_to_text(categoryInput)
        card_winner,card_notwinner,winner_this_round = calCategory(categoryInput,winner,card_winner,card_notwinner,cardComparing_winner,cardComparing_notwinner)
        printOneCard(cardComparing_notwinner,notWinner) #show winner card
        time.sleep(0.5)
        compare_result(categoryInput,cardComparing_winner,cardComparing_notwinner,winner,winner_this_round)

    time.sleep(0.5)
    print() #empty line
    if len(card_winner) != 0:

        print("You Win! You have all card in game now!! Well done;)")
        winner = "human"
        notWinner = "bot"
    else:
        print("You lost, You have lost all card in the game... ;(")
        winner = "bot"
        notWinner = "human"
    input("press enter to return to menu...")

'''
known bug:
    only show first card while looping, try move first card to buttom 
    a pile: [1,2,3,4] --> [1,2,3,4,a]
    b pile: [a,b,c,d] --> [b,c,d]

    what i want:
    a pile: [1,2,3,4] ↘     [2,3,4]  [2,3,4,1,a] 
    comparing:              [1,a] 
    b pile: [a,b,c,d] ↗     [b,c,d]  [b,c,d]
'''