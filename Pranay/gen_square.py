
# This method is the simplest but it creates new variable x(or even overwrites existing x)
def square():
  list = []
  for x in range(20):
    list.append(x**2)
  return list

# This method is much more handy using lambda, but requires deep understanding of it
def squareViaLambda():
  arr = list(map(lambda x: x**2,range(10)))
  return arr

# This is much more simpler, and also disposes off variable once loop finishes
def squareViaPrivateClosure():
  arr = [x**2 for x in range(10)]
  return arr

arrViaSquare = square()
arrViaLambda = squareViaLambda()
arrViaPrivateClosure = squareViaPrivateClosure()


print(arrViaSquare)
print(arrViaLambda)
print(arrViaPrivateClosure)
