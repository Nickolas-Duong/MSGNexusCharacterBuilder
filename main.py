import tkinter
import MobileSuit
import OS
import Mod
from tkinter import *
from tkinter import messagebox
import math
from tkinter import ttk
from pathlib import Path
import textwrap

root = Tk()
mech = MobileSuit.MobileSuit()
os = OS.OS()
mods = None

mModList = []
modSelect = []


def wrap(string, length=120):
    return '\n'.join(textwrap.wrap(string, length))


with open('Modifications.txt', 'r+', encoding='utf-8') as t:
    count = 0
    itemCount = 0
    for line in t.readlines():
        if count == 0:
            mModList.append(Mod.Mod())
            mModList[itemCount].setName(line.replace('\n', ''))
            count = count + 1
        elif count == 1:
            mModList[itemCount].setCost(line.replace('\n', ''))
            count = count + 1
        elif count == 2:
            mModList[itemCount].setDescription(line.replace('\n', ''))
            count = count + 1
        elif count == 3:
            mModList[itemCount].setLevel(line.replace('\n', ''))
            count = count + 1
        elif count == 4:
            mModList[itemCount].setSM(line.replace('\n', ''))
            count = count + 1
        elif count == 5:
            mModList[itemCount].setLM(line.replace('\n', ''))
            count = count + 1
        elif count == 6:
            mModList[itemCount].setUM(line.replace('\n', ''))
            count = count + 1
        else:
            mModList[itemCount].setEffect(line.replace('\n', ''))
            count = 0
            itemCount = itemCount + 1
t.close()


def rankSelect(a, b, c):
    rank = rankClicked.get()
    if typeClicked.get() == "MS":
        match rank:
            case "E":
                mech.setCost(0)
                mech.setLimit(16)
                mech.setHP(100)
                mech.setAC(20)
                mech.setAG(10)
                mech.setMove(3)
                mech.setEN(20)
                mech.setEC(10)
                mech.setDM(8)
                mech.setSize(1)
                mech.setCarry(0)
                mech.setSP(0)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))

                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "D":
                mech.setCost(100)
                mech.setLimit(22)
                mech.setHP(160)
                mech.setAC(30)
                mech.setAG(16)
                mech.setMove(4)
                mech.setEN(35)
                mech.setEC(12)
                mech.setDM(10)
                mech.setSize(1)
                mech.setCarry(0)
                mech.setSP(0)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "C":
                mech.setCost(350)
                mech.setLimit(28)
                mech.setHP(255)
                mech.setAC(55)
                mech.setAG(23)
                mech.setMove(4)
                mech.setEN(60)
                mech.setEC(14)
                mech.setDM(12)
                mech.setSize(1)
                mech.setCarry(0)
                mech.setSP(0)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "B":
                mech.setCost(800)
                mech.setLimit(34)
                mech.setHP(410)
                mech.setAC(95)
                mech.setAG(31)
                mech.setMove(4)
                mech.setEN(95)
                mech.setEC(16)
                mech.setDM(14)
                mech.setSize(1)
                mech.setCarry(0)
                mech.setSP(0)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "A":
                mech.setCost(1400)
                mech.setLimit(40)
                mech.setHP(655)
                mech.setAC(150)
                mech.setAG(40)
                mech.setMove(5)
                mech.setEN(140)
                mech.setEC(18)
                mech.setDM(16)
                mech.setSize(1)
                mech.setCarry(0)
                mech.setSP(0)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "S":
                mech.setCost(2200)
                mech.setLimit("No Limit")
                mech.setHP(1050)
                mech.setAC(220)
                mech.setAG(50)
                mech.setMove(5)
                mech.setEN(200)
                mech.setEC(20)
                mech.setDM(18)
                mech.setSize(1)
                mech.setCarry(0)
                mech.setSP(0)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()
    elif typeClicked.get() == "MA":
        match rank:
            case "E":
                mech.setCost(0)
                mech.setLimit(10)
                mech.setHP(50)
                mech.setAC(10)
                mech.setAG(24)
                mech.setMove(5)
                mech.setEN(10)
                mech.setEC(12)
                mech.setDM(8)
                mech.setSize(1)
                mech.setCarry(0)
                mech.setSP(0)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "D":
                mech.setCost(75)
                mech.setLimit(18)
                mech.setHP(120)
                mech.setAC(30)
                mech.setAG(28)
                mech.setMove(5)
                mech.setEN(25)
                mech.setEC(15)
                mech.setDM(10)
                mech.setSize(1)
                mech.setCarry(0)
                mech.setSP(0)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "C":
                mech.setCost(250)
                mech.setLimit(26)
                mech.setHP(260)
                mech.setAC(60)
                mech.setAG(32)
                mech.setMove(5)
                mech.setEN(40)
                mech.setEC(18)
                mech.setDM(12)
                mech.setSize(1)
                mech.setCarry(0)
                mech.setSP(0)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "B":
                mech.setCost(800)
                mech.setLimit(34)
                mech.setHP(540)
                mech.setAC(110)
                mech.setAG(36)
                mech.setMove(5)
                mech.setEN(80)
                mech.setEC(17)
                mech.setDM(15)
                mech.setSize("3 or 4")
                mech.setCarry(0)
                mech.setSP(0)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "A":
                mech.setCost(1800)
                mech.setLimit(42)
                mech.setHP(960)
                mech.setAC(190)
                mech.setAG(40)
                mech.setMove(5)
                mech.setEN(160)
                mech.setEC(17)
                mech.setDM(18)
                mech.setSize("7" + u"\u00B1" + "1")
                mech.setCarry(0)
                mech.setSP(0)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "S":
                mech.setCost(3200)
                mech.setLimit("No Limit")
                mech.setHP(1520)
                mech.setAC(310)
                mech.setAG(44)
                mech.setMove(5)
                mech.setEN(320)
                mech.setEC(16)
                mech.setDM(21)
                mech.setSize("13" + u"\u00B1" + "2")
                mech.setCarry(0)
                mech.setSP(0)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()
    elif typeClicked.get() == "Ship":
        match rank:
            case "E":
                mech.setCost(0)
                mech.setLimit(None)
                mech.setHP(None)
                mech.setAC(None)
                mech.setAG(None)
                mech.setMove(None)
                mech.setEN(None)
                mech.setEC(None)
                mech.setDM(None)
                mech.setSize(None)
                mech.setCarry(None)
                mech.setSP(None)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "D":
                mech.setCost(200)
                mech.setLimit(15)
                mech.setHP(550)
                mech.setAC(150)
                mech.setAG(10)
                mech.setMove(4)
                mech.setEN(100)
                mech.setEC(9)
                mech.setDM(13)
                mech.setSize("6" + u"\u00B1" + "1")
                mech.setCarry(6)
                mech.setSP(15)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "C":
                mech.setCost(800)
                mech.setLimit(25)
                mech.setHP(900)
                mech.setAC(220)
                mech.setAG(20)
                mech.setMove(4)
                mech.setEN(180)
                mech.setEC(10)
                mech.setDM(16)
                mech.setSize("9" + u"\u00B1" + "1")
                mech.setCarry(9)
                mech.setSP(30)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "B":
                mech.setCost(2000)
                mech.setLimit(35)
                mech.setHP(1350)
                mech.setAC(290)
                mech.setAG(30)
                mech.setMove(4)
                mech.setEN(260)
                mech.setEC(11)
                mech.setDM(19)
                mech.setSize("13" + u"\u00B1" + "2")
                mech.setCarry(13)
                mech.setSP(45)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "A":
                mech.setCost(3800)
                mech.setLimit("No Limit")
                mech.setHP(1900)
                mech.setAC(360)
                mech.setAG(40)
                mech.setMove(5)
                mech.setEN(340)
                mech.setEC(12)
                mech.setDM(22)
                mech.setSize("18" + u"\u00B1" + "2")
                mech.setCarry(18)
                mech.setSP(60)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()

            case "S":
                mech.setCost(0)
                mech.setLimit(None)
                mech.setHP(None)
                mech.setAC(None)
                mech.setAG(None)
                mech.setMove(None)
                mech.setEN(None)
                mech.setEC(None)
                mech.setDM(None)
                mech.setSize(None)
                mech.setCarry(None)
                mech.setSP(None)

                carryText.set("Carry Limit: " + str(mech.getCarry()))
                spText.set("SP: " + str(mech.getSP()))
                statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
                costMText.set("Cost: " + str(mech.getCost()))
                hpText.set("HP: " + str(mech.getHP()))
                acText.set("AC: " + str(mech.getAC()))
                agText.set("AG: " + str(mech.getAG()))
                moveText.set("Move: " + str(mech.getMove()))
                enText.set("EN: " + str(mech.getEN()))
                ecText.set("EC: " + str(mech.getEC()))
                dmText.set("DM: " + str(mech.getDM()))
                sizeText.set("Unit Size: " + str(mech.getSize()))

                updateCost()


