# This Software is licensed under Mozilla Public License 2.0 ( https://spdx.org/licenses/MPL-2.0.html )
from colorama import Back
import colorama
import random
colorama.init(autoreset=True)

# ***************************************************************SETTINGS*********************************************************************
# IF YOU DOESN'T WANT COLORS, CHANGE THIS TO False ! (default: True)
COLORS = True

# If you lose, do you want to still play the game? (default & recommended: False) (Still Play The Game After Lose)
SPTGAL = False
# ********************************************************************************************************************************************


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
    elif p1card["level"] == p2card["level"]:
        return "DRAW"
    else:
        print("\n[ERROR]")
        print("[!!!] The p1card[\"level\"] ( " + str(p1card["level"]) +
              " ) is not relative to the p2card[\"level\"] ( " + str(p2card["level"]) + " )!")
        input("To continue, press [ENTER]. . .")


def isWin(cards):
    """Checks if the user wins or not

    Args:
        cards (dict): The cards

    Returns:
        bool: True: The player won  False: The player doesn't won (BUT the players DOES NOT lose!)
    """
    try:
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
    except:
        notImportant = random.random()


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
        print("[ERROR]")
        print(
            "[!!!] var: card[\"type\"] not W; F; S | card[\"type\"] = " + str(card["type"]))
    if type(card["level"]) is int:
        if card["color"] == "R":
            if COLORS:
                return f"{Back.RED}" + cType + " " + str(card["level"])
            else:
                return "RED " + cType + " " + str(card["level"])
        elif card["color"] == "G":
            if COLORS:
                return f"{Back.GREEN}" + cType + " " + str(card["level"])
            else:
                return "GREEN " + cType + " " + str(card["level"])
        elif card["color"] == "B":
            if COLORS:
                return f"{Back.BLUE}" + cType + " " + str(card["level"])
            else:
                return "BLUE " + cType + " " + str(card["level"])
        else:
            print("[ERROR]")
            print(
                "[!!!] var: card[\"color\"] is not R; G; B | card[\"color\"] = " + card["color"])
    else:
        print("[ERROR]")
        print("[!!!] Type of card[\"level\"] is not int | Type = " +
              str(type(card["level"])) + " | card[\"level\"] = " + str(card["level"]))


def lose():
    inGame = False
    p1cards = []
    p1score = []
    p2cards = []
    p2score = []
    notImportant = 0
    num = 0
    print("\n\nYou losed the game.\n\n")
    if SPTGAL:
        while len(p1cards) != 0:
            for i in range(10):
                p1cards.append({
                    "type": random.choice(["W", "F", "S"]),
                    "level": random.randrange(1, 11),
                    "color": random.choice(["R", "G", "B"])
                })
        for i in range(10):
            p1cards.append({
                "type": random.choice(["W", "F", "S"]),
                "level": random.randrange(1, 11),
                "color": random.choice(["R", "G", "B"])
            })
        for i in range(10):
            p2cards.append({
                "type": random.choice(["W", "F", "S"]),
                "level": random.randrange(1, 11),
                "color": random.choice(["R", "G", "B"])
            })
        notImportant = random.random() ** random.random() ** random.random()
    else:
        for notImportant in range(80):
            print("LOSE")
        raise RuntimeError(
            "Sorry, but you can't play anymore! Please, close, and reopen this game!")


