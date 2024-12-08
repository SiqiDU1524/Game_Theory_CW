# Game_Theory_CW

A hand strength model is constructed in Python to simulate players’ assessments of their hand strength before engaging in betting. Players can form a macro-level understanding of their hand’s likelihood of winning.

In Texas Hold'em poker, card rankings are ordered in ascending strength as follows: '2', '3', '4', '5', '6', '7', '8', '9', 'T' (Ten), 'J' (Jack), 'Q' (Queen), 'K' (King), and 'A' (Ace), with '2' being the weakest and 'Ace' the strongest. The suits—hearts ('h'), diamonds ('d'), clubs ('c'), and spades ('s')—are considered of equal value and do not influence card strength.

A Python program calculates the strength of a given two-card hand (referred to as "hole cards") by assigning weighted ratios to specific combinations, such as pairs. The program then simulates 100,000 games to evaluate the performance of the hand against randomly generated opponent hands, providing win, tie, and loss probabilities.

For example, given an input of your_hand = ['Jd', 'Kh']—representing a Jack of Diamonds and a King of Hearts—the program computes the following probabilities:
•	Win rate: 84.04%
•	Tie rate: 3.80%
•	Loss rate: 12.16%.
This approach allows for a comprehensive statistical analysis of hand strength in a competitive context.
