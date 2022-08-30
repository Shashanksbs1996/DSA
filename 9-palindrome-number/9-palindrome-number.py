class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        anti_x=x[::-1]
        if x == anti_x:
            return True
        else:
            return False
        