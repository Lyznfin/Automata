from typing import Set, Union
import re

def auth(sets: Set[Union[str, int]]) -> None:
    pattern = r'^[a-zA-Z0-9]*$'
    for inp in sets:
        if not re.match(pattern, str(inp)):
            raise TypeError("Invalid input")

class DFA:
    def __init__(self, Q: Set[Union[str, int]], Sigma: Set[Union[str, int]], delta: dict[tuple[Union[str, int], Union[str, int]], Union[str, int]], q0: Union[str, int], F: Set[Union[str, int]]) -> None:
        self.Q = Q # Set of states
        self.Sigma = Sigma # Set of simbols
        self.delta = delta # Transition function as dict
                           # (q2, 1) = q1
        self.q0 = q0 # Starting state
        self.F = F # Set of final states

    @property
    def Q(self) -> Set[Union[str, int]]:
        return self.__Q
    
    @Q.setter
    def Q(self, value: Set[Union[str, int]]) -> None:
        auth(value)
        self.__Q = value

    @property
    def Sigma(self) -> Set[Union[str, int]]:
        return self.__Sigma
    
    @Sigma.setter
    def Sigma(self, value: Set[Union[str, int]]) -> None:
        auth(value)
        self.__Sigma = value

    @property
    def delta(self) -> dict[tuple[Union[str, int], Union[str, int]], Union[str, int]]:
        return self.__delta
    
    @delta.setter
    def delta(self, value: dict[tuple[Union[str, int], Union[str, int]], Union[str, int]]) -> None:
        keys: list[tuple[Union[str, int], Union[str, int]]] = value.keys()
        for key in keys:
            if not key[0] in self.Q or not key[1] in self.Sigma:
                raise KeyError("Invalid transition keys")
        
        values: Union[str, int] = value.values()
        for val in values:
            if not val in self.Q:
                raise KeyError("Invalid transition values")

        self.__delta = value

    @property
    def q0(self) -> Union[str, int]:
        return self.__q0
    
    @q0.setter
    def q0(self, value: Union[str, int]) -> None:
        if value in self.Q:
            self.__q0 = value
        else:
            raise TypeError("Invalid input")

    @property
    def F(self) -> Set[Union[str, int]]:
        return self.__F
    
    @F.setter
    def F(self, value: Set[Union[str, int]]) -> None:
        for val in value:
            if not val in self.Q:
                raise KeyError("Invalid input")
        self.__F = value

    def run(self, L: str) -> Union[bool, None]:
        state = self.q0
        is_int = isinstance(next(iter(self.delta.keys()))[1], int)
        for c in L:
            try:
                state = self.delta[(state, c)] if not is_int else self.delta[(state, int(c))]
            except Exception:
                # Why no raise? Because I no want program crash
                # Crash makes sad, me no want sad :(
                return f"{c} is not within the accepted set of symbols of {self.Sigma}"
        return state in self.F
    
    def __repr__(self) -> str:
        return f"Q: {self.Q}\nSigma: {self.Sigma}\nDelta: {self.delta}\nq0: {self.q0}\nF: {self.F}"
    

if __name__ == '__main__':
    pass