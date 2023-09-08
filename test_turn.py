import pdb
from card import Card
from turn import Turn

def test_turn_exists():
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    turn = Turn("Juneau", card)

    assert isinstance(turn, Turn)

def test_turn_has_card():
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    turn = Turn("Juneau", card)

    assert turn.card == card

def test_turn_has_guess():
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    turn = Turn("Juneau", card)

    assert turn.guess == "Juneau"

def test_correct():
  card = Card("What is the capital of Alaska?", "Juneau", "Geography")
  turn = Turn("Juneau", card)


  assert turn.correct() == True

def test_feedback():
  card = Card("What is the capital of Alaska?", "Juneau", "Geography")
  turn = Turn("Juneau", card)

  assert turn.feedback() == "Correct!"

def test_feedback_incorrect():
  card = Card("What is the capital of Alaska?", "Juneau", "Geography")
  turn = Turn("Anchorage", card)

  assert turn.feedback() == "Incorrect."
