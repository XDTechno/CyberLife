# block that can stack.
# almost the minimum unit of space
class Tile(list):
    def peek(self):
        return self[-1]
    def peek_or_default(self,default):
        if len(self)==0:
            return default
        return self.peek()

    def size(self):
        return len(self)