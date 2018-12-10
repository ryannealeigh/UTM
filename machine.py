from tape import Tape, Direction
from transition import TransitionTable, Transition

class TuringMachine(object):
    def __init__(self, machine_description_file):
        with open(machine_description_file) as input_file:
            init_string = input_file.read()
            split = init_string.split("111")
            machine_info = split[0]
            transitions = split[1]
            inputtape = split[2]
            split_machine = machine_info.split("1")
            print("**************Universal Turing Machine**************")
            print("\nUsing the following metadata:")
            print(machine_info)
            print("\nUsing the following transitions:")
            print(transitions)

            if len(split_machine) != 7:
                raise ValueError('Incorrect number of metadata fields')
            self.states = split_machine[0]
            self.tape_symbols = split_machine[1]
            self.input_symbols = split_machine[2]
            self.blank_symbol = split_machine[3]
            self.current_state = split_machine[4]
            self.accept_state = split_machine[5]
            self.reject_state = split_machine[6]

        self.transition_table = TransitionTable()

        print("\nTransition table: ")
        print("st1\tsym1\tst2\tsym2\tdir")

        if transitions:
            split_transitions = transitions.split("11")
            for transition in split_transitions:
                self.transition_table.add_transition(Transition.create_from_string(transition))
        self.tape = Tape(inputtape.split("1"), self.blank_symbol)

    def run(self):
        count = 0
        while self.current_state != self.accept_state:
            if self.current_state == self.reject_state:
                print("\nTotal head moves: {}".format(count))
                print("Rejected")
                break
            count += 1
            current_symbol = self.tape.read()
            # print("state: {}, symbol: {}".format(self.current_state, current_symbol))
            transition = self.transition_table.get_transition(self.current_state, current_symbol)
            self.tape.write(transition.next_symbol)
            if transition.tape_motion == Direction.RIGHT:
                self.tape.move_right()
            elif transition.tape_motion == Direction.LEFT:
                self.tape.move_left()
            self.current_state = transition.next_state
        if self.current_state == self.accept_state:
            print("\nTotal head moves: {}".format(count))
            print("Accepted")
        return self.tape