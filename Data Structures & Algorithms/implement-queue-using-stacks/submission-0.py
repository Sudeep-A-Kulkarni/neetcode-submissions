class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        """Pushes element x to the back of the queue."""
        self.input_stack.append(x)

    def pop(self) -> int:
        """Removes the element from the front of the queue and returns it."""
        self._move_input_to_output()
        return self.output_stack.pop()

    def peek(self) -> int:
        """Returns the element at the front of the queue."""
        self._move_input_to_output()
        return self.output_stack[-1]

    def empty(self) -> bool:
        """Returns true if the queue is empty, false otherwise."""
        return not self.input_stack and not self.output_stack

    def _move_input_to_output(self) -> None:
        """Helper method to shift elements only when output stack is empty."""
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()