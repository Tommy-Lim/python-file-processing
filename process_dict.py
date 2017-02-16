from collections import defaultdict

filename = "twl3.txt"

def longest_word(filename):
    text_file = open(filename)
    long_word = None
    for line in text_file.readlines():
      line = line.strip()
      if long_word is None:
          long_word = line
          print(f"new long word '{long_word}' with count {len(long_word)}")
      elif len(line) >= len(long_word):
          long_word = line
          print(f"new long word '{long_word}' with count {len(long_word)}")
    print(f"Longest word is {long_word} with length {len(long_word)}")

def letter_distribution(filename):
    text_file = open(filename)
    letter_count = defaultdict(int)
    for letter in text_file.read():
        letter = letter.strip()
        letter_count[letter] +=1
    max_value = None
    max_key = None
    for k,v in letter_count.items():
        if max_key is None:
            max_key = k
            max_value = v
            print(f"new highest count '{max_key}' with count {max_value}")
        elif v >= max_value:
            max_value = v
            max_key = k
            print(f"new highest count '{max_key}' with count {max_value}")
    print(f"Most used letter is {max_key} with count {max_value}")

def string_distribution(filename):
    text_file = open(filename)
    word_count = defaultdict(list)
    for word in text_file.readlines():
        word = word.strip()
        word = ''.join(sorted(word))
        word_count[word].append(word)
    max_value = None
    max_key = None
    for k,v in word_count.items():
        if max_key is None:
            max_key = k
            max_value = len(v)
            print(f"{max_key}: {max_value}")
        elif len(v) >= max_value:
            max_value = len(v)
            max_key = k
            print(f"{max_key}: {max_value}")
    print(f"Most used string is '{max_key}' with count {max_value}")






longest_word(filename)
print()
letter_distribution(filename)
print()
string_distribution(filename)
