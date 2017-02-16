filename = "twl3.txt"
file_ = open(filename)
long_word = None
for line in file_.readlines():
  line = line.strip()
  if long_word is None:
      long_word = line
      print(f"New long word is {long_word} with length {len(long_word)}")
  elif len(line)>len(long_word):
      long_word = line
      print(f"New long word is {long_word} with length {len(long_word)}")
print(long_word)
