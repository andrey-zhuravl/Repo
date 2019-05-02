from PIL import Image, ImageDraw
import random


def funSimpleTriangleCreate():
    coordinates = (34, 375, 250, 0, 467, 375)
    varTriangle = Image.new('L', (500, 500), (0))
    drw = ImageDraw.Draw(varTriangle)
    drw.polygon(coordinates, outline=(255), fill=(255))
    return varTriangle


def funSimpleSquareCreate():
    coordinates = (250, 0, 500, 250, 250, 500, 0, 250)
    varSquare = Image.new('L', (500, 500), (0))
    drw = ImageDraw.Draw(varSquare)
    drw.polygon(coordinates, outline=(255), fill=(255))
    return varSquare


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
    varSimpleTriangleF = funSimpleTriangleCreate()
    varSimpleSquareF = funSimpleSquareCreate()

    varTriangleResizeF = funResizeImg(varSimpleTriangleF)
    varTriangleRotateF = funRotateImg(varTriangleResizeF[0])
    varPasteTriangleToBackgroundF = funPasteImgToBackground(varTriangleRotateF, varTriangleResizeF[1])

    varSquareResizeF = funResizeImg(varSimpleSquareF)
    varSquareRotateF = funRotateImg(varSquareResizeF[0])
    varPasteSquareToBackgroundF = funPasteImgToBackground(varSquareRotateF, varSquareResizeF[1])

    varTriangleToByteF = funToByte(varPasteTriangleToBackgroundF)
    trainImgArray = trainImgArray + varTriangleToByteF
    trainLabelArray = trainLabelArray + bytearray([111])

    varSquareToByteF = funToByte(varPasteSquareToBackgroundF)
    trainImgArray = trainImgArray + varSquareToByteF
    trainLabelArray = trainLabelArray + bytearray([222])

    funSaveBinFileModel(trainImgArray)
    funSaveBinFileLabel(trainLabelArray)


###############################################################################################

trainLabelF = bytearray()
trainImgF = bytearray()

open('FileTrainBinaryModel', "w").close()
open('FileTrainBinaryLabel', "w").close()

funCreationFullModel(trainImgF, trainLabelF)