if __name__ == '__main__':
    print("\nCovered Software is provided under this License on an \"as is\" basis, without warranty of any kind, either expressed, implied, or statutory, including, without limitation, warranties that the Covered Software is free of defects, merchantable, fit for a particular purpose or non-infringing. The entire risk as to the quality and performance of the Covered Software is with You. Should any Covered Software prove defective in any respect, You(not any Contributor) assume the cost of any necessary servicing, repair, or correction. This disclaimer of warranty constitutes an essential part of this License. No use of any Covered Software is authorized under this License except under this disclaimer.\n")
    inGame = False
    while True:
        p1cards = []
        p1score = [[], [], []]

        p2cards = []
        p2score = [[], [], []]

        if inGame == False:
            for i in range(10):
                p1cards.append({
                    "type": random.choice(["W", "F", "S"]),
                    "level": random.randrange(1, 11),
                    "color": random.choice(["R", "G", "B"])
                })
            for i in range(10):
                p2cards.append({
                    "type": random.choice(["W", "F", "S"]),
                    "level": random.randrange(1, 11),
                    "color": random.choice(["R", "G", "B"])
                })

        inGame = True
        while inGame == True:
            print("\n")

            if len(p1score) > 3:
                lose()
                break
            if len(p2score) > 3:
                print("\n\n\nYOU WON THE GAME!!!\n\n\n")
                inGame = False
                break

            if len(p1cards) <= 0:
                for i in range(10):
                    p1cards.append({
                        "type": random.choice(["W", "F", "S"]),
                        "level": random.randrange(1, 11),
                        "color": random.choice(["R", "G", "B"])
                    })

            if len(p2cards) <= 0:
                for i in range(10):
                    p2cards.append({
                        "type": random.choice(["W", "F", "S"]),
                        "level": random.randrange(1, 11),
                        "color": random.choice(["R", "G", "B"])
                    })

            for i in range(0, 3):
                if i == 0:
                    word = "Water"
                elif i == 1:
                    word = "Fire"
                elif i == 2:
                    word = "Snow"
                else:
                    print("[ERROR]")
                    print("[!!!] var: i not 0; 1; 2 | i = " + str(i))

                if len(p1score[i]) != 0:
                    if len(p1score[i]) == 1:
                        print(word + " card: " + frth(p1score[i][0]))
                    elif len(p1score[i]) == 2:
                        print(word + " cards: " +
                              frth(p1score[i][0]) + "; " + frth(p1score[i][1]))
                    elif len(p1score[i]) == 3:
                        print(word + " cards: " + frth(p1score[i][0]) + "; " + frth(
                            p1score[i][1]) + "; " + frth(p1score[i][2]))
                    else:
                        lose()
                        break
            print("Your cards:")
            num = 0
            for card in p1cards:
                print(str(num) + ": " + frth(card))
                num += 1

            user = int(input("Write the number of your choiced card>"))
            if user < 11 and user > -1:
                notImportant = random.random()
            else:
                print("[ERROR]")
                print(
                    "[!!!] var: user not 0; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10 | user = " + str(user))
                userTMP = input(
                    "Write NC for normal continue (NOT recommended), write CC for command continue (recommended), or write B for break (can break something! NOT recommended)>")
                if userTMP == "CC":
                    continue
                elif userTMP == "B":
                    print("[WARNING]")
                    print("[!] This can break something!")
                    break
                else:
                    notImportant = random.random()
            try:
                userChoice = {
                    "type": p1cards[user]["type"], "level": p1cards[user]["level"], "color": p1cards[user]["color"]}
            except:
                lose()
                break
            if userChoice in p1cards:
                print("\n")
                p1cards.remove(userChoice)
                p2random = random.randrange(0, 9)
                if whoWins(userChoice, p2cards[p2random]) == True:
                    print("WIN!")
                    if userChoice["type"] == "W":
                        p1score[0].append(userChoice)
                    elif userChoice["type"] == "F":
                        p1score[1].append(userChoice)
                    elif userChoice["type"] == "S":
                        p1score[2].append(userChoice)
                    else:
                        print("[ERROR]")
                        print(
                            "var: userChoice[\"type\"] not W; F; S | userChoice[\"type\"] = " + str(userChoice["type"]))
                elif whoWins(userChoice, p2cards[p2random]) == False:
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
                    print("func: whoWins RETURN not True; False; DRAW | RETURN = " +
                          str(whoWins(userChoice, p2cards[p2random])))
            else:
                print("var: userChoice not in p1cards | userChoice = " +
                      str(userChoice) + " | p1cards = " + str(p1cards))

            if isWin(p1score) == True:
                print("\n\n\nYOU WON THE GAME!!!\n\n\n")
                inGame = False
                break
            elif isWin(p2score) == True:
                lose()
                break

        inGame = False
        continue
