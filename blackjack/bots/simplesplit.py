from blackjack.bots.bot import Bot

b = Bot(cash=1000, seed=11)
wins = 0
bid = 10
for i in range(1000):
    if b.value > 7:
        t = b.begin(bid * 1.5)
    elif b.value < 7:
        t = b.begin(bid * 0.2)
    else:
        t = b.begin(bid)

    # if card[0].rank == card[1].rank split
    if b.player.current_hand.cards[1].rank == b.player.current_hand.cards[0].rank:
        b.split()

    # hit hand[0] until value >16
    while b.player.current_hand.value <= 16:
        b.hit()

    #if hand[0] value >21, don't stand hand[1]
    if b.player.current_hand.value >=17:
        try:
            b.stand()

        except Exception:
            pass

    # hit hand[1] until >16
    if b.player.hands[0].playing or b.player.hands[1].playing:
        while b.player.current_hand.value <= 16:
            b.hit()

        try:
            b.stand()

        except Exception:
            pass

    if b.player.hands[0].winner == "Player" and b.player.hands[1].winner == "Player":
        wins +=2
    elif b.player.hands[1].winner == "Player" or b.player.hands[0].winner == "Player":
        wins +=1
    b.count()
print(b.player.account_balance)
print(wins)