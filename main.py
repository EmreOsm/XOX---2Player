datas = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
round = 1
game = ""
playerScore1 = 0
playerScore2 = 0
startNewGame = 0


def printXOX():
    print("\n")
    print(f"| {datas[0]} | {datas[1]} | {datas[2]} |")
    print( "|---|---|---|")
    print(f"| {datas[3]} | {datas[4]} | {datas[5]} |")
    print( "|---|---|---|")
    print(f"| {datas[6]} | {datas[7]} | {datas[8]} |")
    print("\n")

def callNumber1():
    a = True
    while a:
        number1 = str(input("input row 1,2,3: "))
        if number1 == "1" or number1 == "2" or number1 == "3":
            a = False
            return number1

def callNumber2():
    a = True
    while a:
        number2 = str(input("input column 1,2,3: "))
        if number2 == "1" or number2 == "2" or number2 == "3":
            a = False
            return number2

def theNumber(callNumber1, callNumber2):

    theNumber = str(callNumber1) + "," + str(callNumber2)
    return theNumber

def theNumberCheck(_theNumber):
    if _theNumber == "1,1":
        if datas[0] == " ":
            return True
    elif _theNumber == "1,2":
        if datas[1] == " ":
            return True
    elif _theNumber == "1,3":
        if datas[2] == " ":
            return True
    elif _theNumber == "2,1":
        if datas[3] == " ":
            return True
    elif _theNumber == "2,2":
        if datas[4] == " ":
            return True
    elif _theNumber == "2,3":
        if datas[5] == " ":
            return True
    elif _theNumber == "3,1":
        if datas[6] == " ":
            return True
    elif _theNumber == "3,2":
        if datas[7] == " ":
            return True
    elif _theNumber == "3,3":
        if datas[8] == " ":
            return True
    else:
        return False

def calculateX(_theNumber):
    if _theNumber == "1,1":
        datas[0] = "X"
    elif _theNumber == "1,2":
        datas[1] = "X"
    elif _theNumber == "1,3":
        datas[2] = "X"
    elif _theNumber == "2,1":
        datas[3] = "X"
    elif _theNumber == "2,2":
        datas[4] = "X"
    elif _theNumber == "2,3":
        datas[5] = "X"
    elif _theNumber == "3,1":
        datas[6] = "X"
    elif _theNumber == "3,2":
        datas[7] = "X"
    elif _theNumber == "3,3":
        datas[8] = "X"

def calculateO(_theNumber):
    if _theNumber == "1,1":
        datas[0] = "O"
    elif _theNumber == "1,2":
        datas[1] = "O"
    elif _theNumber == "1,3":
        datas[2] = "O"
    elif _theNumber == "2,1":
        datas[3] = "O"
    elif _theNumber == "2,2":
        datas[4] = "O"
    elif _theNumber == "2,3":
        datas[5] = "O"
    elif _theNumber == "3,1":
        datas[6] = "O"
    elif _theNumber == "3,2":
        datas[7] = "O"
    elif _theNumber == "3,3":
        datas[8] = "O"

def whouseTurn():

    if round % 2 == 0:
        return True
    else:
        return False

def winer():
    if datas[0] == "X" and datas[1] == "X" and datas[2] == "X":
        return 0
    elif datas[3] == "X" and datas[4] == "X" and datas[5] == "X":
        return 0
    elif datas[6] == "X" and datas[7] == "X" and datas[8] == "X":
        return 0
    elif datas[0] == "X" and datas[3] == "X" and datas[6] == "X":
        return 0
    elif datas[1] == "X" and datas[4] == "X" and datas[7] == "X":
        return 0
    elif datas[2] == "X" and datas[5] == "X" and datas[8] == "X":
        return 0
    elif datas[0] == "X" and datas[4] == "X" and datas[8] == "X":
        return 0
    elif datas[2] == "X" and datas[4] == "X" and datas[6] == "X":
        return 0
    elif datas[0] == "O" and datas[1] == "O" and datas[2] == "O":
        return 1
    elif datas[3] == "O" and datas[4] == "O" and datas[5] == "O":
        return 1
    elif datas[6] == "O" and datas[7] == "O" and datas[8] == "O":
        return 1
    elif datas[0] == "O" and datas[3] == "O" and datas[6] == "O":
        return 1
    elif datas[1] == "O" and datas[4] == "O" and datas[7] == "O":
        return 1
    elif datas[2] == "O" and datas[5] == "O" and datas[8] == "O":
        return 1
    elif datas[0] == "O" and datas[4] == "O" and datas[8] == "O":
        return 1
    elif datas[2] == "O" and datas[4] == "O" and datas[6] == "O":
        return 1

def chouseGameStyle():
    a = True
    while a:
        gameSytle = str(input("1Player or 2Player: "))
        if gameSytle.lower() == "2player":
            return False
            a = False
        elif gameSytle.lower() == "1player":
            return True
            a = False



print("XOX Game")
c = chouseGameStyle()
player1 = str(input("Player1: "))
player2 = str(input("Player2: "))

if c:
    print("1player")
    pass
else:
    try:
        while True:

            if startNewGame == 1 or round == 10:
                a = input("Do you want more round? ")
                if round == 10:
                    print("draw")
                if a.lower() == "yes":
                    datas = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                    round = 1
                    startNewGame = 0
                    playerScore2 = playerScore2 + 1
                    print(f"{player1} | {player2} \n{playerScore1} \t{playerScore2}")
                else:
                    quit()

            if whouseTurn():
                print(f"{player2}'s turn")
            else:
                print(f"{player1}'s turn")

            number = theNumber(callNumber1(), callNumber2())

            if whouseTurn():
                if theNumberCheck(number):
                    calculateO(number)
                    round = round + 1
            else:
                if theNumberCheck(number):
                    calculateX(number)
                    round = round + 1

            if winer() == 0:
                print(f"{player1}'s win")

                startNewGame = 1

            elif winer() == 1:
                print(f"{player2}'s turn")

                startNewGame = 1

            printXOX()


    except:
        pass