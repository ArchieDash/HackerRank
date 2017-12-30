for i in range(int(input("Number of test cases:"))):
  word = input("Word:")
  print (*[(word[::2]),"".join(word[1::2])])
