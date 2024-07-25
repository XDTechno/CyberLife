# block that can stack.
# almost the minimum unit of space
class Tile(list):
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
