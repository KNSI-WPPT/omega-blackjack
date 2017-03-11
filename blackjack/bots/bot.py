from blackjack.bots.cmds import *


class Bot:
    def __init__(self, cash, seed):
        json = register(cash=cash, seed=seed)
        self.uid = json["uid"]
        self.seed = seed

        self.state = None
        self.player = None
        self.croupier = None

        self.number_of_cards = 0
        self.value = 0

    class State:
        def __init__(self, json):
            self.phase = json["phase"]
            self.bid = json["bid"]
            self.winnings = json["winnings"]

    class Hand:
        def __init__(self, json):
            self.cards = [Bot.Hand.Card(card) for card in json["cards"]]
            self.playing = json["playing"]
            self.value = json["value"]
            self.winner = json["winner"]

        class Card:
            def __init__(self, json):
                self.rank = json["rank"]
                self.color = json["color"]

    class Player:
        def __init__(self, json):
            self.hands = [Bot.Hand(hand) for hand in json["hands"]]
            self.current_hand = Bot.Hand(json["current_hand"])
            self.account_balance = json["account_balance"]

    class Croupier:
        def __init__(self, json):
            self.hand = Bot.Hand(json["hand"])

    def parse(self, json):
        self.state = Bot.State(json["state"])
        self.player = Bot.Player(json["player"])
        self.croupier = Bot.Croupier(json["croupier"])

    def begin(self, bid):
        self.parse(begin(self.uid, bid))

    def hit(self):
        self.parse(hit(self.uid))

    def split(self):
        self.parse(split(self.uid))

    def stand(self):
        self.parse(stand(self.uid))

    def double_down(self):
        self.parse(double_down(self.uid))

    def insure(self):
        self.parse(insure(self.uid))

    def surrender(self):
        self.parse(surrender(self.uid))

    def count(self):
        for hand in self.player.hands:
            for card in hand.cards:
                if self.number_of_cards == 52:
                    self.number_of_cards = 0
                else:
                    if card.rank in [2, 3, 6, 7]:
                        self.value +=1
                    elif card.rank in [4, 5]:
                        self.value +=2
                    elif card.rank in [10, 11, 12, 13]:
                        self.value -=2
        for card in self.croupier.hand.cards:
            if self.number_of_cards == 51:
                self.number_of_cards = 0
            else:
                if card.rank in [2, 3, 6, 7]:
                    self.value += 1
                elif card.rank in [4, 5]:
                    self.value += 2
                elif card.rank in [10, 11, 12, 13]:
                    self.value -= 2