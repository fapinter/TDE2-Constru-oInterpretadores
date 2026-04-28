from mef import MEF, StateNode

grammar = { '0', '1' }

# Definição dos Estados de L0
s0 = StateNode()
s1 = StateNode()
s2 = StateNode()
s3 = StateNode(accept_state=True)
s4 = StateNode()

# Definição do L0
s0.addTransition(key='0', state_pointer=s1)
s0.addTransition(key='1', state_pointer=s0)
s1.addTransition(key='0', state_pointer=s2)
s1.addTransition(key='1', state_pointer=s1)
s2.addTransition(key='0', state_pointer=s3)
s2.addTransition(key='1', state_pointer=s2)
s3.addTransition(key='0', state_pointer=s4)
s3.addTransition(key='1', state_pointer=s3)
s4.addTransition(key='0', state_pointer=s4)
s4.addTransition(key='1', state_pointer=s4)

l2 = MEF(grammar=grammar)
l2.addState(state=s0)
l2.addState(state=s1)
l2.addState(state=s2)
l2.addState(state=s3)
l2.addState(state=s4)
l2.setStartState(state=s0)

grammar_l2 = [
    '111000',
    '1111001',
    '1101',
    '00',
    '100',
]

print(f'MEF Grammar {l2.grammar}')
for string in grammar_l2:
    valid_string = l2.executeMEF(string)
    print(f'String [{string}] Valid: {valid_string}')