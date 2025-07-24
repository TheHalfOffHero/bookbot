from stats import get_num_words, get_num_characters, sorted_list_of_dict

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

def main():
  file_contents = get_book_text("./books/frankenstein.txt")
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  get_num_words(file_contents)
  print("--------- Character Count -------")
  
  
  char_dict = get_num_characters(file_contents)
  sorted_list = sorted_list_of_dict(char_dict)
  
  for dict in sorted_list:
    print(f"{dict["char"]}: {dict["num"]}")
  
  print("============= END ===============")
  

main()