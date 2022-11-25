def summation(n):
  if n == 0:
    return 0
  return n + summation(n-1)
   
if __name__ == "__main__":
  print(summation(9))
