class OS:
    def __init__(self, name="", cost=0, rank=None, sMod=None, lMod=None, uMod=None, loadout=None):
        self.name = name
        self.cost = cost
        self.sMod = sMod
        self.lMod = lMod
        self.uMod = uMod
        self.loadout = loadout
        self.rank = rank

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setCost(self, setCost):
        self.cost = setCost

    def getCost(self):
        return int(self.cost)

    def setRank(self, rank):
        self.rank = rank

    def getRank(self):
        return self.rank

    def setSMod(self, sMod):
        self.sMod = sMod

    def getSMod(self):
        return self.sMod

    def setLMod(self, lMod):
        self.lMod = lMod

    def getLMod(self):
        return self.lMod

    def setUMod(self, uMod):
        self.uMod = uMod

    def getUMod(self):
        return self.uMod

    def setLoadout(self, loadout):
        self.loadout = loadout

    def getLoadout(self):
        return self.loadout