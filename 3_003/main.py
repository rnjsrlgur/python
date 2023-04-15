import module as m

if __name__ == "__main__":
    inputNum = int(input("Enter a number: "))

    returnVal = m.cmToMm(inputNum)
    print(f'inputNum : {inputNum}cm -> returnVal : {returnVal}mm')

    returnVal = m.cmToInch(inputNum)
    print(f'inputNum : {inputNum}cm -> returnVal : {returnVal}inch')

    returnVal = m.cmToM(inputNum)
    print(f'inputNum : {inputNum}cm -> returnVal : {returnVal}m')

    returnVal = m.cmToFt(inputNum)
    print(f'inputNum : {inputNum}cm -> returnVal : {returnVal}ft')