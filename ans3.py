def f(dict_list, key):
  sorted_dict_list = sorted(dict_list, key=lambda x: x[key])


  return sorted_dict_list


if __name__ == "__main__":

  dict_list = [
    {
      "fruit": "orange",
      "color": "orange"
    },
    {
      "fruit": "apple",
      "color": "red"
    },
    {
      "fruit": "banana",
      "color": "yellow"
    },
    {
      "fruit": "blueberry",
      "color": "blue"
    }
  ]

  key = input("Enter the key to sort by: ")

  # Sort the list of dictionaries and print the result.
  sorted_dict_list = f(dict_list, key)
  print(sorted_dict_list)
