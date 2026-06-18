class Solution:
    
    def mySqrt(self, x: int) -> int:
        i = 0

        if ( x < 0 ):
            return

        while True:
            if ((i*i) <= x and ((i+1)*(i+1)) > x):
                return i

            i += 1

            
