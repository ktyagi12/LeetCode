#Problem available at: https://leetcode.com/problems/implement-queue-using-stacks/submissions/
class MyQueue:

    def __init__(self):
        self.stack = []       

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        return self.stack.pop(0)
        
    def peek(self) -> int:
        if len(self.stack) > 0:
            return self.stack[0] 

    def empty(self) -> bool:
        return True if len(self.stack) == 0 else False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()