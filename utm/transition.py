from tape import Direction

class NoSuchTransitionError(Exception):
    pass

class TransitionParsingError(Exception):
    pass

class Transition(object):
    def __init__(self, state_current, symbol_current, next_state, next_symbol, tape_motion):
        self.current_tuple = (state_current, symbol_current)
        self.next_state = next_state
        self.next_symbol = next_symbol
        self.tape_motion = tape_motion

    @staticmethod
    def create_from_string(transition):
        split = transition.split("1")

        print(split)

        if len(split) != 5:
            raise TransitionParsingError("Transition '{}' has incorrect number of arguments".format(transition))
        if not Direction.is_valid(split[4]):
            raise TransitionParsingError("Transition '{}' has invalid tape direction '{}'".format(transition, split[4]))
        return Transition(split[0], split[1], split[2], split[3], split[4])

class TransitionTable(object):
    def __init__(self):
        self.transitions = {}

    def add_transition(self, transition):
        self.transitions[transition.current_tuple] = transition

    def get_transition(self, state_current, symbol_current):
        state_symbol_tuple = (state_current, symbol_current)
        if state_symbol_tuple in self.transitions:
            return self.transitions[state_symbol_tuple]
        raise NoSuchTransitionError()