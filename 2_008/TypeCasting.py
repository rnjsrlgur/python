var = ''
print(var)
print(type(var)) # str

var = bool(var)
print(var) # False
print(type(var)) # boolean

# 공백문자 -> 논리
var = ' '
print(var)
print(type(var)) # str

var = bool(var)
print(var) # True
print(type(var)) # boolean