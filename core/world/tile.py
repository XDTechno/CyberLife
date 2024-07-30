# block that can stack.
# almost the minimum unit of space
class Tile(list):
    def peek(self):
        return self[-1]
    def peek_or(self,default):
        if len(self)==0:
            return default
        return self.peek()

    def size(self):
        return len(self)
    def remove(self,input):
        if callable(input):
            try:
                for idx,item in enumerate(self):
                    if(input(item)):
                        self.pop(idx)
                        return 
            except:
                pass
        else :
            try:
                for idx,item in enumerate(self):
                    if(item == input):
                        self.pop(idx)
                        return 
            except:
                pass
    def remove_all(self,input):
        if callable(input):
            try:
                for idx,item in enumerate(self):
                    if(input(item)):
                        self.pop(idx)
            except:
                pass
        else :
            try:
                for idx,item in enumerate(self):
                    if(item == input):
                        self.pop(idx)
            except:
                pass