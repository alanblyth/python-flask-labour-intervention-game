class Outcome:

    def __init__(self, name) -> None:
        self.name = name
        self.likelihood = None
        self.goto = None
        self.key = None
    
    def setLikelihood(self, likelihood: int) -> None:
        self.likelihood = likelihood

    def setGoto(self, goto: int) -> None:
        self.goto = goto

    def setKey(self, key: int) -> None:
        self.key = key
 
    def getName(self) -> str:
        return self.name
    
    def getLikelihood(self) -> int:
        return self.likelihood
    
    def getGoto(self) -> int:
        return self.goto

    def getKey(self) -> int:
        return self.key