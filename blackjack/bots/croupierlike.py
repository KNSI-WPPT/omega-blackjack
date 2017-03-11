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

    while b.player.current_hand.value <= 16:
        b.hit()

    try:
        b.stand()
    except Exception:
        pass

    if b.player.current_hand.winner == "Player":
        wins += 1
    b.count()
print(b.player.account_balance)
print(wins)