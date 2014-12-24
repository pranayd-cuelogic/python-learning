from collections import deque
def dequeDemo():
  arr = deque([1,2,3,4])
  arr.append(5)
  arr.appendleft(6)
  arr.extend([11,123,12])
  arr.extendleft([99])
  return arr

arr = dequeDemo()

print list(arr)