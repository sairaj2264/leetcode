class MyStack:

    def __init__(self):
        self.queue = []
        self.size = 0
        self.start = -1
        self.end = -1
        

    def push(self, x: int) -> None:
        if self.start == -1:
            self.queue = []
            self.queue.append(x)
            self.start = 0
            self.end = 0
        else:
            self.queue.append(x)
            self.end += 1

        

    def pop(self) -> int:
        if self.end != -1:
            temp = self.queue[self.end]
            self.end -= 1
            self.queue.pop()
            if self.start > self.end:
                self.start = -1
                self.end = -1
            return temp
        else:
            temp = self.queue[self.start]
            self.start = -1
            self.end = -1
            return temp

    def top(self) -> int:
        temp = self.queue[self.end]
        return temp
        
    def empty(self) -> bool:
        if self.start == -1 and self.end == -1:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()