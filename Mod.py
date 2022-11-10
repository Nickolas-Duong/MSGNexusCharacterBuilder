class Mod:
    def __init__(self, name="", cost=0, description="", level=0, sm=0, lm=0, um=0, effect=""):
        self.name = name
        self.level = level
        self.cost = cost
        self.description = description
        self.sm = sm
        self.lm = lm
        self.um = um
        self.effect = effect

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setLevel(self, level):
        self.level = level

    def getLevel(self):
        return self.level

    def setCost(self, cost):
        self.cost = cost

    def getCost(self):
        return self.cost

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def setSM(self, sm):
        self.sm = sm

    def getSM(self):
        return self.sm

    def setLM(self, lm):
        self.lm = lm

    def getLM(self):
        return self.lm

    def setUM(self, um):
        self.um = um

    def getUM(self):
        return self.um

    def setEffect(self, effect):
        self.effect = effect

    def getEffect(self):
        return self.effect