def typeSelect(a, b, c):
    rankSelect(0, 0, 0)
    orankSelect(0, 0, 0)

    if typeClicked.get() == "None":
        rankDrop.config(state=DISABLED)
        terrainDrop.config(state=DISABLED)
        slotUpdate.config(state=DISABLED)
        modButton.config(state=DISABLED)
        osDrop.config(state=DISABLED)
        rankDrop2.config(state=DISABLED)

        mech.setCost(0)
        mech.setLimit(None)
        mech.setHP(None)
        mech.setAC(None)
        mech.setAG(None)
        mech.setMove(None)
        mech.setEN(None)
        mech.setEC(None)
        mech.setDM(None)
        mech.setSize(None)
        mech.setCarry(None)
        mech.setSP(None)
        carryText.set("Carry Limit: " + str(mech.getCarry()))
        spText.set("SP: " + str(mech.getSP()))
        statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
        costMText.set("Cost: " + str(mech.getCost()))
        hpText.set("HP: " + str(mech.getHP()))
        acText.set("AC: " + str(mech.getAC()))
        agText.set("AG: " + str(mech.getAG()))
        moveText.set("Move: " + str(mech.getMove()))
        enText.set("EN: " + str(mech.getEN()))
        ecText.set("EC: " + str(mech.getEC()))
        dmText.set("DM: " + str(mech.getDM()))
        sizeText.set("Unit Size: " + str(mech.getSize()))

        updateCost()
    else:
        rankDrop.config(state=NORMAL)
        terrainDrop.config(state=NORMAL)
        osDrop.config(state=NORMAL)
        rankDrop2.config(state=NORMAL)
        terrainDrop.config(state=NORMAL)
        modButton.config(state=NORMAL)
        rankSelect(0, 0, 0)
        orankSelect(0, 0, 0)


