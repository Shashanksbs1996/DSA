from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deckFrequencies  = Counter(deck).values()
        X = math.gcd(*deckFrequencies)
        if X > 1:
            return True
        return False