def makeNumberSquare(number):
    try:

        numberSqua = number ** 2
        return numberSqua
    except Exception as err:
        print(' функция makeNumSqua, ошибка = ', err)


def takeSymbol3to10(numSqua, lenNum):
    try:
        if len(str(numSqua)) < 4:
            symbol3to10 = int(str(numSqua))
        else:
            symbol3to10 = int(str(numSqua)[1:(lenNum)])
        return symbol3to10
    except Exception as err:
        print(' функция takeSymbol3to10, ошибка = ', err)


def makeSummSymbolAndSecond(symbol3to10, numberListSecond):
    try:
        summ = symbol3to10 + numberListSecond
        return summ
    except Exception as err:
        print(' функция makeSummSymbolAndSecond, ошибка = ', err)


def makeDivisionSummToThird(summ, numberListThird, lenNum):
    try:
        div = (summ / numberListThird) + 1
        if len(str(div)) < 4:
            div = int(str(div).replace('.', ''))
        else:
            div = int(str(div).replace('.', '')[1:(lenNum + 1)]) + 1
        return div
    except Exception as err:
        print(' функция divisionToThird, ошибка = ', err)


def makeSingleNumber(numberList):
    try:
        numSqua = makeNumberSquare(numberList[0])
        symbol3to10 = takeSymbol3to10(numSqua, len(str(numberList[0])))
        summSymbolAndSecond = makeSummSymbolAndSecond(symbol3to10, numberList[1])
        divisionSummToThird = makeDivisionSummToThird(summSymbolAndSecond, numberList[2], len(str(numberList[0])))
        return divisionSummToThird
    except Exception as err:
        print(' функция makeSingleNumber, ошибка = ', err)


def generateRandomSequence(sizeSequence, numberList):
    try:
        sequenceRandom = []
        sequenceRandomAddon = []

        for j in range(sizeSequence // 10):
            numberListAddon = [j ** 2, (j ** 2) + 3, (j ** 2) + 5]
            SingleNumberAddon = makeSingleNumber(numberListAddon)
            sequenceRandomAddon.append(SingleNumberAddon)
            print(' дополнительный массив - ', sequenceRandomAddon[j])

        for i in range(sizeSequence):
            SingleNumber = makeSingleNumber(numberList)

            numberList[0] = SingleNumber

            if SingleNumber in sequenceRandom:
                sequenceRandom.append(SingleNumber + 10)
            else:
                sequenceRandom.append(SingleNumber)

            if i % 5 == 0:
                numberList[1] = numberList[1] + 26
                numberList[2] = numberList[2] + 16

            if i % 10 == 0:
                k = i // 10
                numberList[1] = sequenceRandomAddon[k]
            print(sequenceRandom[i])

        return (sequenceRandom, len(sequenceRandom))

    except Exception as err:
        print(' функция generateRandomSequence, ошибка = ', err)


#############################################################


try:
    sizeSequence = 100
    numberList = [31, 23, 11]

    print('\n', ' последовательность получилась такая = ', generateRandomSequence(sizeSequence, numberList)[0], '\n',
          ' количество элементов в последовательности = ', generateRandomSequence(sizeSequence, numberList)[1])

except Exception as err:
    print(' функция MAIN, ошибка = ', err)
