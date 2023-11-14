import random
import itertools

# class Deck:
#     def draw_card(self):
#         # Draw a random card from 1-13
#         card = random.randint(1, 13)
#         # Return either card value or 10 if card is a face card
#         return min(card, 10)
    
# def simulate_dealer(dealer_upcard, deck):
#     dealer_hand = [dealer_upcard, deck.draw_card()]
#     while sum(dealer_hand) < 17:
#         dealer_hand.append(deck.draw_card())
#     return sum(dealer_hand)

# def simulate_player(player_hand, dealer_upcard, deck):
#     if sum(player_hand) > 21:
#         return -1  # Player busts
#     if sum(player_hand) >= 17:
#         # Player stands, now simulate the dealer's hand
#         dealer_total = simulate_dealer(dealer_upcard, deck)
#         if dealer_total > 21 or sum(player_hand) > dealer_total:
#             return 1  # Player wins
#         elif sum(player_hand) == dealer_total:
#             return 0  # Push
#         else:
#             return -1  # Player loses

#     # If the player's hand is less than 17, simulate the expected value of hitting
#     if sum(player_hand) < 17:
#         hit_outcomes = [simulate_player(player_hand + [deck.draw_card()], dealer_upcard, deck) for _ in range(1000)]
#         hit_ev = sum(hit_outcomes) / 1000.0
#         return hit_ev

#     # This point should not be reached because the function should return before here
#     raise ValueError("Reached an unexpected point in simulate_player")

# def make_decision(player_hand, dealer_upcard, deck):
#     # If the player's hand is less than 17, simulate hitting and standing to decide
#     if sum(player_hand) < 17:
#         hit_ev = simulate_player(player_hand + [deck.draw_card()], dealer_upcard, deck)
#         # Simulate standing
#         dealer_total = simulate_dealer(dealer_upcard, deck)
#         if dealer_total > 21 or sum(player_hand) > dealer_total:
#             stand_ev = 1  # Player wins
#         elif sum(player_hand) == dealer_total:
#             stand_ev = 0  # Push
#         else:
#             stand_ev = -1  # Player loses
#         return 'hit' if hit_ev > stand_ev else 'stand'
#     else:
#         # If the player's hand is 17 or more, always stand
#         return 'stand'

# if __name__ == "__main__":
#     deck = Deck()
#     for dealer_upcard in range(1, 11):
#         for player_initial_total in range(4, 21):  # Assuming player won't hit below 4
#             player_hand = [player_initial_total - 1, 1]  # Simplified initial hand
#             optimal_strategy = make_decision(player_hand, dealer_upcard, deck)
#             print(f"Dealer shows: {dealer_upcard}, Player has: {player_initial_total}, Optimal strategy: {optimal_strategy}")



def main():
    card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    effectiveness = 0
    
    two_card_combinations = itertools.combinations_with_replacement(card_values, 2)

    # Function to calculate the sum of the cards in a hand
    def hand_value(hand):
        return sum(hand)

    # Create an array to store all possible hand values
    hand_values = []

    # Add the values of all 2-card and 3-card combinations
    for hand in two_card_combinations:
        hand_values.append(hand_value(hand))

    # Sort the hand values for better readability
    hand_values.sort()

    for init_hand in hand_values:
        hits = 0
        hand = init_hand
        dealer_hand = random.choice(hand_values)

        while hand < 17:
            # if hits > 2:
            #     break
            hand += random.choice(card_values)
            if hand > 21:
                effectiveness -= 1

        while dealer_hand < 17:
            dealer_hand += random.choice(card_values)

        if hand < dealer_hand:
            effectiveness -= 1
        elif hand > dealer_hand:
            effectiveness += 1

        return effectiveness
        
if __name__ == "__main__":
    num = 0
    outcomes = [0] * 100000

    while num < 100000:
        outcomes[num] = main()
        num += 1

    avg_eff = sum(outcomes) / len(outcomes)
    print(avg_eff)