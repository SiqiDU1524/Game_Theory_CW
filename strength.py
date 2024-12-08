#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[28]:


import random
from itertools import combinations

# Define a deck of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['h', 'd', 'c', 's']
deck = [rank + suit for rank in ranks for suit in suits]

# Function to calculate hand strength with ratio-based weighting for pairs
def calculate_hand_strength_with_ratio(hand):
    """
    Calculate the strength of a given two-card hand with ratio-based weighting for pairs.
    """
    # Extract card ranks and suits
    rank1, suit1 = hand[0][0], hand[0][1]
    rank2, suit2 = hand[1][0], hand[1][1]
    
    # Base strength based on rank
    rank_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                  '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    rank1_value = rank_order[rank1]
    rank2_value = rank_order[rank2]
    
    # Calculate initial strength (sum of ranks)
    strength = rank1_value + rank2_value
    
    # Pair logic: add proportional strength for pocket pairs
    if rank1 == rank2:
        pair_ratio = 0.5 * (rank1_value / 14)  # Example: 50% increase for Aces
        strength *= (1 + pair_ratio)  # Scale strength proportionally
    
    # Bonus for suited cards
    if suit1 == suit2:
        strength += 5  # Add bonus for suited cards
    
    # Bonus for connected cards
    if abs(rank1_value - rank2_value) == 1 or ('A' in [rank1, rank2]) and ('2' in [rank1, rank2]):
        strength += 3  # Add bonus for connected cards
    
    return strength

# Function to compare hands based on hand strength
def compare_hands_with_strength(your_hand, opponent_hand):
    """
    Compare two hands using the hand strength formula.
    Returns 1 if your hand is stronger, 0.5 if tied, and 0 if opponent's hand is stronger.
    """
    your_strength = calculate_hand_strength_with_ratio(your_hand)
    opponent_strength = calculate_hand_strength_with_ratio(opponent_hand)
    if your_strength > opponent_strength:
        return 1
    elif your_strength < opponent_strength:
        return 0
    else:
        return 0.5

# Calculate your hand's win rate against a random opponent
def calculate_win_rate(your_hand, num_simulations=10000):
    """
    Simulate win rate for a given hand against random opponent hands.
    """
    # Remove your hand from the deck
    available_deck = [card for card in deck if card not in your_hand]
    win_count = 0
    tie_count = 0

    for _ in range(num_simulations):
        # Randomly select opponent hand
        random.shuffle(available_deck)
        opponent_hand = available_deck[:2]
        result = compare_hands_with_strength(your_hand, opponent_hand)
        if result == 1:
            win_count += 1
        elif result == 0.5:
            tie_count += 1

    # Calculate win rate
    win_rate = win_count / num_simulations
    tie_rate = tie_count / num_simulations
    lose_rate = 1 - win_rate - tie_rate
    return win_rate, tie_rate, lose_rate

# Example: Your hand
your_hand = ['Jd','Kh']
win_rate, tie_rate, lose_rate = calculate_win_rate(your_hand, num_simulations=100000)

# Display results
print(f"Win rate: {win_rate:.2%}")
print(f"Tie rate: {tie_rate:.2%}")
print(f"Lose rate: {lose_rate:.2%}")


# In[ ]:





# In[ ]:




