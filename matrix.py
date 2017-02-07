import numpy as np

def shMatrix():
  return tuple(map(int, input().split()))

def enterMatrix(axis):
  try:
    return np.fromiter(map(int, input().split()), np.int).reshape(axis)
  except:
    print("n * m format")
    enterMatrix(axis)

def mulMatrix(x, y):
  try:
    return x.dot(y.T)
  except:
    printa("matrix shapes do not match")

X = enterMatrix(shMatrix())
Y = enterMatrix(shMatrix())

print(X)
print(Y.T)
print(mulMatrix(X, Y))




