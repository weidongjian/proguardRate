# coding=utf-8
# This is a sample Python script.

# 混淆的标识符
FILTER_SYMBOL = " -> "
SYMBOL_LENGTH = len(FILTER_SYMBOL)


def calculateProguardRate(filePath):
    file = open(filePath)
    lines = file.readlines()
    length = len(lines)
    # print("mapping.txt 总的行数是 :" + str(length))

    # 方法跟变量的总的数量
    methodTotal = 0
    # 方法跟变量已混淆的数量
    methodProguard = 0

    for index in range(0, len(lines)):
        lineString = lines[index]
        symbolIndex = lineString.find(FILTER_SYMBOL)
        if symbolIndex >= 0:  # 代表有混淆标识
            firstPart = lineString[0:symbolIndex]
            firstPart = removeEndSymbol(firstPart)
            secondPart = lineString[symbolIndex + SYMBOL_LENGTH:]
            secondPart = removeLineBreak(secondPart)

            sameEnd = firstPart.endswith(secondPart)
            methodTotal = methodTotal + 1
            # print "same end:" + str(sameEnd) + "，first:" + firstPart + "，second:" + secondPart + "，end"
            # 代表有混淆
            if not sameEnd:
                methodProguard = methodProguard + 1

    proguardRate = float(methodProguard) / methodTotal
    print("总的有效行数: " + str(methodTotal) + " 已混淆的行数 " + str(methodProguard) + " 混淆率 " + str(proguardRate))


# 移除方法后面的符号
def removeEndSymbol(str):
    newStr = str.strip()
    index = newStr.find('(')
    if index >= 0:
        # 代表是方法，移除括号后面的内容
        return newStr[0:index]
    else:
        return newStr


# 移除换行符
def removeLineBreak(str):
    return str.strip()


def cal_rate():
    mappingFile = input("请输入mapping文件地址：")
    # 方法开始的地方
    calculateProguardRate(mappingFile.strip())

def main():
    cal_rate()


if __name__ == "__main__":
    main()
