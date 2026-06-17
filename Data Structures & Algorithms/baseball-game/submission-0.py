class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        
        for op in operations:
            if op == '+':
                # Record a new score that is the sum of the previous two scores
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                # Record a new score that is the double of the previous score
                stack.append(stack[-1] * 2)
            elif op == 'C':
                # Invalidate the previous score, removing it from the record
                stack.pop()
            else:
                # op is an integer, record it
                stack.append(int(op))
                
        return sum(stack)




