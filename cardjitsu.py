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
import random
import time

"""
===HOW TO WIN===
1. You have the same card type (water, fire, snow), but three in different colors (Red, Green, Blue).
2. You have NOT the same card type, but three in different colors, and types.
"""


def whoWins(p1card, p2card):
    if p1card["type"] == p2card["type"]:
        return "DRAW"

    if p1card["level"] > p2card["level"]:
        return True
    elif p1card["level"] < p2card["level"]:
        return False
    else:
        return "DRAW"


def isWin(cards):
    try:
        for i in range(0, 3):
            idkvar = cards[i][0]["color"]
            if idkvar != cards[i][1]["color"] and idkvar != cards[i][2]["color"] and cards[i][1]["color"] != cards[i][2]["color"]:
                return True
        idkvar = cards[0][0]["color"]
        if idkvar != cards[1][0]["color"] and idkvar != cards[2][0]["color"] and cards[1][0]["color"] != cards[2][0]["color"]:
            return True

        return False
    except:
        notImportant = random.random()


if __name__ == '__main__':
    print("\nCovered Software is provided under this License on an \"as is\" basis, without warranty of any kind, either expressed, implied, or statutory, including, without limitation, warranties that the Covered Software is free of defects, merchantable, fit for a particular purpose or non-infringing. The entire risk as to the quality and performance of the Covered Software is with You. Should any Covered Software prove defective in any respect, You(not any Contributor) assume the cost of any necessary servicing, repair, or correction. This disclaimer of warranty constitutes an essential part of this License. No use of any Covered Software is authorized under this License except under this disclaimer.\n")
    print("Version: 1.0.0-alpha.1")
    while True:
        inGame = True
        p1cards = []
        p1score = [[], [], []]

        p2cards = []
        p2score = [[], [], []]

        for i in range(5):
            p1cards.append({
                "type": random.choice(["W", "F", "S"]),
                "level": random.randrange(0, 11),  # FIXME: 0 nem lehet
                "color": random.choice(["R", "G", "B"])
            })
        for i in range(5):
            p2cards.append({
                "type": random.choice(["W", "F", "S"]),
                "level": random.randrange(0, 11),
                "color": random.choice(["R", "G", "B"])
            })

        while inGame == True:
            for i in range(0, 2):
                if len(p1score[i]) != 0:
                    if len(p1score[i]) == 1:
                        print("Water cards: " + p1score[i][0])
                    elif len(p1score[i]) == 2:
                        print("Water cards: " +
                              p1score[i][0] + "; " + p1score[i][1])
                    else:
                        print(
                            "Water cards: " + p1score[i][0] + "; " + p1score[i][1] + "; " + p1score[i][2])

            print("Your cards: " + str(p1cards))
            userT = input("Write the type of your choiced card>")
            userL = int(input("Write the level of your choiced card>"))
            userC = input("Write the color of your choiced card>")
            if {"type": userT, "level": userL, "color": userC} in p1cards:
                p2random = random.randrange(0, 4)
                if whoWins({"type": userT, "level": userL, "color": userC}, p2cards[p2random]) == True:
                    print("WIN!")
                    if userT == "W":
                        p1score[0].append(
                            {"type": userT, "level": userL, "color": userC})
                    elif userT == "F":
                        p1score[1].append(
                            {"type": userT, "level": userL, "color": userC})
                    else:
                        p1score[2].append(
                            {"type": userT, "level": userL, "color": userC})
                elif whoWins({"type": userT, "level": userL, "color": userC}, p2cards[p2random]) == False:
                    print("Lose")
                    if p2cards[p2random]["type"] == "W":
                        p2score[0].append(p2cards[p2random])
                    elif p2cards[p2random]["type"] == "F":
                        p2score[1].append(p2cards[p2random])
                    else:
                        p1score[2].append(p2cards[p2random])
                else:
                    print("Draw")
            time.sleep(60)
