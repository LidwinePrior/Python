# Encapsulation

# Public method            surface
class Blackboard:
    def __init__(self):
        self.surface = ""

    def write(self, message_written):
        if self.surface != "":
            self.surface += '\n'
        self.surface += message_written
    
    def read(self):
        return self.surface
    
board = Blackboard()
board.write("an another message")
board.surface = "Hello guy's"
board.read()
# output = "Hello guy's"



# Protected method         _surface
class Blackboard:
    def __init__(self):
        self._surface = ""
    def write(self, message_written):
        if self._surface != "":
            self._surface += '\n'
        self._surface += message_written
    
    def read(self):
        return self._surface
    
board = Blackboard()
board.write("an another message")
board._surface = "Hello guy's"
board.read()
# output = "Hello guy's"



# Private method          __surface
class Blackboard:
    def __init__(self):
        self.__surface = ""
    def write(self, message_written):
        if self.__surface != "":
            self.__surface += '\n'
        self.__surface += message_written
    
    def read(self):
        return self.__surface
    
board = Blackboard()
board.__surface = "Hello guy's"
board.read()    
# output = ""
