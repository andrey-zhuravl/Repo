import math


def strToInt(strArg):
    for sym in strArg:
        if isinstance(sym, str):
            sym = ord(sym)
        intArgOut = strArgOut + str(sym)

    return intArgOut


def tupToStr(tupArg):
    strArgOut = ''
    for sym in tupArg:
        if isinstance(sym, str):
            sym1 = ord(sym)
            sym = str(sym1)
        elif isinstance(sym, (int, float)):
            sym1 = int(sym)
            sym = str(sym1)
        strArgOut = strArgOut + sym
    return strArgOut


def numToStr(numArg):
    strArgOut = str(numArg)
    return strArgOut


def funMakeStrArg(strArgOut, lenHashOut):
    if len(strArgOut) < (lenHashOut * 5):
        while len(strArgOut) < (lenHashOut * 5):
            strArgOut = strArgOut + str(math.pi)[2:16]
        if len(strArgOut) > (lenHashOut * 5):
            strArgOut = strArgOut[0:lenHashOut * 5]
    return strArgOut


def makeHashOutFull(strArgOutFin):
    num = 0
    for i in range(len(strArgOutFin)):
        num = num + int(strArgOutFin[i])
        numCos = math.cos(num) + math.pi
        hashOut = int(str(numCos).partition('.')[2]) * 99999999999999999
    return hashOut


def cutHashOut(hashOut):
    if len(str(hashOut)) < lenHashOut:
        delta = lenHashOut - len(str(hashOut))
        numOutStr = str(hashOut) + str(numCos).partition('.')[2][:delta]
        hashOut = int(numOutStr)
    else:
        delta = len(str(hashOut)) - lenHashOut
        hashOut = str(hashOut)[delta:]
    return hashOut

def hashFunction(inData, lenHashOut):
    if isinstance(inData, (tuple, list)):
        strArgOut = tupToStr(inData)
    elif isinstance(inData, (int, float)):
        strArgOut = numToStr(inData)

    strArgOutFin = funMakeStrArg(strArgOut, lenHashOut)

    makeHashOutF = makeHashOutFull(strArgOutFin)
    hashOut = cutHashOut(makeHashOutF)


    print(' hashOut = ', hashOut)
    print(' len(hashOut) = ', len(str(hashOut)))

    return strArgOutFin


####################################

inData = (1, 2, 4.5, 4, 888, 234, 3.4444, 345345345)
lenHashOut = 16

hashFunction(inData, lenHashOut)