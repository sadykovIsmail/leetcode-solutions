class MyStack:
    def __init__(self):
        # store elements
        self.data = []

    def push(self, x: int) -> None:
        """Insert an element into the stack."""
        self.data.append(x)

    def is_empty(self) -> bool:
        """Checks whether the stack is empty or not."""
        # An empty list evaluates to False in Python, but len() == 0 is very explicit
        return len(self.data) == 0

    def top(self) -> int:
        """Get the top item from the stack."""
        # Using -1 accesses the very last element in a Python list
        return self.data[-1]

    def pop(self) -> bool:
        """Delete an element from the stack. Return true if the operation is successful."""
        if self.is_empty():
            return False
        # Python's built-in pop() removes the last element automatically
        self.data.pop() 
        return True


# This is Python's equivalent to "public static void main"
if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    s.push(3)
    
    for i in range(4):
        if not s.is_empty():
            print(s.top())
        print(s.pop())