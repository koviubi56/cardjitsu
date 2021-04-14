"""
⚠️ WARNING ⚠️ This project is using the global keyword! Please, don't use these variables!
List of variables:
inGame
p1cards
p1score
p2cards
p2score
losed
"""
# This Software is licensed under Mozilla Public License 2.0 ( https://spdx.org/licenses/MPL-2.0.html )
from colorama import Back
import colorama
import random
colorama.init(autoreset=True)
notImportant = 1
# ***************************************************************SETTINGS**************************************************************************************
# IF YOU DOESN'T WANT COLORS, CHANGE THIS TO False ! (default: True)
COLORS = True

# (This is for me) Debug mode [WARNING] This will NOT say anything more! This checks if there any issues.
DEBUG = {
    # If True: the program is automaticly selecting the 0 card  False: you can select a card
    "auto": False,
    # If True: when you are at a new game (after losing, winning and before the first game) you need to press enter to continue  If "when100": every 100th time
    "pause": False
}

# If there are less than 10 cards, you get one (or more). (If There Are Less Than 10 Cards, Give A Card) (default: True)
ITALT10CGAC = True
# *************************************************************************************************************************************************************


def giveNewCards(isPlayer2=True, isPlayer1=True, howMany=10):
    """Gives new cards.

    Args:
        isPlayer2 (bool, optional): Player2 needs new cards? Defaults to True.
        isPlayer1 (bool, optional): Player1 needs new cards? Defaults to True.
    """
    if isPlayer1:
        for notImportant in range(howMany):
            p1cards.append({
                "type": random.choice(["W", "F", "S"]),
                "level": random.randrange(1, 11),
                "color": random.choice(["R", "G", "B"])
            })
    if isPlayer2:
        for notImportant in range(howMany):
            p2cards.append({
                "type": random.choice(["W", "F", "S"]),
                "level": random.randrange(1, 11),
                "color": random.choice(["R", "G", "B"])
            })


def error(errcode, varToShow=None, nameOfVar=None):
    """Just an error function.

    Args:
        errcode (str): The error code.
        varToShow (var, optional): The variable to show. Defaults to None.
        nameOfVar (str, optional): The name of var. Defaults to None.

    Example:
        [ERROR]
        {errcode} | {nameOfVar} = {varToShow}

        [ERROR]
        {errcode}

        [ERROR]
        It's Friday | day = Friday

        [ERROR]
        You can't do that here and now!
    """
    print("[ERROR]")
    if varToShow is None:
        print(errcode)
    else:
        print(errcode + " | " + nameOfVar + " = " + str(varToShow))


def whoWins(p1card, p2card):
    """Returns if the player1 wins or not

    Args:
        p1card (dict): Cards of player1
        p2card (dict): Cards of player2

    Returns:
        bool: True: If player1 won  False: If player2 won  "DRAW": If it's a draw.
    """
    if p1card["type"] == p2card["type"]:
        return "DRAW"

    if p1card["level"] > p2card["level"]:
        return True
    elif p1card["level"] < p2card["level"]:
        return False

    return "DRAW"


def isWin(cards):
    """Checks if the user wins or not

    Args:
        cards (dict): The cards

    Returns:
        bool: True: The player won  False: The player doesn't won (BUT the players DOES NOT lose!)
    """
    try:  # * This try-except is IMPORTANT!
        for i in range(0, 3):
            idkvar = cards[i][0]["color"]
            if idkvar != cards[i][1]["color"] and idkvar != cards[i][2]["color"] and cards[i][1]["color"] != cards[i][2]["color"]:
                return True
        idkvar = cards[0][0]["color"]
        if idkvar != cards[1][0]["color"] and idkvar != cards[2][0]["color"] and cards[1][0]["color"] != cards[2][0]["color"]:
            return True
        if idkvar != cards[1][1]["color"] and idkvar != cards[2][1]["color"] and cards[1][1]["color"] != cards[2][1]["color"]:
            return True
        if idkvar != cards[1][2]["color"] and idkvar != cards[2][2]["color"] and cards[1][2]["color"] != cards[2][2]["color"]:
            return True

        return False
    except IndexError:
        pass


def frth(card):
    """From Robot To Human. Colorizes the card

    Args:
        card (dict): One card

    Returns:
        str: The colorized card
    """
    if card["type"] == "W":
        cType = "Water"
    elif card["type"] == "F":
        cType = "Fire"
    elif card["type"] == "S":
        cType = "Snow"
    else:
        error("var: card[\"type\"] not W; F; S",
              card["type"], "card[\"type\"]")
    if isinstance(card["level"], int):  # isinstance(X, Y) = if type of X is Y, then :)
        if card["color"] == "R":
            if COLORS:
                return f"{Back.RED}" + cType + " " + str(card["level"])

            return "RED " + cType + " " + str(card["level"])
        elif card["color"] == "G":
            if COLORS:
                return f"{Back.GREEN}" + cType + " " + str(card["level"])

            return "GREEN " + cType + " " + str(card["level"])
        elif card["color"] == "B":
            if COLORS:
                return f"{Back.BLUE}" + cType + " " + str(card["level"])

            return "BLUE " + cType + " " + str(card["level"])

        error("var: card[\"color\"] is not R; G; B",
              card["color"], "card[\"color\"]")
    else:
        error("Type of card[\"level\"] is not int",
              card["level"], "card[\"level\"]")


def lose(reason="ERROR! NO REASON PROVIDED!"):
    """Lose the game.
    """
    global inGame
    global p1cards
    global p1score
    global p2cards
    global p2score
    global losed
    inGame = False
    p1cards = []
    p1score = [[], [], []]
    p2cards = []
    p2score = [[], [], []]
    if losed is False:
        print("\n\nYou losed the game.\n\n")
        losed = True
    giveNewCards()


