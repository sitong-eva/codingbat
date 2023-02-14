def diff21(n):
  """
  Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
  """
  
  if n<= 21:
    if n-21>0:
      return n-21
    if n-21<0:
      return -(n-21)
    if n-21==0:
      return 0
  if n>21:
    if n-21>0:
      return (n-21)*2
    if n-21<0:
      return -(n-21)*2
    if n-21==0:
      return 0