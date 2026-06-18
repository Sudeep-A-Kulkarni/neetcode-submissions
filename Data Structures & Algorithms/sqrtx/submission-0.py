class Solution:
    def mySqrt(self, x: int) -> int:
        square = 0
        i = 0
        ODD = 1

        # Check if adding the next odd number keeps us within x
        while square + ODD <= x:
            square = square + ODD
            ODD = ODD + 2
            i += 1  # Only increment i if the square safely fits inside x

        return i
