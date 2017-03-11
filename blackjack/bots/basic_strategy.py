from blackjack.bots.bot import Bot


b = Bot(cash=1000, seed=11)
wins = 0
bid = 10
for i in range(1000):

    if b.value > 8:
        t = b.begin(bid * 1.5)
    elif b.value < 8:
        t = b.begin(bid * 0.2)
    else:
        t = b.begin(bid)

    if b.player.current_hand.cards[1].rank == b.player.current_hand.cards[0].rank == 11:
        b.split()

    elif b.player.current_hand.cards[1].rank == b.player.current_hand.cards[0].rank == 10:
        b.stand()

    elif b.player.current_hand.cards[1].rank == b.player.current_hand.cards[0].rank == 9:
        if b.croupier.hand.cards[1].rank in [2, 3, 4, 5, 6, 8, 9]:
            b.split()
        else:
            b.stand()

    elif b.player.current_hand.cards[1].rank == b.player.current_hand.cards[0].rank == 8:
        b.split()

    elif b.player.current_hand.cards[1].rank == b.player.current_hand.cards[0].rank == 7:
        if b.croupier.hand.cards[1].rank in [2, 3, 4, 5, 6, 7]:
            b.split()
        else:
            b.hit()

    elif b.player.current_hand.cards[1].rank == b.player.current_hand.cards[0].rank == 6:
        if b.croupier.hand.cards[1].rank in [2, 3, 4, 5, 6]:
            b.split()
        else:
            b.hit()

    elif b.player.current_hand.cards[1].rank == b.player.current_hand.cards[0].rank == 5:
        if b.croupier.hand.cards[1].rank in [2, 3, 4, 5, 6, 7, 8, 9]:
            b.double_down()
        else:
            b.hit()

    elif b.player.current_hand.cards[1].rank == b.player.current_hand.cards[0].rank == 4:
        if b.croupier.hand.cards[1].rank in [5, 6]:
            b.split()
        else:
            b.hit()

    elif b.player.current_hand.cards[1].rank == b.player.current_hand.cards[0].rank == 3:
        if b.croupier.hand.cards[1].rank in [2, 3, 4, 5, 6]:
            b.split()
        else:
            b.hit()

    elif b.player.current_hand.cards[1].rank in [11, 9] and b.player.current_hand.cards[0].rank in [11, 9]:
        b.stand()

    elif b.player.current_hand.cards[1].rank in [11, 8] and b.player.current_hand.cards[0].rank in [11, 8]:
        b.stand()

    elif b.player.current_hand.cards[1].rank in [11, 7] and b.player.current_hand.cards[0].rank in [11, 7]:
        if b.croupier.hand.cards[1].rank in [3, 4, 5, 6]:
            b.double_down()
        elif b.croupier.hand.cards[1].rank in [2, 7, 8]:
            b.stand()
        else:
            b.hit()

    elif b.player.current_hand.cards[1].rank  in [11, 6] and b.player.current_hand.cards[0].rank in [11, 6]:
        if b.croupier.hand.cards[1].rank in [3, 4, 5, 6]:
            b.double_down()
        else:
            b.hit()

    elif b.player.current_hand.cards[1].rank in [11, 5] and b.player.current_hand.cards[0].rank in [11, 5]:
        if b.croupier.hand.cards[1].rank in [4, 5, 6]:
            b.double_down()
        else:
            b.hit()

    elif b.player.current_hand.cards[1].rank in [11, 4] and b.player.current_hand.cards[0].rank in [11, 4]:
        if b.croupier.hand.cards[1].rank in [4, 5, 6]:
            b.double_down()
        else:
            b.hit()

    elif b.player.current_hand.cards[1].rank in [11, 3] and b.player.current_hand.cards[0].rank in [11, 3]:
        if b.croupier.hand.cards[1].rank in [5, 6]:
            b.double_down()
        else:
            b.hit()

    elif b.player.current_hand.cards[1].rank in [11, 2] and b.player.current_hand.cards[0].rank in [11, 2]:
        if b.croupier.hand.cards[1].rank in [5, 6]:
            b.double_down()
        else:
            b.hit()

    if b.state.phase != "end_game":
        while b.player.current_hand.playing:

            if b.player.current_hand.value in [17, 18, 19, 20]:
                b.stand()

            elif b.player.current_hand.value in [13, 14, 15, 16]:
                if b.croupier.hand.cards[1].rank in [2, 3, 4, 5, 6]:
                    b.stand()
                else:
                    b.hit()

            elif b.player.current_hand.value == 12:
                if b.croupier.hand.cards[1].rank in [4, 5, 6]:
                    b.stand()
                else:
                    b.hit()

            elif b.player.current_hand.value == 11:
                if b.croupier.hand.cards[1].rank in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
                    try:
                        b.double_down()
                    except Exception:
                        b.hit()
                else:
                    b.hit()

            elif b.player.current_hand.value == 10:
                if b.croupier.hand.cards[1].rank in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
                    try:
                        b.double_down()
                    except Exception:
                        b.hit()
                else:
                    b.hit()

            elif b.player.current_hand.value == 9:
                if b.croupier.hand.cards[1].rank in [3, 4, 5, 6]:
                    try:
                        b.double_down()
                    except Exception:
                        b.hit()
                else:
                    b.hit()

            elif b.player.current_hand.value in [5, 6, 7, 8]:
                b.hit()


    if b.player.hands[0].winner == "Player" and b.player.hands[1].winner == "Player":
        wins +=2
    elif b.player.hands[1].winner == "Player" or b.player.hands[0].winner == "Player":
        wins +=1
    b.count()

print(b.player.account_balance)
print(wins)