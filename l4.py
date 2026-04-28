from mef import MEF, StateNode

grammar = { '0', '1' }

# Definição dos Estados de L0
s0 = StateNode(accept_state=True)
s1 = StateNode(accept_state=True)
s2 = StateNode()

# Definição do L0
s0.addTransition(key='0', state_pointer=s1)
s0.addTransition(key='1', state_pointer=s2)
s1.addTransition(key='0', state_pointer=s1)
s1.addTransition(key='1', state_pointer=s1)
s2.addTransition(key='0', state_pointer=s2)
s2.addTransition(key='1', state_pointer=s2)

l4 = MEF(grammar=grammar)
l4.addState(state=s0)
l4.addState(state=s1)
l4.addState(state=s2)
l4.setStartState(state=s0)

grammar_l4 = [
    '111000',
    '1111001',
    '1101',
    '',
    '001',
]

print(f'MEF Grammar {l4.grammar}')
for string in grammar_l4:
    valid_string = l4.executeMEF(string)
    print(f'String [{string}] Valid: {valid_string}')