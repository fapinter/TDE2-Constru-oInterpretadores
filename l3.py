from mef import MEF, StateNode

grammar = { '0', '1' }

# Definição dos Estados de L0
s0 = StateNode()
s1 = StateNode(accept_state=True)
s2 = StateNode()

# Definição do L0
s0.addTransition(key='0', state_pointer=s2)
s0.addTransition(key='1', state_pointer=s1)
s1.addTransition(key='0', state_pointer=s1)
s1.addTransition(key='1', state_pointer=s1)
s2.addTransition(key='0', state_pointer=s2)
s2.addTransition(key='1', state_pointer=s2)

l3 = MEF(grammar=grammar)
l3.addState(state=s0)
l3.addState(state=s1)
l3.addState(state=s2)
l3.setStartState(state=s0)

grammar_l3 = [
    '111000',
    '1111001',
    '1101',
    '00',
    '001',
]

print(f'MEF Grammar {l3.grammar}')
for string in grammar_l3:
    valid_string = l3.executeMEF(string)
    print(f'String [{string}] Valid: {valid_string}')