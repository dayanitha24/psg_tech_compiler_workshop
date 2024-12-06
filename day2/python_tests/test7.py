if __name__ == "__main__":
  strList = ["red", "blue", "green"]
  print("Items in list are")
  for s in strList:
      print(s)

  strList.append("black")
  print("\nAdd items to a list")
  for s in strList:
      print(s)

  strList[3] = "white"
  print("\nUpdate items to a list")
  for s in strList:
      print(s)

  strList.remove("white")
  print("\nRemove items from a list")
  for s in strList:
      print(s)