def win():
    """Win the game
    """
    print("\n\n\nYOU WON THE GAME!!!\n\n\n")
    inGame = False


def testLose():
    for j in range(3):  # j has no meanings. it's just j. why not?
        if len(p1score[j]) > 3:
            lose("tooManyCards")


if __name__ == '__main__':
    print("\nCovered Software is provided under this License on an \"as is\" basis, without warranty of any kind, either expressed, implied, or statutory, including, without limitation, warranties that the Covered Software is free of defects, merchantable, fit for a particular purpose or non-infringing. The entire risk as to the quality and performance of the Covered Software is with You. Should any Covered Software prove defective in any respect, You(not any Contributor) assume the cost of any necessary servicing, repair, or correction. This disclaimer of warranty constitutes an essential part of this License. No use of any Covered Software is authorized under this License except under this disclaimer.\n")
    inGame = False
    while True:
        # Reseting (or creating the variables for) cards
        p1cards = []
        p1score = [[], [], []]

        p2cards = []
        p2score = [[], [], []]

        losed = False

        # Giving new cards
        giveNewCards()

        # Debug mode pause
        if DEBUG["pause"] is True:
            input("debug: press [ENTER]. . .")
        elif DEBUG["pause"] == "when100":
            try:
                debugNum += 1
            except NameError:
                debugNum = 1
            if debugNum >= 100:
                debugNum = 0
                input("debug100: press [ENTER]. . .")

        inGame = True
        while inGame:
            print("\n")

            # If the user (or the bot) has no cards, give them
            if ITALT10CGAC is not True:
                if len(p1cards) <= 0:
                    giveNewCards(False)

                if len(p2cards) <= 0:
                    giveNewCards(True, False)
            else:
                while len(p1cards) < 10:
                    giveNewCards(False, True, 1)

                while len(p2cards) < 10:
                    giveNewCards(True, False, 1)

            losed = False
            # Showing score (winned cards)
            for i in range(0, 3):
                if i == 0:
                    word = "Water"
                elif i == 1:
                    word = "Fire"
                elif i == 2:
                    word = "Snow"
                else:
                    error("var: i not 0; 1; 2", i, "i")

                try:  # * This try-except is IMPORTANT!
                    for k in range(0, 3):
                        if len(p1score[k]) > 3:
                            lose("tooManyCards")

                    if len(p1score[i]) != 0:
                        if len(p1score[i]) == 1:
                            print(word + " card: " + frth(p1score[i][0]))
                        elif len(p1score[i]) == 2:
                            print(word + " cards: " +
                                  frth(p1score[i][0]) + "; " + frth(p1score[i][1]))
                        elif len(p1score[i]) == 3:
                            print(word + " cards: " + frth(p1score[i][0]) + "; " + frth(
                                p1score[i][1]) + "; " + frth(p1score[i][2]))
                        elif len(p1score[i]) > 3:
                            lose("tooManyCards")
                except IndexError:
                    lose("tooManyCards")

            # Showing the cards (p1cards)
            print("Your cards:")
            num = 0
            for card in p1cards:
                print(str(num) + ": " + frth(card))
                num += 1
            num = None

            # Write the number of your choiced card
            if DEBUG["auto"] is not True:
                try:
                    user = int(input("Write the number of your choiced card>"))
                except ValueError:
                    continue
            elif DEBUG["auto"]:
                user = 0
            # Tests the number is good (0-9)
            if user < 10 and user > -1:
                pass
            else:
                error("var: user not 0; 1; 2; 3; 4; 5; 6; 7; 8; 9", user, "user")
            userChoice = {
                "type": p1cards[user]["type"], "level": p1cards[user]["level"], "color": p1cards[user]["color"]}
            # Checks the userChoice is in p1cards (the user have that card?)
            if userChoice in p1cards:
                print("\n")
                p1cards.remove(userChoice)
                if ITALT10CGAC:
                    while len(p1cards) < 10:
                        giveNewCards(False, True, 1)
                # F i g h t
                p2random = random.randrange(0, len(p2cards))
                if whoWins(userChoice, p2cards[p2random]):
                    print("WIN!")
                    if userChoice["type"] == "W":
                        p1score[0].append(userChoice)
                    elif userChoice["type"] == "F":
                        p1score[1].append(userChoice)
                    elif userChoice["type"] == "S":
                        p1score[2].append(userChoice)
                    else:
                        error("var: userChoice[\"type\"] not W; F; S",
                              userChoice["type"], "userChoice[\"type\"]")
                elif whoWins(userChoice, p2cards[p2random]) is False:
                    print("Lose")
                    if p2cards[p2random]["type"] == "W":
                        p2score[0].append(p2cards[p2random])
                    elif p2cards[p2random]["type"] == "F":
                        p2score[1].append(p2cards[p2random])
                    elif p2cards[p2random]["type"] == "S":
                        p1score[2].append(p2cards[p2random])
                    else:
                        print("var: p2cards[" + str(p2random) + "] not W; F; S | p2cards[" + str(
                            p2random) + "] = " + str(p2cards[p2random]))
                elif whoWins(userChoice, p2cards[p2random]) == "DRAW":
                    print("Draw")
                else:
                    error("func: whoWins RETURN not True; False; DRAW", str(
                        whoWins(userChoice, p2cards[p2random])), "RETURN")
                p2cards.remove(p2cards[p2random])
            else:
                error("var: userChoice not in p1cards", [
                      userChoice, p1cards], "userChoice AND p1cards")

            testLose()

            # Checks if the user is won the game
            if isWin(p1score):
                win()
                break
            elif isWin(p2score):
                lose("player2")
                break

            # Continue
            continue
        inGame = False