def updateCost():
    total = int(mech.getCost())
    total = int(total) + os.getCost()

    if checkTerrain():
        total = int(total) + int(100)

    costText.set("Cost: " + str(total))


def checkTerrain():
    for i, v in enumerate(mech.getTerrain()):
        if v == "+":
            return True


def terrainSelect(a, b, c):
    mech.setTerrain(str(terrainClicked.get()))
    updateCost()


def osSelect(a, b, c):
    smE.insert(0, str(os.getSMod()))
    lmE.insert(0, str(os.getLMod()))
    umE.insert(0, str(os.getUMod()))
    loadoutE.insert(0, str(os.getLoadout()))
    orankSelect(0, 0, 0)


def orankSelect(a, b, c):
    rank = orankClicked.get()

    if osClicked.get() != osOptions[10]:
        smE.config(state=DISABLED)
        lmE.config(state=DISABLED)
        umE.config(state=DISABLED)
        slotUpdate.config(state=DISABLED)

    if osClicked.get() == osOptions[0]:
        baseCost = 0
        match rank:
            case "E":
                os.setCost((int(baseCost) * int(rankMult[0])))
                os.setSMod(1)
                os.setLMod(1)
                os.setUMod(2)
                os.setLoadout(2)
            case "D":
                os.setCost((int(baseCost) * int(rankMult[1])))
                os.setSMod(2)
                os.setLMod(2)
                os.setUMod(4)
                os.setLoadout(3)
            case "C":
                os.setCost((int(baseCost) * int(rankMult[2])))
                os.setSMod(4)
                os.setLMod(4)
                os.setUMod(6)
                os.setLoadout(3)
            case "B":
                os.setCost((int(baseCost) * int(rankMult[3])))
                os.setSMod(6)
                os.setLMod(6)
                os.setUMod(9)
                os.setLoadout(4)
            case "A":
                os.setCost((int(baseCost) * int(rankMult[4])))
                os.setSMod(9)
                os.setLMod(9)
                os.setUMod(12)
                os.setLoadout(4)
            case "S":
                os.setCost((int(baseCost) * int(rankMult[5])))
                os.setSMod(12)
                os.setLMod(12)
                os.setUMod(16)
                os.setLoadout(5)
    elif osClicked.get() == osOptions[1]:
        baseCost = 15
        match rank:
            case "E":
                os.setCost((int(baseCost) * int(rankMult[0])))
                os.setSMod(2)
                os.setLMod(0)
                os.setUMod(2)
                os.setLoadout(3)
            case "D":
                os.setCost((int(baseCost) * int(rankMult[1])))
                os.setSMod(4)
                os.setLMod(1)
                os.setUMod(4)
                os.setLoadout(4)
            case "C":
                os.setCost((int(baseCost) * int(rankMult[2])))
                os.setSMod(6)
                os.setLMod(3)
                os.setUMod(6)
                os.setLoadout(4)
            case "B":
                os.setCost((int(baseCost) * int(rankMult[3])))
                os.setSMod(9)
                os.setLMod(5)
                os.setUMod(9)
                os.setLoadout(5)
            case "A":
                os.setCost((int(baseCost) * int(rankMult[4])))
                os.setSMod(13)
                os.setLMod(7)
                os.setUMod(13)
                os.setLoadout(5)
            case "S":
                os.setCost((int(baseCost) * int(rankMult[5])))
                os.setSMod(18)
                os.setLMod(10)
                os.setUMod(17)
                os.setLoadout(6)
    elif osClicked.get() == osOptions[2]:
        baseCost = 15
        match rank:
            case "E":
                os.setCost((int(baseCost) * int(rankMult[0])))
                os.setSMod(1)
                os.setLMod(2)
                os.setUMod(1)
                os.setLoadout(3)
            case "D":
                os.setCost((int(baseCost) * int(rankMult[1])))
                os.setSMod(3)
                os.setLMod(3)
                os.setUMod(3)
                os.setLoadout(4)
            case "C":
                os.setCost((int(baseCost) * int(rankMult[2])))
                os.setSMod(5)
                os.setLMod(5)
                os.setUMod(6)
                os.setLoadout(4)
            case "B":
                os.setCost((int(baseCost) * int(rankMult[3])))
                os.setSMod(7)
                os.setLMod(8)
                os.setUMod(9)
                os.setLoadout(5)
            case "A":
                os.setCost((int(baseCost) * int(rankMult[4])))
                os.setSMod(10)
                os.setLMod(11)
                os.setUMod(13)
                os.setLoadout(5)
            case "S":
                os.setCost((int(baseCost) * int(rankMult[5])))
                os.setSMod(13)
                os.setLMod(15)
                os.setUMod(17)
                os.setLoadout(6)
    elif osClicked.get() == osOptions[3]:
        baseCost = 15
        match rank:
            case "E":
                os.setCost((int(baseCost) * int(rankMult[0])))
                os.setSMod(0)
                os.setLMod(2)
                os.setUMod(2)
                os.setLoadout(3)
            case "D":
                os.setCost((int(baseCost) * int(rankMult[1])))
                os.setSMod(2)
                os.setLMod(4)
                os.setUMod(3)
                os.setLoadout(4)
            case "C":
                os.setCost((int(baseCost) * int(rankMult[2])))
                os.setSMod(4)
                os.setLMod(7)
                os.setUMod(5)
                os.setLoadout(4)
            case "B":
                os.setCost((int(baseCost) * int(rankMult[3])))
                os.setSMod(6)
                os.setLMod(11)
                os.setUMod(7)
                os.setLoadout(5)
            case "A":
                os.setCost((int(baseCost) * int(rankMult[4])))
                os.setSMod(8)
                os.setLMod(15)
                os.setUMod(11)
                os.setLoadout(5)
            case "S":
                os.setCost((int(baseCost) * int(rankMult[5])))
                os.setSMod(10)
                os.setLMod(20)
                os.setUMod(15)
                os.setLoadout(6)
    elif osClicked.get() == osOptions[4]:
        baseCost = 20
        match rank:
            case "E":
                os.setCost((int(baseCost) * int(rankMult[0])))
                os.setSMod(0)
                os.setLMod(4)
                os.setUMod(1)
                os.setLoadout(3)
            case "D":
                os.setCost((int(baseCost) * int(rankMult[1])))
                os.setSMod(1)
                os.setLMod(7)
                os.setUMod(2)
                os.setLoadout(4)
            case "C":
                os.setCost((int(baseCost) * int(rankMult[2])))
                os.setSMod(3)
                os.setLMod(11)
                os.setUMod(4)
                os.setLoadout(4)
            case "B":
                os.setCost((int(baseCost) * int(rankMult[3])))
                os.setSMod(5)
                os.setLMod(15)
                os.setUMod(6)
                os.setLoadout(5)
            case "A":
                os.setCost((int(baseCost) * int(rankMult[4])))
                os.setSMod(7)
                os.setLMod(20)
                os.setUMod(10)
                os.setLoadout(5)
            case "S":
                os.setCost((int(baseCost) * int(rankMult[5])))
                os.setSMod(9)
                os.setLMod(25)
                os.setUMod(14)
                os.setLoadout(6)
    elif osClicked.get() == osOptions[5]:
        baseCost = 30
        match rank:
            case "E":
                os.setCost((int(0) * int(baseCost) * int(rankMult[0])))
                os.setSMod(0)
                os.setLMod(0)
                os.setUMod(0)
                os.setLoadout(0)
            case "D":
                os.setCost((int(baseCost) * int(rankMult[1])))
                os.setSMod(3)
                os.setLMod(3)
                os.setUMod(5)
                os.setLoadout(4)
            case "C":
                os.setCost((int(baseCost) * int(rankMult[2])))
                os.setSMod(6)
                os.setLMod(6)
                os.setUMod(8)
                os.setLoadout(5)
            case "B":
                os.setCost((int(baseCost) * int(rankMult[3])))
                os.setSMod(9)
                os.setLMod(9)
                os.setUMod(11)
                os.setLoadout(6)
            case "A":
                os.setCost((int(baseCost) * int(rankMult[4])))
                os.setSMod(13)
                os.setLMod(13)
                os.setUMod(16)
                os.setLoadout(7)
            case "S":
                os.setCost((int(baseCost) * int(rankMult[5])))
                os.setSMod(17)
                os.setLMod(17)
                os.setUMod(21)
                os.setLoadout(8)
    elif osClicked.get() == osOptions[6]:
        baseCost = 30
        match rank:
            case "E":
                os.setCost((int(0) * int(baseCost) * int(rankMult[0])))
                os.setSMod(0)
                os.setLMod(0)
                os.setUMod(0)
                os.setLoadout(0)
            case "D":
                os.setCost((int(baseCost) * int(rankMult[1])))
                os.setSMod(7)
                os.setLMod(2)
                os.setUMod(3)
                os.setLoadout(4)
            case "C":
                os.setCost((int(baseCost) * int(rankMult[2])))
                os.setSMod(10)
                os.setLMod(4)
                os.setUMod(7)
                os.setLoadout(5)
            case "B":
                os.setCost((int(baseCost) * int(rankMult[3])))
                os.setSMod(14)
                os.setLMod(6)
                os.setUMod(10)
                os.setLoadout(6)
            case "A":
                os.setCost((int(baseCost) * int(rankMult[4])))
                os.setSMod(19)
                os.setLMod(8)
                os.setUMod(15)
                os.setLoadout(7)
            case "S":
                os.setCost((int(baseCost) * int(rankMult[5])))
                os.setSMod(25)
                os.setLMod(10)
                os.setUMod(20)
                os.setLoadout(8)
    elif osClicked.get() == osOptions[7]:
        baseCost = 30
        match rank:
            case "E":
                os.setCost((int(0) * int(baseCost) * int(rankMult[0])))
                os.setSMod(0)
                os.setLMod(0)
                os.setUMod(0)
                os.setLoadout(0)
            case "D":
                os.setCost((int(baseCost) * int(rankMult[1])))
                os.setSMod(2)
                os.setLMod(7)
                os.setUMod(3)
                os.setLoadout(4)
            case "C":
                os.setCost((int(baseCost) * int(rankMult[2])))
                os.setSMod(4)
                os.setLMod(10)
                os.setUMod(7)
                os.setLoadout(5)
            case "B":
                os.setCost((int(baseCost) * int(rankMult[3])))
                os.setSMod(6)
                os.setLMod(14)
                os.setUMod(10)
                os.setLoadout(6)
            case "A":
                os.setCost((int(baseCost) * int(rankMult[4])))
                os.setSMod(8)
                os.setLMod(19)
                os.setUMod(15)
                os.setLoadout(7)
            case "S":
                os.setCost((int(baseCost) * int(rankMult[5])))
                os.setSMod(10)
                os.setLMod(25)
                os.setUMod(15)
                os.setLoadout(8)
    elif osClicked.get() == osOptions[8] and typeClicked.get() == "MA" or osClicked.get() == osOptions[
        8] and typeClicked.get() == "Ship":
        baseCost = 30
        match rank:
            case "E":
                os.setCost((int(baseCost) * int(rankMult[0])))
                os.setSMod(0)
                os.setLMod(4)
                os.setUMod(2)
                os.setLoadout(3)
            case "D":
                os.setCost((int(baseCost) * int(rankMult[1])))
                os.setSMod(2)
                os.setLMod(7)
                os.setUMod(4)
                os.setLoadout(4)
            case "C":
                os.setCost((int(baseCost) * int(rankMult[2])))
                os.setSMod(4)
                os.setLMod(12)
                os.setUMod(7)
                os.setLoadout(5)
            case "B":
                os.setCost((int(baseCost) * int(rankMult[3])))
                os.setSMod(6)
                os.setLMod(17)
                os.setUMod(10)
                os.setLoadout(6)
            case "A":
                os.setCost((int(baseCost) * int(rankMult[4])))
                os.setSMod(8)
                os.setLMod(22)
                os.setUMod(16)
                os.setLoadout(7)
            case "S":
                os.setCost((int(baseCost) * int(rankMult[5])))
                os.setSMod(10)
                os.setLMod(28)
                os.setUMod(22)
                os.setLoadout(8)
    elif osClicked.get() == osOptions[9] and typeClicked.get() == "Ship":
        baseCost = 0
        modifier = 40
        match rank:
            case "E":
                os.setCost((int(0) * int(baseCost) * int(rankMult[0])))
                os.setSMod(0)
                os.setLMod(0)
                os.setUMod(0)
                os.setLoadout(0)
            case "D":
                os.setCost((int(baseCost) * int(rankMult[1])) - int(modifier))
                os.setSMod(2)
                os.setLMod(8)
                os.setUMod(6)
                os.setLoadout(5)
            case "C":
                os.setCost((int(baseCost) * int(rankMult[2])) - int(modifier))
                os.setSMod(4)
                os.setLMod(12)
                os.setUMod(10)
                os.setLoadout(6)
            case "B":
                os.setCost((int(baseCost) * int(rankMult[3])) - int(modifier))
                os.setSMod(6)
                os.setLMod(16)
                os.setUMod(14)
                os.setLoadout(7)
            case "A":
                os.setCost((int(baseCost) * int(rankMult[4])) - int(modifier))
                os.setSMod(9)
                os.setLMod(21)
                os.setUMod(19)
                os.setLoadout(8)
            case "S":
                os.setCost((int(baseCost) * int(rankMult[5])) - int(modifier))
                os.setSMod(12)
                os.setLMod(26)
                os.setUMod(24)
                os.setLoadout(9)
    elif osClicked.get() == osOptions[10]:
        baseCost = 5
        smE.config(state=NORMAL)
        lmE.config(state=NORMAL)
        umE.config(state=NORMAL)
        slotUpdate.config(state=NORMAL)

        match rank:
            case "E":
                maxVar.set(maxOptions[1])
                os.setSMod(0)
                os.setLMod(0)
                os.setUMod(0)
                os.setCost((int(baseCost) * int(maxOptions[1])))
                os.setLoadout(int(2) + math.floor(int(os.getCost()) / 30))
                maxText.set("Max Slots: " + str(maxOptions[1]))
            case "D":
                maxVar.set(maxOptions[2])
                os.setSMod(0)
                os.setLMod(0)
                os.setUMod(0)
                os.setCost((int(baseCost) * int(maxOptions[2])))
                os.setLoadout(int(2) + math.floor(int(os.getCost()) / 30))
                maxText.set("Max Slots: " + str(maxOptions[2]))
            case "C":
                maxVar.set(maxOptions[3])
                os.setSMod(0)
                os.setLMod(0)
                os.setUMod(0)
                os.setCost((int(baseCost) * int(maxOptions[3])))
                os.setLoadout(int(2) + math.floor(int(os.getCost()) / 30))
                maxText.set("Max Slots: " + str(maxOptions[3]))
            case "B":
                maxVar.set(maxOptions[4])
                os.setSMod(0)
                os.setLMod(0)
                os.setUMod(0)
                os.setCost((int(baseCost) * int(maxOptions[4])))
                os.setLoadout(int(2) + math.floor(int(os.getCost()) / 30))
                maxText.set("Max Slots: " + str(maxOptions[4]))
            case "A":
                maxVar.set(maxOptions[5])
                os.setSMod(0)
                os.setLMod(0)
                os.setUMod(0)
                os.setCost((int(baseCost) * int(maxOptions[5])))
                os.setLoadout(int(2) + math.floor(int(os.getCost()) / 30))
                maxText.set("Max Slots: " + str(maxOptions[5]))
            case "S":
                maxVar.set(maxOptions[6])
                os.setSMod(0)
                os.setLMod(0)
                os.setUMod(0)
                os.setCost((int(baseCost) * int(maxOptions[6])))
                os.setLoadout(int(2) + math.floor(int(os.getCost()) / 30))
                maxText.set("Max Slots: " + str(maxOptions[6]))
    else:
        os.setSMod(0)
        os.setLMod(0)
        os.setUMod(0)
        os.setCost(int(0))
        os.setLoadout(int(0))

    if osClicked.get() != osOptions[10]:
        maxText.set("Max Slots: " + str(int(os.getSMod()) + int(os.getLMod()) + int(os.getUMod())))

    smEText.set(str(os.getSMod()))
    lmEText.set(str(os.getLMod()))
    umEText.set(str(os.getUMod()))
    loadoutEText.set(str(os.getLoadout()))

    updateCost()


