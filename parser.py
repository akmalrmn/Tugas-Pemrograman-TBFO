import sys
import re

def parse_pda_definition(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    pda = {
    'states': {'q0', 'q1', 'q2', 'q3'},
    'input_symbols': {'<tag>', '</tag>'},
    'stack_symbols': {'Z', '<tag>'},
    'start_state': 'q0',
    'start_stack': 'Z',
    'accept_states': {'q0'},
    'accept_condition': 'E',
    'transitions': {
        ('q0', '<tag>', 'Z'): [('q1', '<tag>')],
        ('q1', '<tag>', '<tag>'): [('q1', '<tag>'), ('q1', '<tag>')],
        ('q1', '</tag>', '<tag>'): [('q2', 'e')],
        ('q2', '</tag>', '<tag>'): [('q2', 'e')],
        ('q2', 'e', 'Z'): [('q0', 'Z')],
    }
}

    for line in lines[7:]:
      state, symbol, stack_top, *rest = line.strip().split()
      if (state, symbol, stack_top) not in pda['transitions']:
          pda['transitions'][(state, symbol, stack_top)] = []
      pda['transitions'][(state, symbol, stack_top)].append(tuple(rest))

    return pda

def check_html_syntax(pda, file_path):
    with open(file_path, 'r') as file:
        html = file.read()

    symbols = re.findall(r'<[^>]*>', html)  # Extract symbols from the HTML file

    stack = [pda['start_stack']]
    state = pda['start_state']

    for symbol in symbols:
        print(f"Current State: {state}, Symbol: {symbol}, Stack: {stack}")

        if stack and (state, symbol, stack[-1]) in pda['transitions']:
            transitions = pda['transitions'][(state, symbol, stack[-1])]
            state, new_stack_top = transitions[0]  
            if new_stack_top != 'e':
                stack.append(new_stack_top)
            else:
                stack.pop()
        else:
            return 'Syntax Error'

    if state not in pda['accept_states'] and len(stack) == 1 and stack[0] == pda['start_stack']:
        return 'Accepted'
    else:
        return 'Syntax Error'

pda_file = sys.argv[1]
html_file = sys.argv[2]

pda = parse_pda_definition(pda_file)
result = check_html_syntax(pda, html_file)

print(result)