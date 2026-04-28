from mef import MEF, StateNode

grammar = { '0', '1' }

# Definição dos Estados de L0
s0 = StateNode()
s1 = StateNode()
s2 = StateNode(accept_state=True)

# Definição do L0
s0.addTransition(key='0', state_pointer=s1)
s0.addTransition(key='1', state_pointer=s0)
s1.addTransition(key='0', state_pointer=s2)
s1.addTransition(key='1', state_pointer=s0)
s2.addTransition(key='0', state_pointer=s2)
s2.addTransition(key='1', state_pointer=s0)
l1 = MEF(grammar=grammar)
l1.addState(state=s0)
l1.addState(state=s1)
l1.addState(state=s2)
l1.setStartState(state=s0)

grammar_l1 = [
    '111000',
    '1111001',
    '1101',
    '00',
    '100',
]

print(f'MEF Grammar {l1.grammar}')
for string in grammar_l1:
    valid_string = l1.executeMEF(string)
    print(f'String [{string}] Valid: {valid_string}')