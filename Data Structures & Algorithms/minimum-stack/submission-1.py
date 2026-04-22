class MinStack:

    def __init__(self):
        self.stack = []
        # self.minStack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if self.stack:
            self.stack.pop()
    
    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.stack:
            return min(self.stack)


















        

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     val = min(val, self.minStack[-1] if self.minStack else val)
    #     self.minStack.append(val)


        

    # def pop(self) -> None:
    #     if self.stack:
    #         self.stack.pop()
    #         self.minStack.pop()

    # def top(self) -> int:
    #     if self.stack:
    #         return self.stack[-1]
        

    # def getMin(self) -> int:
    #     return self.minStack[-1]

        
