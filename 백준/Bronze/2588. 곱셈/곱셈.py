A = int(input())
B = list(input())

_01, _02, _03 = A*int(B[2]), A*int(B[1]), A*int(B[0])

print(_01)
print(_02)
print(_03)
print(_01 + _02*10 + _03*100)