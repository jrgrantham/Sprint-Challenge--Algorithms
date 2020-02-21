#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

a)  a = 0                     O(1)
    while (a < n * n * n):    O(n^3 / n * n + ( ))
      a = a + n * n             O(1)

the while loop is based on n^3
'a' doubles with each loop.
no idea how the maths works.

O(n) is my best guess

b)

b)  sum = 0               O(1)
    for i in range(n):    O(n)
      j = 1                 O(1)
      while j < n:          O(log n)
        j *= 2              O(1)
        sum += 1            O(1)

O(n log n)

c)

c)  def bunnyEars(bunnies):
      if bunnies == 0:                     O(1)
        return 0                           O(1)

      return 2 + bunnyEars(bunnies-1)      O(n)

O(n)

## Exercise II

for a building with n floors, to find floor f:

while there are 2 remaining floors (to check between):
  drop egg at floor n / 2
    if egg breaks:
      save f as current floor
      ignore floors above and set n = all lower floors and repeat
    otherwise:
      set n = all higher floors and repeat

as doubling the number of floors would lead to a single further iteration, the runtime complexity is logrhythmic