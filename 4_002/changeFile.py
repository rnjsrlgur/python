f = open('C:/pythonEx/pythonTxt/aboutPython.txt', 'r', encoding='UTF8')

str = f.read()
print(f'str: {str}')

f.close()

str = str.replace('python', '파이썬', 2)
print(f'str: {str}')

f = open('C:/pythonEx/pythonTxt/aboutPython.txt', 'w', encoding='UTF8')
f.write(str)

f.close()