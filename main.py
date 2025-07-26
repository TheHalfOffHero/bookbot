from stats import get_num_words, get_num_characters, sorted_list_of_dict
import sys

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    book_filepath = sys.argv[1]
    
  file_contents = get_book_text(book_filepath)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_filepath}")
  print("----------- Word Count ----------")
  get_num_words(file_contents)
  print("--------- Character Count -------")
  
  
  char_dict = get_num_characters(file_contents)
  sorted_list = sorted_list_of_dict(char_dict)
  
  for dict in sorted_list:
    print(f"{dict["char"]}: {dict["num"]}")
  
  print("============= END ===============")
  

main()