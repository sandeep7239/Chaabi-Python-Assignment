def f(list, low, high):
  if low < 0:
    low = 0
  if high > len(list) - 1:
    high = len(list) - 1
  result = []
  for i in range(low, high + 1, 2):
    result.append(list[i])
  return result
if __name__ == "__main__":
  list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
  low = 2
  high = 9

  result = f(list, low, high)

  print("Result of the given input is :", result)
