class PDA:
    def __init__(self):
        self.start_input = ""  # input word to be found or not found
        self.found = 0  # stores found state
        self.accepted_config = []  # here we will post end configuration that was accepted

        # production rules ("read input", "pop stack", "push stack", "next state")
        self.productions = {}

        # start state
        self.start_symbol = ""

        # start stack symbol
        self.start_stack = ""

        # list of acceptable states
        self.acceptable_states = []

        # E - accept on an empty stack or F - acceptable state (default is false)
        self.accept_with = ""

    # recursively generate all possibility tree and terminate on success
    def generate(self, state, input, stack, config):
        total = 0

        # check for other tree node success
        if self.found:
            return 0

        # check if our node can terminate with success
        if self.is_found(state, input, stack):
            self.found = 1  # mark that the word is accepted so other tree nodes know and terminate

            # add successful configuration
            self.accepted_config.extend(config)

            return 1

        # check if there are further moves (or we have to terminate)
        moves = self.get_moves(state, input, stack, config)
        if len(moves) == 0:
            return 0

        # for each move do a tree
        for i in moves:
            total += self.generate(i[0], i[1], i[2], config + [(i[0], i[1], i[2])])

        return total

    # checks if symbol is terminal or non-terminal
    def get_moves(self, state, input, stack, config):
        moves = []

        for i in self.productions:
            if i != state:
                continue

            for j in self.productions[i]:
                current = j
                new = []

                new.append(current[3])

                # read symbol from input if we have one
                if len(current[0]) > 0:
                    if len(input) > 0 and input[0] == current[0]:
                        new.append(input[1:])
                    else:
                        continue
                else:
                    new.append(input)

                # read stack symbol
                if len(current[1]) > 0:
                    if len(stack) > 0 and stack[0] == current[1]:
                        new.append(current[2] + stack[1:])
                    else:
                        continue
                else:
                    new.append(current[2] + stack)

                moves.append(new)

        return moves

    # checks if word already was generated somewhere in the past
    def is_found(self, state, input, stack):
        # check if all symbols are read
        if len(input) > 0:
            return 0

        # check if we accept with an empty stack or end state
        if self.accept_with == "E":
            if len(stack) < 1:  # accept if the stack is empty
                return 1

            return 0

        else:
            for i in self.acceptable_states:
                if i == state:  # accept if we are in the terminal state
                    return 1

            return 0

    # print list of current configuration
    def print_config(self, config):
        for i in config:
            print(i)

    def parse_file(self, filename):
        try:
            lines = [line.rstrip() for line in open(filename)]

        except FileNotFoundError:
            return 0

        # add start state
        self.start_symbol = lines[3]

        # add start stack symbol
        self.start_stack = lines[4]

        # list of acceptable states
        self.acceptable_states.extend(lines[5].split())

        # E - accept on an empty stack or F - acceptable state (default is false)
        self.accept_with = lines[6]

        # add rules
        for i in range(7, len(lines)):
            production = lines[i].split()

            configuration = [(production[1], production[2], production[4], production[3])]

            if not production[0] in self.productions.keys():
                self.productions[production[0]] = []

            configuration = [tuple(s if s != "~" else "" for s in tup) for tup in configuration]

            self.productions[production[0]].extend(configuration)

        return 1

    # checks if the symbol is terminal or non-terminal
    def done(self):
        if self.found:
            print("Hurray! Input word \"" + self.start_input + "\" is part of the grammar.")
        else:
            print("Sorry! Input word \"" + self.start_input + "\" is not part of the grammar.")

    # UI
    def process_input(self):
        filename = input("Please enter your automata file:\n")
        while not self.parse_file(filename):
            print("File not found!")
            filename = input("Please enter your automata file again:\n")
        print("Automata built.")

        self.start_input = input("Please enter your word:\n")
        print("Checking word \"" + self.start_input + "\" ...")

        # while self.start_input != "end":
        #     # magic starts here
        #     if not self.generate(self.start_symbol, self.start_input, self.start_stack,
        #                          [(self.start_symbol, self.start_input, self.start_stack)]):
        #         self.done()
        #     else:
        #         self.print_config(self.accepted_config)  # show a list of configurations for acceptance
        #         self.done()

        #     self.start_input = input("Enter your next word (or end):\n")
        #     print("Checking word \"" + self.start_input + "\" ...")


# Create an instance of the PDA class
pda_instance = PDA()
# Process user input
pda_instance.process_input()
print(pda_instance.productions)
