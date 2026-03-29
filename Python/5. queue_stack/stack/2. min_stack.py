class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.min = []
        self.min_size = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.size += 1
        if self.min:

            if val <= self.min[self.min_size - 1]:
                self.min.append(val)
                self.min_size += 1
        else:
            self.min.append(val)
            self.min_size += 1

        return
    
    def pop(self) -> None:
        if not self.stack:
            return False
        else:
            item = self.stack.pop()
            self.size -= 1
            if self.min:
                if self.min[self.min_size - 1] == item:
                    self.min.pop()
                    self.min_size -= 1
            return



    def top(self) -> int:
        if self.stack:
            item = self.stack.pop()
            self.stack.append(item)
            return item
        return
    

    def getMin(self) -> int:
        if self.min:
            item = self.min.pop()
            self.min.append(item)
            return item
        return


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.getMin()
obj.pop()
obj.top()
obj.getMin()

