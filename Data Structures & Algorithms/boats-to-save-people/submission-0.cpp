class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # Step 1: Sort the people by weight
        people.sort()
        
        left = 0
        right = len(people) - 1
        boats = 0
        
        # Step 2: Pair them up using two pointers
        while left <= right:
            # If the lightest and heaviest person can fit in the same boat
            if people[left] + people[right] <= limit:
                left += 1  # Lightest person is paired, move to the next lightest
            
            # The heaviest person will always take a boat (either paired or alone)
            right -= 1
            boats += 1  # Increment the boat count
            
        return boats