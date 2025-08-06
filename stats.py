def get_words_number(text):
  return len(text.split())

def get_characters_number(text):
  result = {}
  for char in text:
    if char.isalpha():
      char = char.lower()
      if char in result:
        result[char] += 1
      else:
        result[char] = 1
  return result

def get_sorted_characters_count(char_count):
  return sorted(char_count.items(), key=lambda item: item[1], reverse=True)
