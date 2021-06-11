import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("heart", 2)
        self.card2 = Card("spade", 10)
        self.card3 = Card("diamond", 1)
        self.card_game = CardGame()
        self.cards = [self.card1, self.card2, self.card3]

    def test_card_is_an_ace(self):
        self.assertAlmostEqual(True, self.card_game.check_for_ace(self.card3))

    def test_card_is_not_an_ace(self):
        self.assertAlmostEqual(False, self.card_game.check_for_ace(self.card1))

    def test_card1_is_not_higher_than_card2(self):
        self.assertAlmostEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    def test_card2_is_not_higher_than_card1(self):
        self.assertAlmostEqual(self.card2, self.card_game.highest_card(self.card2, self.card1))

    def test_card1_and_card2_total(self):
        self.assertAlmostEqual("You have a total of 13", self.card_game.cards_total(self.cards))