import pdb
from card import Card



def test_card_exists():
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")

    assert isinstance(card, Card)

def test_card_has_question():
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    assert card.question == "What is the capital of Alaska?"


def test_card_has_answer():
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    assert card.answer == "Juneau"

def test_card_has_category():
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    assert card.category == "Geography"



# RSpec.describe Card do
#   it 'exists' do
#     card = Card.new("What is the capital of Alaska?", "Juneau", :Geography)

#     expect(card).to be_instance_of(Card)
#   end

#   it 'has a question' do
#     card = Card.new("What is the capital of Alaska?", "Juneau", :Geography)

#     expect(card.question).to eq("What is the capital of Alaska?")
#   end

#   it 'has an answer' do
#     card = Card.new("What is the capital of Alaska?", "Juneau", :Geography)

#     expect(card.answer).to eq("Juneau")
#   end

#   it 'has a category' do
#     card = Card.new("What is the capital of Alaska?", "Juneau", :Geography)

#     expect(card.category).to eq(:Geography)
#   end
# end
