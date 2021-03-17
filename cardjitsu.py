# This Software is licensed under Mozilla Public License 2.0 ( https://spdx.org/licenses/MPL-2.0.html )

"""
************************************************************************
*                                                                      *
*  6. Disclaimer of Warranty                                           *
*  -------------------------                                           *
*                                                                      *
*  Covered Software is provided under this License on an "as is"       *
*  basis, without warranty of any kind, either expressed, implied, or  *
*  statutory, including, without limitation, warranties that the       *
*  Covered Software is free of defects, merchantable, fit for a        *
*  particular purpose or non-infringing. The entire risk as to the     *
*  quality and performance of the Covered Software is with You.        *
*  Should any Covered Software prove defective in any respect, You     *
*  (not any Contributor) assume the cost of any necessary servicing,   *
*  repair, or correction. This disclaimer of warranty constitutes an   *
*  essential part of this License. No use of any Covered Software is   *
*  authorized under this License except under this disclaimer.         *
*                                                                      *
************************************************************************
"""

# * The basic idea is from Club Penguin!

# ! .:FOR ME!:. DO NOT FORGET TO CREATE CHANGELOG!

# TODO: NO: raise YES: handle
# TODO: p1visual (rendesen jelenjenek meg a kártyák)

import random
import time

"""
===HOW TO WIN===
1. You have the same card type (water, fire, snow), but three in different colors (Red, Green, Blue).
2. You have NOT the same card type, but three in different colors, and types.
3. If the 2nd player (in this case the robot) have more than 3 cards in the water, fire, or snow type.
"""


def whoWins(p1card, p2card):
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


if __name__ == '__main__':
    print("\nCovered Software is provided under this License on an \"as is\" basis, without warranty of any kind, either expressed, implied, or statutory, including, without limitation, warranties that the Covered Software is free of defects, merchantable, fit for a particular purpose or non-infringing. The entire risk as to the quality and performance of the Covered Software is with You. Should any Covered Software prove defective in any respect, You(not any Contributor) assume the cost of any necessary servicing, repair, or correction. This disclaimer of warranty constitutes an essential part of this License. No use of any Covered Software is authorized under this License except under this disclaimer.\n")
    while True:
        inGame = True
        p1cards = []
        p1score = [[], [], []]

        p2cards = []
        p2score = [[], [], []]

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

        while inGame == True:
            print("\n")

            if len(p1score) > 3:
                print("\n\n\nYou losed the game.\n\n\n")
                inGame = False
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
                    print("[!!!] var: i: not 0; 1; 2 | i = " + str(i))
                    userTMP = input(
                        "Write NC for normal continue (recommended), write CC for command continue, or write B for break (can break something!)>")
                    if userTMP == "CC":
                        continue
                    elif userTMP == "B":
                        print("[WARNING]")
                        print("[!] This can break something!")
                        break
                    else:
                        notImportant = random.random()
                if len(p1score[i]) != 0:
                    if len(p1score[i]) == 1:
                        print(word + " cards: " + str(p1score[i][0]))
                    elif len(p1score[i]) == 2:
                        print(word + " cards: " +
                              str(p1score[i][0]) + "; " + str(p1score[i][1]))
                    elif len(p1score[i]) == 3:
                        print(word + " cards: " + str(p1score[i][0]) + "; " + str(
                            p1score[i][1]) + "; " + str(p1score[i][2]))
                    else:
                        print("[ERROR]")
                        print("[!!!] var: let(p1score[" + str(
                            i) + "]) not 0; 1; 2; 3 | len(p1score[" + str(i) + "]) = " + str(len(p1score[i])))
                        userTMP = input(
                            "Write NC for normal continue (recommended), write CC for command continue, or write B for break (can break something!)>")
                        if userTMP == "CC":
                            continue
                        elif userTMP == "B":
                            print("[WARNING]")
                            print("[!] This can break something!")
                            break
                        else:
                            notImportant = random.random()

            print("Your cards: " + str(p1cards))
            userT = input("Write the type of your choiced card>").upper()
            userL = int(input("Write the level of your choiced card>"))
            userC = input("Write the color of your choiced card>").upper()
            userChoice = {"type": userT, "level": userL, "color": userC}
            if userChoice in p1cards:
                print("\n")
                p1cards.remove(userChoice)
                p2random = random.randrange(0, 9)
                if whoWins(userChoice, p2cards[p2random]) == True:
                    print("WIN!")
                    if userT == "W":
                        p1score[0].append(userChoice)
                    elif userT == "F":
                        p1score[1].append(userChoice)
                    elif userT == "S":
                        p1score[2].append(userChoice)
                    else:
                        print("[ERROR]")
                        raise RuntimeError(
                            "var: userT not W; F; S | userT = " + str(userT))
                elif whoWins(userChoice, p2cards[p2random]) == False:
                    print("Lose")
                    if p2cards[p2random]["type"] == "W":
                        p2score[0].append(p2cards[p2random])
                    elif p2cards[p2random]["type"] == "F":
                        p2score[1].append(p2cards[p2random])
                    elif p2cards[p2random]["type"] == "S":
                        p1score[2].append(p2cards[p2random])
                    else:
                        raise RuntimeError(
                            "var: p2cards[" + str(p2random) + "] not W; F; S | p2cards[" + str(p2random) + "] = " + str(p2cards[p2random]))
                elif whoWins(userChoice, p2cards[p2random]) == "DRAW":
                    print("Draw")
                else:
                    raise RuntimeError(
                        "func: whoWins RETURN not True; False; DRAW | RETURN = " + str(whoWins(userChoice, p2cards[p2random])))
            else:
                raise RuntimeError(
                    "var: userChoice not in p1cards | userChoice = " + str(userChoice) + " | p1cards = " + str(p1cards))

            if isWin(p1score) == True:
                print("\n\n\nYOU WON THE GAME!!!\n\n\n")
                inGame = False
                break
            elif isWin(p2score) == True:
                print("\n\n\nYou losed the game.\n\n\n")
                inGame = False
                break
