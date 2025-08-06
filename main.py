import sys
from stats import get_words_number, get_characters_number, get_sorted_characters_count

def get_book_text(path):
  with open(path, 'r', encoding='utf-8') as file:
    return file.read()

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  book_text = get_book_text(book_path)
  char_count = get_characters_number(book_text)
  char_count_sorted = get_sorted_characters_count(char_count)
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {get_words_number(book_text)} total words")
  print("--------- Character Count -------")
  for char, count in char_count_sorted:
    print(f"{char}: {count}")


if __name__ == '__main__':
  main()
