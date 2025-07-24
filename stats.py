def get_num_words(file_contents):
  string_array = file_contents.split()
  num_words = len(string_array)
  
  print(f"Found {num_words} total words")
  
def get_num_characters(file_contents):
  character_array = list(file_contents)
  
  character_dict = {}
  
  for character in character_array:
    char = character.lower()
    
    if char in character_dict:
      character_dict[char] = character_dict[char] + 1
    else:
      character_dict[char] = 1
  
  return character_dict

def sort_on(items):
  return items["num"]

def sorted_list_of_dict(character_dict):
  sorted_list_of_char_dicts = []
  
  for item in character_dict:
    if item.isalpha():
      sorted_list_of_char_dicts.append({
        "char": item,
        "num": character_dict[item]
      })
  sorted_list_of_char_dicts.sort(reverse=True, key=sort_on)
  
  return sorted_list_of_char_dicts