import sys
import re

def parse_pda_definition(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    pda = {'states': set(lines[0].strip().split()),
           'input_symbols': set(lines[1].strip().split()),
           'stack_symbols': set(lines[2].strip().split()),
           'start_state': lines[3].strip(),
           'start_stack': lines[4].strip(),
           'accept_states': set(lines[5].strip().split()),
           'accept_condition': lines[6].strip(),
           'transitions': {}}

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