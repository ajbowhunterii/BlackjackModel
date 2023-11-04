import random

class Deck:
    def draw_card(self):
        # Draw a random card from 1-13
        card = random.randint(1, 13)
        # Return either card value or 10 if card is a face card
        return min(card, 10)
    
def simulate_dealer(dealer_upcard, deck):
    dealer_hand = [dealer_upcard, deck.draw_card()]
    while sum(dealer_hand) < 17:
        dealer_hand.append(deck.draw_card())
    return sum(dealer_hand)

def simulate_player(player_hand, dealer_upcard, deck):
    if sum(player_hand) > 21:
        return -1  # Player busts
    if sum(player_hand) >= 17:
        # Player stands, now simulate the dealer's hand
        dealer_total = simulate_dealer(dealer_upcard, deck)
        if dealer_total > 21 or sum(player_hand) > dealer_total:
            return 1  # Player wins
        elif sum(player_hand) == dealer_total:
            return 0  # Push
        else:
            return -1  # Player loses

    # Expected value of hitting
    hit_outcomes = [simulate_player(player_hand + [deck.draw_card()], dealer_upcard, deck) for _ in range(1000)]
    hit_ev = sum(hit_outcomes) / 1000.0

    # Expected value of standing
    stand_outcomes = [simulate_dealer(dealer_upcard, deck) for _ in range(1000)]
    stand_wins = sum(1 for outcome in stand_outcomes if outcome < sum(player_hand) or outcome > 21)
    stand_pushes = sum(1 for outcome in stand_outcomes if outcome == sum(player_hand))
    stand_losses = 1000 - stand_wins - stand_pushes
    stand_ev = (stand_wins - stand_losses) / 1000.0

    # Return the expected values
    return hit_ev, stand_ev

if __name__ == "__main__":
    deck = Deck()
    for dealer_upcard in range(1, 11):
        for player_initial_total in range(4, 21):  # Assuming player won't hit below 4
            player_hand = [player_initial_total - 1, 1]  # Simplified initial hand
            hit_ev, stand_ev = simulate_player(player_hand, dealer_upcard, deck)
            optimal_strategy = 'hit' if hit_ev > stand_ev else 'stand'
            print(f"Dealer shows: {dealer_upcard}, Player has: {player_initial_total}, Optimal strategy: {optimal_strategy}")
