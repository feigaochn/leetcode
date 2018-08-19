"""
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W,
and consists of W consecutive cards.

Return true if and only if she can.

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.

Note:

    1 <= hand.length <= 10000
    0 <= hand[i] <= 10^9
    1 <= W <= hand.length
"""


class Solution:

    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        from collections import Counter

        if len(hand) % W != 0:
            return False

        cards = Counter(hand)
        while cards:
            m = min(cards)
            for i in range(W):
                if m + i not in cards:
                    return False
                else:
                    cards[m + i] -= 1
                    if cards[m + i] == 0:
                        del cards[m + i]
        return True


sol = Solution().isNStraightHand
tests = [
    (([1, 2, 3, 6, 2, 4, 3, 7, 8], 3), True),
    (([1, 2, 3, 4, 5, 6], 4), False),
    (([1, 2, 3, 4, 5, 6], 3), True),
]
for inputs, expect in tests:
    print(sol(*inputs), " ?= ", expect)
