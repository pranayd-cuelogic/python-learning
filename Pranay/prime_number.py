def GenPrime(x):
  for m in range(2, x):
    for n in range(2, m):
      if  m % n == 0:
        break
    else: 
      print(m, 'is a prime number')


GenPrime(100)
