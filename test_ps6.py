# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest

import Prob1
import Prob2

class Test_Prob1:

    def test_class_named_Card(self):
        assert 'Card' in dir(Prob1), "Did you name your class Card?"

    def test_str_method_created(self):
        student = Prob1.Card(0,3)
        assert '__main__' not in str(student), "Did you define a __str__ method that returns something?"

    def test_str_method_correct(self):
        inputs = [(3,0), (12,3), (10,2), (1,1)]
        outputs = ["3C", "QS", "TH", "AD"]
        for i,o in zip(inputs, outputs):
            student = Prob1.Card(*i)
            assert str(student) == o, f"The card with inputs {i} should look like {o} but instead looks like {str(student)}."

    def test_get_rank_exists(self):
        student = Prob1.Card(3,0)
        assert 'get_rank' in dir(student), "Did you create a get_rank method?"

    def test_get_rank_correct(self):
        inputs = [(3,0), (12,3), (10,2), (1,1)]
        outputs = [3,12,10,1]
        for i,o in zip(inputs, outputs):
            student = Prob1.Card(*i)
            assert student.get_rank() == o, f"The card with inputs {i} should return {o} from get_rank but instead return {student.get_rank()}."

    def test_get_suit_exists(self):
        student = Prob1.Card(3,0)
        assert 'get_suit' in dir(student), "Did you create a get_suit method?"

    def test_get_suit_correct(self):
        inputs = [(3,0), (12,3), (10,2), (1,1)]
        outputs = [0,3,2,1]
        for i,o in zip(inputs, outputs):
            student = Prob1.Card(*i)
            assert student.get_suit() == o, f"The card with inputs {i} should return {o} from get_suit but instead return {student.get_rank()}."


class Test_Prob2:

    def test_class_named_Deck(self):
        assert 'Deck' in dir(Prob2), "Did you name your class Deck?"

    def test_str_method_created(self):
        student = Prob2.Deck()
        assert '__main__' not in str(student), "Did you define a __str__ method that returns something?"

    def test_str_method_prints_nice_card_representations(self):
        student = Prob2.Deck()
        assert len(str(student)) < 52*5, "All the cards in your deck should be printed with their two character codes, and that does not seem to be the case here?"

    def test_get_deck_exists(self):
        student = Prob2.Deck()
        assert 'get_deck' in dir(student), "Did you create a get_deck method?"

    def test_get_deck_functions_correctly(self):
        student = Prob2.Deck()
        assert type(student.get_deck()) == list, "get_deck is not returning a list?"
        assert type(student.get_deck()[0]) == Prob1.Card, "The elements of get_deck are not card elements?"
        deck = student.get_deck()
        deck.pop(0)
        assert deck != student.get_deck(), "It looks like you returned a reference to your deck attribute instead of a copy of it."

    def test_initial_deck(self):
        student = Prob2.Deck()
        assert len(student.get_deck()) == 52, f"Your initial deck size should be 52 but instead is {len(student.get_deck())}. Or your get_deck method is broken."
        deck = student.get_deck()
        for suit in range(3):
            assert 13 == sum([1 for card in deck if card.get_suit()==suit]), "You don't seem to have 13 cards of each suit in your deck initially. Or your get_deck method is broken."

    def test_shuffle_exists(self):
        student = Prob2.Deck()
        assert 'shuffle' in dir(student), "Did you create a shuffle method?"

    def test_shuffle_works(self):
        student = Prob2.Deck()
        d1 = student.get_deck()
        student.shuffle()
        d2 = student.get_deck()
        assert d1 != d2, "Is your shuffle method properly scrambling the card order? Or your get_deck is not returning a copy."
    def test_draw_exists(self):
        student = Prob2.Deck()
        assert 'draw' in dir(student), "Did you create a draw method?"

    def test_draw_functions_correctly(self):
        student = Prob2.Deck()
        curdeck = student.get_deck()
        topcard = curdeck[0]
        assert student.draw() == topcard, "You are not returning the top card of your deck when you draw it?"
        assert len(student.get_deck()) == len(curdeck)-1, "Your deck size is not decreasing by one once you have drawn the card? Or your get_deck is not returning a copy."
        assert topcard not in student.get_deck(), "The drawn card is still within your deck for some reason?"
