class Direction(object):
    LEFT = "0"
    RIGHT = "00"

    @staticmethod
    def is_valid(char):
        return char in [Direction.LEFT, Direction.RIGHT]

class Tape(object):
    def __init__(self, input, blank_symbol):
        self.blank_symbol = blank_symbol
        self.tape = {}
        self.head_position = 0
        for index, item in enumerate(input):
            self.tape[index] = item

    def move_left(self):
        self.head_position -= 1

    def move_right(self):
        self.head_position += 1

    def read(self):
        if self.head_position in self.tape:
            return self.tape[self.head_position]
        return self.blank_symbol

    def write(self, value):
        self.tape[self.head_position] = value

    def __str__(self):
        str = ""
        for value in self.tape.values():
            str += value
        return str