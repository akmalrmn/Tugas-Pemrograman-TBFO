import os
from parserOneString import HTMLToString

class PDA:
    def __init__(self, file_path):
        self.start_input = ""  # input word to be accept or not accept
        self.accept = 0  # stores accept state
        self.accepted_config = []  # here we will post end configuration that was accepted

        # production rules ("read input", "pop stack", "push stack", "next state")
        self.transitions = {}

        #TUPLE PDA
        self.start_state = ""
        self.bottom_stack = ""
        self.acceptable_states = []
        self.type = ""

        self.parse_file(file_path)

    def parse_file(self, file_path):
        while not os.path.exists(file_path):
            print(f"Error: File not accept - {file_path}")
            file_path = input("Please enter a valid file path: ")
        
        lines = [line.rstrip() for line in open(file_path)]
        
        self.start_state = lines[3]
        self.bottom_stack = lines[4]
        self.acceptable_states = [x for x in lines[5].split()]
        self.type = lines[6]

        for line in lines[7:]:
            transition = line.split()
            self.add_transitions(transition[0], transition[1], transition[2], transition[3], transition[4])

    
    def add_transitions(self, state, input_symbol, stack_symbol, next_state, push_stack):
        if state not in self.transitions:
            self.transitions[state] = []

        configuration = (input_symbol, stack_symbol, push_stack, next_state)
        configuration = tuple(s if s != "~" else "" for s in configuration)

        self.transitions[state].append(configuration)
    
    def accepted(self, current_state, input, stack):
        if len(input) > 0:
            return 0

        if self.type == "E" and len(stack) == 0:
            return 1

        if self.type == "F" and current_state in self.acceptable_states:
            return 1

        return 0
    
    def finish(self):
        if self.accept:
            print("Accepted")
        else:
            print("Syntax Error")
        
        self.reset()

    def reset(self):
        self.accept = 0
        self.accepted_config = []
    
    def print_config(self, config):
        for i in config:
            print(i)

    def generate(self, state, input, stack, config):
        if self.accept:
            return 0

        if self.accepted(state, input, stack):
            self.accept = 1
            self.accepted_config.extend(config)
            return 1

        moves = self.get_moves(state, input, stack)
        if not moves:
            return 0

        total = 0
        for move in moves:
            next_state, next_input, next_stack = move
            total += self.generate(next_state, next_input, next_stack, config + [move])

        print(total)
        return total

    def get_moves(self, state, input, stack):
        moves = []

        if state in self.transitions:
            for current in self.transitions[state]:
                next_state, read_input, stack_symbol = current[3], current[0], current[1]

                if (not read_input or ((input and input[0] == read_input) or( input[0] == ' ' and read_input == '#') )) and (not stack_symbol or (stack and stack[0] == stack_symbol)):
                    new_input = input[1:] if read_input else input
                    new_stack = current[2] + stack[1:] if stack_symbol else current[2] + stack
                    moves.append((next_state, new_input, new_stack))

        print(moves)
        return moves
    
    def process_input(self):
        html_path = input("Masukkan file html: ")
        self.start_input = HTMLToString(html_path)
        print("Checking word \"" + self.start_input + "\" ...")

        while self.start_input != "end":
            # magic starts here
            if not self.generate(self.start_state, self.start_input, self.bottom_stack,
                                    [(self.start_state, self.start_input, self.bottom_stack)]):
                self.finish()
            else:
                self.print_config(self.accepted_config)  # show a list of configurations for acceptance
                self.finish()

            self.start_input = input("Enter your next word (or end):\n")
            print("Checking word \"" + self.start_input + "\" ...")


pda_instance = PDA("pda.txt")
pda_instance.process_input()

