# Blueprint for queue
class MyQueue:
    def __init__(self):
        self.data = []      # store elements
        self.p_start = 0    # pointer to indicate the start position

    # Insert an element into the queue
    def enQueue(self, x):
        self.data.append(x)
        return True

    # Delete an element from the queue
    def deQueue(self):
        if self.isEmpty():
            return False
        self.p_start += 1
        return True

    # Get the front item from the queue
    def Front(self):
        return self.data[self.p_start]

    # Checks whether the queue is empty or not
    def isEmpty(self):
        return self.p_start >= len(self.data)


# Main equivalent
if __name__ == "__main__":
    q = MyQueue()
    q.enQueue(5)
    q.enQueue(3)

    if not q.isEmpty():
        print(q.Front())

    q.deQueue()
    if not q.isEmpty():
        print(q.Front())

    q.deQueue()
    if not q.isEmpty():
        print(q.Front())