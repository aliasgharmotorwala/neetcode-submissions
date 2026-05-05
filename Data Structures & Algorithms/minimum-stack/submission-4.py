class LinkList:
    def __init__(self, val=None, previous=None, min=None):
        self.val = val
        self.previous = previous
        self.min = min

class MinStack:

    def __init__(self):
        self.val = None
        self.previous = None
        self.min = None
        
    def push(self, val: int) -> None:
        if self.val is None:
            self.val = LinkList(val=val, min=val)
            self.min = val
        else:
            new = LinkList(val=val, previous=self.val)
            self.previous = self.val
            self.val = new
            if val < self.min:
                self.min = val
            self.val.min = self.min
        
    def pop(self) -> None:
        previous = self.previous
        self.val = self.previous
        if previous is not None:
            self.previous = previous.previous
        else:
            self.previous = None
        if self.val is not None:
            self.min = self.val.min
        else:
            self.min = None


    def top(self) -> int:
        return self.val.val
        

    def getMin(self) -> int:
        return self.min