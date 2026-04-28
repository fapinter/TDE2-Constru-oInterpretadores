from __future__ import annotations
from typing import List, Set

class StateNode():
    def __init__(self, accept_state : bool = False):
        self.transitions = dict()
        self.acceptance_state = accept_state
    
    def addTransition(self, key: str, state_pointer : StateNode) -> None:
        self.transitions[key] = state_pointer
    
    def isAcceptable(self) -> bool:
        return self.acceptance_state



class MEF():
    def __init__(self, grammar : List[str]):
        self.states : Set[StateNode] = set()
        self.start_state = None
        self.grammar : Set[str] = set()
        for char in grammar:
            self.grammar.add(char)

    def addState(self, state: StateNode) -> None:
        self.states.add(state)
    
    def setStartState(self, state: StateNode) -> None:
        self.start_state = state

    def executeMEF(self, string : str) -> bool:
        curr_state = self.start_state
        for char in string:
            if char not in self.grammar:
                raise ValueError('Caracter não pertencente a gramática declarada')
            next_state = curr_state.transitions.get(char, None)
            if not next_state:
                raise KeyError('Transição faltante')
            if next_state not in self.states:
                raise ValueError('Estado não presente na MEF')
            curr_state = next_state
        return curr_state.isAcceptable()
            

            


