# from classes.deck import Deck
from classes.deck import Deck
from classes.card import Card
import random
from classes.__init__ import *


bicycle = Deck()

bicycle.show_cards()


card = Card('Spades', 6, 'Jack' )

deck = Deck()
deck.shuffle()
deck.show_cards()


christian = Player('christian')
christian.sayHello()
christian.draw(deck, 5)
christian.showHand()



