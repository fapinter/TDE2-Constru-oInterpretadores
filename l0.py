from mef import MEF, StateNode

grammar = { '0', '1' }

# Definição dos Estados de L0
s0 = StateNode(accept_state=True)
s1 = StateNode()
s2 = StateNode()

# Definição do L0
s0.addTransition(key='0', state_pointer=s1)
s0.addTransition(key='1', state_pointer=s0)
s1.addTransition(key='0', state_pointer=s2)
s1.addTransition(key='1', state_pointer=s0)
s2.addTransition(key='0', state_pointer=s2)
s2.addTransition(key='1', state_pointer=s2)
l0 = MEF(grammar=grammar)
l0.addState(state=s0)
l0.addState(state=s1)
l0.addState(state=s2)
l0.setStartState(state=s0)

grammar_l0 = [
    '11110101101111011',
    '11111',
    '1101',
    '110',
    '0'
]

print(f'MEF Grammar {l0.grammar}')
for string in grammar_l0:
    valid_string = l0.executeMEF(string)
    print(f'String [{string}] Valid: {valid_string}')