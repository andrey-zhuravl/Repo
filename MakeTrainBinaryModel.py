from PIL import Image, ImageDraw
import numpy as np
import random


def funSimpleTriangleCreate():
    coordinates = (34, 375,
                   250, 0,
                   467, 375)
    varTriangle = Image.new('L', (500, 500), (0))
    drw = ImageDraw.Draw(varTriangle)
    drw.polygon(coordinates, outline=(255), fill=(255))
    return varTriangle


def funSimpleSquareCreate():
    coordinates = (250, 0,
                   500, 250,
                   250, 500,
                   0, 250)
    varSquare = Image.new('L', (500, 500), (0))
    drw = ImageDraw.Draw(varSquare)
    drw.polygon(coordinates, outline=(255), fill=(255))
    return varSquare


def funSimpleCircleCreate():
    coordinates = (0, 0,
                   500, 500)
    varCircle = Image.new('L', (500, 500), (0))
    drw = ImageDraw.Draw(varCircle)
    drw.ellipse(coordinates, outline=(255), fill=(255))
    return varCircle


def funSimpleCrossCreate():
    coordinates = (50, 200,
                   200, 200,
                   200, 50,
                   300, 50,
                   300, 200,
                   450, 200,
                   450, 300,
                   300, 300,
                   300, 450,
                   200, 450,
                   200, 300,
                   50, 300)
    varCross = Image.new('L', (500, 500), (0))
    drw = ImageDraw.Draw(varCross)
    drw.polygon(coordinates, outline=(255), fill=(255))
    return varCross


def funSimpleChordCreate():
    coordinates1 = (50, 50, 450, 450)
    varChord = Image.new('L', (500, 500), (0))
    drw = ImageDraw.Draw(varChord)
    drw.chord(coordinates1, 210, 0, fill=(255))
    return varChord


def funResizeImg(img):
    sideResize = random.randint(10, 500)
    varImgResize = img.resize((sideResize, sideResize))
    return (varImgResize, sideResize)


def funRotateImg(img):
    angle = random.randint(0, 360)
    varImgRotate = img.rotate(angle, expand=0)
    return varImgRotate


def funPasteImgToBackground(imgRotate, sideResize):
    x4 = random.randint(0, 500 - sideResize)
    y4 = random.randint(0, 500 - sideResize)
    varImgBlanc = Image.new('L', (500, 500), (0))
    varImgBlanc.paste(imgRotate, (x4, y4))
    return varImgBlanc


def funToByte(img):
    ByteModel = img.tobytes()
    return ByteModel


def funSaveBinFileModel(varToByte):
    with open(r'FileTrainBinaryModel', "ab") as fileModelOut:
        fileModelOut.write(varToByte)


def funSaveBinFileLabel(varToByte):
    with open(r'FileTrainBinaryLabel', "ab") as fileModelOut:
        fileModelOut.write(varToByte)


def funCreationFullModel(trainImgArray, trainLabelArray):
    arrayFigure = [0, 1, 2, 3, 4]
    varFigureNumber = np.random.choice(arrayFigure, p=[0.05, 0.45, 0.20, 0.20, 0.10])

    if varFigureNumber == 0:
        varImg = funSimpleTriangleCreate()
        trainLabelArray = trainLabelArray + bytearray([11])
    elif varFigureNumber == 1:
        varImg = funSimpleSquareCreate()
        trainLabelArray = trainLabelArray + bytearray([22])
    elif varFigureNumber == 2:
        varImg = funSimpleCircleCreate()
        trainLabelArray = trainLabelArray + bytearray([33])
    elif varFigureNumber == 3:
        varImg = funSimpleCrossCreate()
        trainLabelArray = trainLabelArray + bytearray([44])
    elif varFigureNumber == 4:
        varImg = funSimpleChordCreate()
        trainLabelArray = trainLabelArray + bytearray([55])

    varImgResizeF = funResizeImg(varImg)
    varImgRotateF = funRotateImg(varImgResizeF[0])
    varPasteImgToBackgroundF = funPasteImgToBackground(varImgRotateF, varImgResizeF[1])
    varImgToByteF = funToByte(varPasteImgToBackgroundF)
    trainImgArray = trainImgArray + varImgToByteF
 
    funSaveBinFileModel(trainImgArray)
    funSaveBinFileLabel(trainLabelArray)

###############################################################################################

trainLabelF = bytearray()
trainImgF = bytearray()

open('FileTrainBinaryModel', "w").close()
open('FileTrainBinaryLabel', "w").close()

funCreationFullModel(trainImgF, trainLabelF)
