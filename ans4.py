def swapKeysAndValues(dict):
  return {value: key for key, value in dict.items()}
dict = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3",
  "key4": "value4",
  "key5": "value5"
}

newDict = swapKeysAndValues(dict)

print(newDict)
