import unittest
import cardjitsu
import random


class TestCardjitsu(unittest.TestCase):

    def test_whoWins_draw(self):
        randomType = random.choice(["S", "F", "W"])
        self.assertEqual(cardjitsu.whoWins(
            {"type": randomType},
            {"type": randomType}),
            "DRAW")

    def test_whoWins_p1(self):
        self.assertTrue(cardjitsu.whoWins(
            {
                "type": "W",
                "level": random.randrange(5, 11)
            },
            {
                "type": "F",
                "level": random.randrange(1, 5)
            }),
        )

    def test_whoWins_p2(self):
        self.assertFalse(cardjitsu.whoWins(
            {
                "type": "W",
                "level": random.randrange(1, 5)
            },
            {
                "type": "F",
                "level": random.randrange(5, 11)
            }),
        )

    def test_isWin_True_1t3c(self):
        self.assertTrue(
            cardjitsu.isWin(
                [
                    [
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "R"
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "G"
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "B"
                        }
                    ],
                    [],
                    []
                ]
            )
        )

    def test_isWin_False_1t3c(self):
        self.assertFalse(
            cardjitsu.isWin(
                [
                    [
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "R"
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "R"
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "R"
                        }
                    ],
                    [],
                    []
                ]
            )
        )

    def test_isWin_True_3t3c(self):
        self.assertTrue(
            cardjitsu.isWin(
                [
                    [
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "R"
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "R"
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "R"
                        }
                    ],
                    [
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "G"
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "G"
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "G"
                        }
                    ],
                    [
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "B"
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "B"
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": "B"
                        }
                    ]
                ]
            )
        )

    def test_isWin_False_3t3c(self):
        randomColor = random.choice(["R", "G", "B"])
        self.assertFalse(
            cardjitsu.isWin(
                [
                    [
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": randomColor
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": randomColor
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": randomColor
                        }
                    ],
                    [
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": randomColor
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": randomColor
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": randomColor
                        }
                    ],
                    [
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": randomColor
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": randomColor
                        },
                        {
                            "type": random.choice(["W", "S", "F"]),
                            "level": random.randrange(1, 11),
                            "color": randomColor
                        }
                    ]
                ]
            )
        )


if __name__ == '__main__':
    unittest.main()
