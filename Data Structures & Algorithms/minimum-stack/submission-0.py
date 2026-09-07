class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.minstack[-1] if self.minstack else val)
        #compare the new value and the value alr present in minstack and see which one is minimum and return self.minstack if not empty if empty return val
        self.minstack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
