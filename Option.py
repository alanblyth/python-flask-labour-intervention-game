from typing import List
from Outcome import Outcome

class Option:

    def __init__(self, name) -> None:
        self.name = name
        self.key = None
        self.outcomes = None

    def setKey(self, key: int) -> None:
        self.key = key
    
    def setOutcomes(self, outcomes: List[Outcome]) -> None:
        self.outcomes = outcomes
 
    def getName(self) -> str:
        return self.name

    def getKey(self) -> int:
        return self.key
    
    def getOutcomes(self) -> List[Outcome]:
        return self.outcomes