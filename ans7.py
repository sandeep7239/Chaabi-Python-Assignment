def factorial(n):
  factLambda = lambda n: n if n == 1 else n * factLambda(n - 1)
  return factLambda(n)
if __name__ == "__main__":
  n = 5
  factOfNum = factorial(n)
  print("The factorial of", n, "is", factOfNum)