def updateSlots(sm, lm, um):
    if (int(sm) + int(lm) + int(um)) != int(maxVar.get()):
        if (int(sm) + int(lm) + int(um)) < int(maxVar.get()):
            messagebox.showerror("Invalid slot allocation", "Not enough slots allocated", parent=root)
        else:
            messagebox.showerror("Invalid slot allocation", "Too many slots allocated", parent=root)
    else:
        messagebox.showinfo("Success!", "Slots Updated Successfully", parent=root)
        os.setSMod(sm)
        os.setLMod(lm)
        os.setUMod(um)


def openMods():
    modButton.config(state=DISABLED)
    rankDrop.config(state=DISABLED)
    terrainDrop.config(state=DISABLED)
    slotUpdate.config(state=DISABLED)
    smE.config(state=DISABLED)
    lmE.config(state=DISABLED)
    umE.config(state=DISABLED)
    typeDrop.config(state=DISABLED)
    osDrop.config(state=DISABLED)
    nameE.config(state=DISABLED)
    global modSelect
    global mods
    mods = Toplevel(root)

    excludeList = []

    if len(modSelect) > 0:
        for mm in range(0, len(mModList)):
            count2 = 0
            for m in range(0, len(modSelect)):
                if modSelect[m].getName() == mModList[mm].getName() and str(modSelect[m].getLevel()) != mModList[mm].getLevel():
                        if count2 >= 1:
                            tempMod = Mod.Mod()
                            tempMod.setName(modSelect[m].getName())
                            tempMod.setLevel(0)
                            excludeList.append(tempMod)
                            print(tempMod.getName() + " " + str(tempMod.getLevel()))
                elif modSelect[m].getName() == mModList[mm].getName() and str(modSelect[m].getLevel()) == mModList[mm].getLevel():
                    count2 = count2 + 1
                    tempMod = Mod.Mod()
                    tempMod.setName(mModList[mm].getName())
                    tempMod.setLevel(mModList[mm].getLevel())
                    excludeList.append(tempMod)
                    print(tempMod.getName() + " " + str(tempMod.getLevel()))

    mods.title("Modifications")
    w = 1650
    h = 650
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)

    mods.geometry('%dx%d+%d+%d' % (w, h, x, y))

    columns = ("Name", "Cost", "Description", "Level", "ShortMod", "LongMod", "UtilityMod", "Effect")
    modTree = ttk.Treeview(mods, columns=columns, show="headings", selectmode="extended", height=5)
    modTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    modTree.heading("Cost", text="Cost", anchor=tkinter.CENTER)
    modTree.heading("Description", text="Description", anchor=tkinter.CENTER)
    modTree.heading("Level", text="Level", anchor=tkinter.CENTER)
    modTree.heading("ShortMod", text="Short Mod", anchor=tkinter.CENTER)
    modTree.heading("LongMod", text="Long Mod", anchor=tkinter.CENTER)
    modTree.heading("UtilityMod", text="Utility Mod", anchor=tkinter.CENTER)
    modTree.heading("Effect", text="Effect", anchor=tkinter.CENTER)
    s = ttk.Style()
    s.configure('Treeview', rowheight=100)

    for mod in mModList:
        count3 = 0
        for e in excludeList:
            if e.getName() == mod.getName() and e.getLevel() == mod.getLevel():
                count3 = count3 + 1
                continue
            elif e.getName() == mod.getName() and e.getLevel() == 0:
                count3 = count3 + 1
                continue
        if count3 == 0:
            modTree.insert("", tkinter.END, values=(
            mod.getName(), mod.getCost(), wrap(str(mod.getDescription())), mod.getLevel(), mod.getSM(), mod.getLM(),
            mod.getUM(), mod.getEffect()))

    modTree.pack(side="left", fill="both")

    modTree.column("Name", minwidth=250, width=250, stretch=False)
    modTree.column("Cost", minwidth=50, width=50, stretch=False)
    modTree.column("Description", minwidth=750, width=750, stretch=False)
    modTree.column("Level", minwidth=75, width=75, stretch=False)
    modTree.column("ShortMod", minwidth=75, width=75, stretch=False)
    modTree.column("LongMod", minwidth=75, width=75, stretch=False)
    modTree.column("UtilityMod", minwidth=75, width=75, stretch=False)
    modTree.column("Effect", minwidth=150, width=150, stretch=False)

    scrollbar = ttk.Scrollbar(mods, orient=tkinter.VERTICAL, command=modTree.yview)
    modTree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y", expand=False)

    def handle_click(event):
        if modTree.identify_region(event.x, event.y) == "separator":
            return "break"

    def addModEvent(event):
        global modSelect
        item = Mod.Mod()
        for selected_item in modTree.selection():
            item.setName(modTree.item(selected_item)['values'][0])
            item.setCost(modTree.item(selected_item)['values'][1])
            item.setDescription(str(modTree.item(selected_item)['values'][2]))
            item.setLevel(modTree.item(selected_item)['values'][3])
            item.setSM(modTree.item(selected_item)['values'][4])
            item.setLM(modTree.item(selected_item)['values'][5])
            item.setUM(modTree.item(selected_item)['values'][6])
            item.setEffect(modTree.item(selected_item)['values'][7])
            addMod(item)
        closeMod()

    modTree.bind('<Double-1>', addModEvent)
    modTree.bind('<Button-1>', handle_click)

    mods.protocol("WM_DELETE_WINDOW", closeMod)


