class MyQueue:

    def __init__(self):
        self.stacka = deque()
        self.stackb = deque()
        

    def push(self, x: int) -> None:

        n = len(self.stackb)
        self.stacka = []
        for i in range(0,n):
            temp = self.stackb.pop()
            self.stacka.append(temp)
        self.stacka.append(x)
        for i in range(0,n+1):
            temp = self.stacka.pop()
            self.stackb.append(temp)

    def pop(self) -> int:
        temp = self.stackb.pop()
        return temp
        

    def peek(self) -> int:
        return self.stackb[-1]

    def empty(self) -> bool:
        if len(self.stackb) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()