class MobileSuit:
    def __init__(self, name=None, type=None, rank=None, sLimit=None, cost=0, hp=None, ac=None, ag=None,
                 en=None, ec=None, dm=None, move=None, size=None, sp=None, carry=None, terrain="None"):
        self.name = name
        self.type = type
        self.rank = rank
        self.sLimit = sLimit
        self.cost = cost
        self.hp = hp
        self.ac = ac
        self.ag = ag
        self.en = en
        self.ec = ec
        self.dm = dm
        self.move = move
        self.size = size
        self.sp = sp
        self.carry = carry
        self.terrain = terrain

    def getType(self):
        return self.type

    def getRank(self):
        return self.rank

    def getCost(self):
        return str(self.cost)

    def getsLimit(self):
        return str(self.sLimit)

    def getHP(self):
        return str(self.hp)

    def getAC(self):
        return str(self.ac)

    def getAG(self):
        return str(self.ag)

    def getEN(self):
        return str(self.en)

    def getEC(self):
        return str(self.ec)

    def getDM(self):
        return str(self.dm)

    def getMove(self):
        return str(self.move)

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getTerrain(self):
        return self.terrain

    def setTerrain(self, terrain):
        self.terrain = terrain

    def getSP(self):
        return self.sp

    def setSP(self, sp):
        self.sp = sp

    def getCarry(self):
        return self.carry

    def setCarry(self, carry):
        self.carry = carry

    def setType(self, type):
        self.type = type

    def setRank(self, rank):
        self.rank = rank

    def setCost(self, cost):
        self.cost = cost

    def setLimit(self, sLimit):
        self.sLimit = sLimit

    def setHP(self, hp):
        self.hp = hp

    def setAC(self, ac):
        self.ac = ac

    def setAG(self, ag):
        self.ag = ag

    def setEN(self, en):
        self.en = en

    def setEC(self, ec):
        self.ec = ec

    def setDM(self, dm):
        self.dm = dm

    def setMove(self, move):
        self.move = move

    def setName(self, name):
        self.name = name