def addMod(item):
    modSelect.append(item)


def closeMod():
    if typeClicked.get() != "None":
        modButton.config(state=NORMAL)
        rankDrop.config(state=NORMAL)
        terrainDrop.config(state=NORMAL)
        typeDrop.config(state=NORMAL)
        osDrop.config(state=NORMAL)
        nameE.config(state=NORMAL)
    else:
        rankDrop.config(state=DISABLED)
        terrainDrop.config(state=DISABLED)
        slotUpdate.config(state=DISABLED)
        modButton.config(state=DISABLED)
        typeDrop.config(state=NORMAL)
        osDrop.config(state=DISABLED)
        nameE.config(state=NORMAL)

    if osClicked.get() == osOptions[10]:
        slotUpdate.config(state=NORMAL)
        smE.config(state=NORMAL)
        lmE.config(state=NORMAL)
        umE.config(state=NORMAL)

    global mods
    mods.destroy()


root.title("Mobile Suit Gundam Nexus Character Builder")

w = 850
h = 400
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

x = (sw / 2) - (w / 2)
y = (sh / 2) - (h / 2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

icon = tkinter.PhotoImage(file='ico.png')
root.wm_iconphoto(False, icon)
nameLabel = Label(root, text="Mech Name:")
nameE = Entry(root, width=50)
nameE.insert(0, "Enter Mecha Name")
nameLabel.grid(row=0, column=0)
nameE.grid(row=0, column=1)

costText = StringVar()
costText.set("Cost: " + str(0))

costLabel = Label(root, textvariable=costText)

costLabel.grid(row=0, column=2)

rankMult = [
    1,
    2,
    3,
    4,
    5,
    6,
]
typeOptions = [
    "None",
    "MS",
    "MA",
    "Ship",
]

typeClicked = StringVar()
typeClicked.set(typeOptions[0])
typeClicked.trace('w', typeSelect)

rankOptions = [
    "E",
    "D",
    "C",
    "B",
    "A",
    "S",
]

rankClicked = StringVar()
rankClicked.set(rankOptions[0])
rankClicked.trace('w', rankSelect)

orankOptions = [
    "E",
    "D",
    "C",
    "B",
    "A",
    "S",
]

orankClicked = StringVar()
orankClicked.set(orankOptions[0])
orankClicked.trace('w', orankSelect)

terrainOptions = [
    "Ground",
    "Flight",
    "Space",
    "Water",
    "Ground+",
    "Flight+",
    "Space+",
    "Water+",
]

terrainClicked = StringVar()
terrainClicked.set(terrainOptions[0])
terrainClicked.trace('w', terrainSelect)

terrainLabel = Label(root, text="Terrain:")
terrainDrop = OptionMenu(root, terrainClicked, *terrainOptions, command=lambda x=None: terrainSelect)
terrainDrop.config(state=DISABLED)
osOptions = [
    "General Purpose OS",
    "General Assault OS",
    "Multi-Purpose OS",
    "Ranged Combat OS",
    "Long Range Support OS",
    "Multi-Purpose Custom OS",
    "Assault Custom OS",
    "Long Range Custom OS",
    "Mobile Armor OS",
    "Mothership OS",
    "Original OS",
]

osClicked = StringVar()
osClicked.set(osOptions[0])
osClicked.trace('w', osSelect)

orankClicked = StringVar()
orankClicked.set(orankOptions[0])
orankClicked.trace('w', orankSelect)

osLabel = Label(root, text="OS:")
osDrop = OptionMenu(root, osClicked, *osOptions, command=lambda x=None: osSelect)
osDrop.config(state=DISABLED)

smText = StringVar()
smText.set("Short Mod Remaining: ")
smLabel = Label(root, textvariable=smText)
smEText = StringVar()
smEText.set(str(os.getSMod()))
smE = Entry(root, width=10, state=DISABLED, textvariable=smEText)

lmText = StringVar()
lmText.set("Long Mod Remaining: ")
lmLabel = Label(root, textvariable=lmText)
lmEText = StringVar()
lmEText.set(str(os.getLMod()))
lmE = Entry(root, width=10, state=DISABLED, textvariable=lmEText)

umText = StringVar()
umText.set("Utility Mod Remaining: ")
umLabel = Label(root, textvariable=umText)
umEText = StringVar()
umEText.set(str(os.getUMod()))
umE = Entry(root, width=10, state=DISABLED, textvariable=umEText)

loadoutText = StringVar()
loadoutText.set("Loadout Limit Remaining: ")
loadoutLabel = Label(root, textvariable=loadoutText)
loadoutEText = StringVar()
loadoutEText.set(str(os.getLoadout()))
loadoutE = Entry(root, width=10, state=DISABLED, textvariable=loadoutEText)

typeLabel = Label(root, text="Mech Type:")
typeDrop = OptionMenu(root, typeClicked, *typeOptions, command=lambda x=None: typeSelect)
typeLabel.grid(row=1, column=0)
typeDrop.grid(row=1, column=1)

statText = StringVar()
statText.set("Pilot Stat Limit: " + str(mech.getsLimit()))
statLabel = Label(root, textvariable=statText)

costMText = StringVar()
costMText.set("Cost: " + str(mech.getCost()))
costLabel = Label(root, textvariable=costMText)

statHeaderLabel1 = Label(root, text="STAT")
statHeaderLabel2 = Label(root, text="STAT")

hpText = StringVar()
hpText.set("HP: " + str(mech.getHP()))
hpLabel = Label(root, textvariable=hpText)

acText = StringVar()
acText.set("AC: " + str(mech.getAC()))
acLabel = Label(root, textvariable=acText)

agText = StringVar()
agText.set("AG: " + str(mech.getAG()))
agLabel = Label(root, textvariable=agText)

moveText = StringVar()
moveText.set("Move: " + str(mech.getMove()))
moveLabel = Label(root, textvariable=moveText)

enText = StringVar()
enText.set("EN: " + str(mech.getEN()))
enLabel = Label(root, textvariable=enText)

ecText = StringVar()
ecText.set("EC: " + str(mech.getEC()))
ecLabel = Label(root, textvariable=ecText)

sizeText = StringVar()
sizeText.set("Unit Size: " + str(mech.getSize()))
sizeLabel = Label(root, textvariable=sizeText)
sizeLabel.grid(row=7, column=1)

dmText = StringVar()
dmText.set("DM: " + str(mech.getDM()))
dmLabel = Label(root, textvariable=dmText)

carryText = StringVar()
carryText.set("Carry Limit: " + str(mech.getCarry()))
carryLabel = Label(root, textvariable=carryText)
carryLabel.grid(row=8, column=0)

spText = StringVar()
spText.set("SP: " + str(mech.getSP()))
spLabel = Label(root, textvariable=spText)
spLabel.grid(row=8, column=1)

statLabel.grid(row=2, column=0)

statLabel.grid(row=2, column=0)

costLabel.grid(row=2, column=1)

statHeaderLabel1.grid(row=3, column=0)
statHeaderLabel2.grid(row=3, column=1)

hpLabel.grid(row=4, column=0)

acLabel.grid(row=5, column=0)

agLabel.grid(row=6, column=0)

moveLabel.grid(row=7, column=0)

enLabel.grid(row=4, column=1)

ecLabel.grid(row=5, column=1)

dmLabel.grid(row=6, column=1)
maxOptions = [
    0,
    6,
    10,
    17,
    26,
    37,
    50,

]

maxVar = StringVar()
maxVar.set(maxOptions[0])

maxText = StringVar()
maxText.set("Max Slots: " + str(int(os.getSMod()) + int(os.getLMod()) + int(os.getUMod())))

maxLabel = Label(root, textvariable=maxText)
maxLabel.grid(row=9, column=2)
slotUpdate = Button(text="Update Slots",
                    command=lambda x=int(smE.get()), y=int(lmE.get()), z=int(umE.get()): updateSlots(smE.get(),
                                                                                                     lmE.get(),
                                                                                                     umE.get()),
                    state=DISABLED)
slotUpdate.grid(row=9, column=3)

rankLabel = Label(root, text="Rank:")
rankDrop = OptionMenu(root, rankClicked, *rankOptions, command=lambda x=None: rankSelect)
rankLabel2 = Label(root, text="Rank:")
rankDrop2 = OptionMenu(root, orankClicked, *orankOptions, command=lambda x=None: orankSelect)
rankDrop.config(state=DISABLED)
rankDrop2.config(state=DISABLED)

rankLabel.grid(row=1, column=2)
rankDrop.grid(row=1, column=3)
terrainLabel.grid(row=2, column=2)
terrainDrop.grid(row=2, column=3)
osLabel.grid(row=3, column=2)
osDrop.grid(row=3, column=3)
rankLabel2.grid(row=4, column=2)
rankDrop2.grid(row=4, column=3)
smLabel.grid(row=5, column=2)
smE.grid(row=5, column=3)
lmLabel.grid(row=6, column=2)
lmE.grid(row=6, column=3)
umLabel.grid(row=7, column=2)
umE.grid(row=7, column=3)
loadoutLabel.grid(row=8, column=2)
loadoutE.grid(row=8, column=3)

modButton = Button(root, text="Add New Modification", command=openMods)
modButton.config(state=DISABLED)
modButton.grid(row=9, column=0)

root.mainloop()
