#Problem available at: https://leetcode.com/problems/min-stack/submissions/
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> None:
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()  
minStack.pop()
minStack.top()     
minStack.getMin()

#==============================================================================

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min is None or self.min > x:
            self.min = x
        
    def pop(self) -> None:
        popped =  self.stack.pop()
        if self.stack :
            self.min = min(self.stack)
        else:
            self.min = None
        return popped
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
    

# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()  
minStack.pop()
minStack.top()     
minStack.getMin()