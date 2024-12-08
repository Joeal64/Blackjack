import random

def blackjack():
    def draw_card():
        return random.choice(["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])

    def calculate_score(hand):
        score = 0
        ace_count = hand.count("A")
        for card in hand:
            if card in "JQK":
                score += 10
            elif card == "A":
                score += 11
            else:
                score += int(card)
        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
        return score

    print("Welcome to Blackjack!")
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    while True:
        print(f"\nYour hand: {player_hand} | Score: {calculate_score(player_hand)}")
        print(f"Dealer's visible card: {dealer_hand[0]}")
        if calculate_score(player_hand) > 21:
            print("You went over 21! You lose.")
            return
        choice = input("Hit or Stand? (h/s): ").lower()
        if choice == "h":
            player_hand.append(draw_card())
        else:
            break

    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(draw_card())

    print(f"\nDealer's hand: {dealer_hand} | Score: {calculate_score(dealer_hand)}")
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if dealer_score > 21 or player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("You lose!")
    else:
        print("It's a tie!")

blackjack()
