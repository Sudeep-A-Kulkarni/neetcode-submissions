class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # Sort to easily pair the heaviest and lightest remaining people
        people.sort()
        
        boats = 0
        l = 0                  # Lightest pointer
        r = len(people) - 1    # Heaviest pointer
        
        while l <= r:
            # If the heaviest and lightest can share, the lightest gets on board
            if people[l] + people[r] <= limit:
                l += 1
            
            # The heaviest person always takes up a boat slot (either alone or paired)
            r -= 1
            boats += 1
            
        return boats