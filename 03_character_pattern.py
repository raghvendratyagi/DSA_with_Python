'''
ABCD
ABCD
ABCD
ABCD
'''
n=int(input())
i=1
while i<=n:
  j=1
  while j<=n:
    charp= chr(ord('A')+j-1)
    print(charp,end=" ")
    j=j+1
  print()
  i=i+1



'''
ABCD
BCDE
CDEF
DEFG
'''

n=int(input())
i=1
while i<=n:
  start=chr(ord('A')+i-1)
  j=1
  while j<=n:
    charp= chr(ord(start)+j-1)
    print(charp,end=" ")
    j=j+1
  print()
  i=i+1











'''
A A A A 
B B B B
C C C C
D D D D
'''

n=int(input())
i=1
while i<=n:
  j=1
  while j<=n:
    charp= chr(ord('A')+i-1)
    print(charp,end=" ")
    j=j+1
  print()
  i=i+1
