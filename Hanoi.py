import timeit
from Stack import Stack

def Hanoi_rec(n, s, a, d):
  # Base case, 1 disc left and gets moved to destination
  if n == 0:
    d.push(s.pop())
  else:
  # Recursive case, we need to move things around still
    Hanoi_rec(n-1, s, a, d)
    d.push(s.pop())
    Hanoi_rec(n-1, a, d, s)
  print(n, s, a, d)
  print()
def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == "__main__":
  n=1
  runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
  print("computed Hanoi(" + str(n) + ") in " + str(runtime) + " seconds.")
