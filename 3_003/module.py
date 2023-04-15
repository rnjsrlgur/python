def cmToMm(n):
    return round(n * 10, 2)

def cmToInch(n):
    return round(n * 0.393, 2)

def cmToM(n):
    return round(n * 0.01, 2)

def cmToFt(n):
    return round(n * 0.032, 2)

if __name__ == '__main__':
    print(f'10cm : {cmToMm(10)}')
    print(f'10inch : {cmToInch(10)}')
    print(f'10m : {cmToM(10)}')
    print(f'10ft : {cmToFt(10)}')