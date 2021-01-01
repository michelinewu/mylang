# myLang
# a made-up language generator

# names of the languages:
NAME_NEW_LANG = "newlang"
NAME_ORIG_LANG = "origlang"

# this is a default set of words if the user does not want to start from scratch:
WORDS = {
  "truma": "for",
  "llamama": "your",
  "twenlyli": "to",
  "freenee": "and",
  "l1lol1": "I",
  "trickTrike": "bicycle",
  "lopsi": "multiple",
  "jiloj": "characters",
  "ikol": "happens",
  "kilsdan": "special",
  "prlioi": "house"
}

#
#   INTERNAL TASK FUNCTIONS
#

def set_up_dictionary():
  """Asks user if they would like to use language name and dictionary defaults and updates accordingly."""

  # since we're reassigning global variables
  global NAME_NEW_LANG
  global NAME_ORIG_LANG
  global WORDS

  # ask user if they'd like to use default language names or new language names
  language_name_request = "Would you like to use the default language names or name your languages? \n\n\tPlease enter: \n\n\t[Y] Use Default Names\n\t[N] Name Languages\n"

  if not yes_or_no(language_name_request):

    # reassign new language name
    NAME_NEW_LANG = input('\nWhat would you like to name your new language?\n> ')

    # beginning of reassignment original language
    orig_lang_input = input('\nWhat would you like to name your original language?\n> ')

    # in case the user inputs the same string as the new language name
    while orig_lang_input == NAME_NEW_LANG:
      orig_lang_input = input('\nPlease input a different language name than "{}".\n> '.format(NAME_NEW_LANG))

    NAME_ORIG_LANG = orig_lang_input
  
  # ask user if they'd like to use default word dictionary
  dictionary_request = "\nWould you like to use the default word dictionary?\n\n\tPlease enter: \n\n\t[Y] Use Default Dictionary\n\t[N] Use New Dictionary\n"

  # if using the default dictionary, print the dictionary
  if yes_or_no(dictionary_request):
    
    print('\n\nNew Language Name: {}\nOriginal Language Name: {}\n\nYour dictionary is:'.format(NAME_NEW_LANG, NAME_ORIG_LANG))

    internal_print_dictionary(NAME_NEW_LANG)
  
  # if using the default dictionary, print the dictionary

  else:
    WORDS = {}
    print('\nNew Language Name: {}\nOriginal Language Name: {}\n\nYour dictionary is empty.\n\n*****'.format(NAME_NEW_LANG, NAME_ORIG_LANG))

def yes_or_no(request):
  """This function ensures the user answers yes or no by determining if the input starts with y or n."""

  while True:
    print(request)
    answer = input('> ').upper()
    if answer.startswith('Y'):
      return True
    elif answer.startswith('N'):
      return False
    else:
      print('\n\tPlease answer [Y] or [N]\n')

def print_word_list(language):

  """Prints the words in one language."""
  print('\n\tThe words in {} are:\n'.format(language))

  for key, value in WORDS.items():
    if language == NAME_NEW_LANG:
      print('\t\t', key)
    else:
      print('\t\t', value)

def internal_print_dictionary(language):
  """Called within functions to print the dictionary."""

  # checks to make sure there are words in the dictionary
  if len(WORDS) == 0:
    print('\nThere are currently no words in your dictionary.')

  # print the keys first if it's the new language
  elif language == NAME_NEW_LANG:
    print("\n\t\t%-20s %s" %(NAME_NEW_LANG, NAME_ORIG_LANG))
    print("\t\t%-20s %s" %("-----", "-----"))
    for key, value in WORDS.items():
      print("\t\t%-20s %s" %(key, value))
    print('\nRemember, words are case sensitive.')
  
  # print the values first if it's the original language
  else:
    print("\n\t\t%-20s %s" %(NAME_ORIG_LANG, NAME_NEW_LANG))
    print("\t\t%-20s %s" %("-----", "-----"))
    for key, value in WORDS.items():
      print("\t\t%-20s %s" %(value, key))
    print('\nRemember, words are case sensitive.')

def format_header(header):
  stars = ""
  for letter in header:
    stars = stars + "*"
  
  print (f'\n{stars}\n{header}\n{stars}')

#
#   WORD FUNCTIONS
#

def get_valid_word(language, task):
  """This function ensures the user inputs a valid word."""

  # check if it's the new language
  if language == NAME_NEW_LANG:
    return validate_word (NAME_NEW_LANG, task)

  # otherwise, it must be the original language
  else:
    return validate_word (NAME_ORIG_LANG, task)

def validate_word (language,task):
  """This function validates the word the user has input within a language. It is different from get_valid_word() because here is where it is actually checked."""

  while True:

    print('\nWhat word would you like to {}?'.format(task))
    word_input = input('> ')

    # checks if the word is in the new language
    if language == NAME_NEW_LANG:
      for x in WORDS:
        if x == word_input:
          # print('\n\t"{}" is a valid word in {}.\n'.format(word_input,language))
          return word_input

    # checks if the word is in the new language
    elif language == NAME_ORIG_LANG:
      for x in WORDS:
        if WORDS[x] == word_input:
          # print('\n\t"{}" is a valid word in {}.\n'.format(word_input,language))
          return word_input
    
    # otherwise, it's not a valid word
    print('\n\tPlease enter a valid word.')

    # list the words for the user
    print_word_list(language)

    print('\t\nRemember, words are case sensitive.')

#
#   LANGUAGE FUNCTIONS
#

def get_valid_language(task):
  """This function gets a valid language name from the user."""

  while True:
    
    language = input('\nWhich language would you like to {}?\n> '.format(task))

    if language == NAME_NEW_LANG or language == NAME_ORIG_LANG:
      return language

    else:
      print('\nPlease enter {} or {}.'.format(NAME_NEW_LANG, NAME_ORIG_LANG))

def in_lang(word):
  """Checks if the word is in the dictionary and returns True or False. """

  for key, value in WORDS.items():

    # checks if the word is in the new language
    if key == word:
      print ('{} is already defined in the language {}. Please enter a new word.'.format(word, NAME_NEW_LANG))
      return True
    
    # checks if the word is in the original language
    elif value == word:
      print ('{} is already defined in the language {}. Please enter a new word.'.format(word, NAME_ORIG_LANG))
      return True

  # otherwise, we're in the clear
  return False

def get_other_language(language):
  """Gets the name of the other language."""
  
  if language == NAME_NEW_LANG:
    return NAME_ORIG_LANG

  else:
    return NAME_NEW_LANG

#
#   FUNCTIONS FOR TRANSLATION
#

def parse_text(text):
  """This function works to translate to special characters and handles not having punctuation at the end."""

  current_word = ""
  text_list = []

  iteration_counter = 0

  for character in text:

    iteration_counter += 1

    # check to see if this is the end of the sentence and if so return
    if iteration_counter == len(text):

      current_word = current_word + character
      text_list.append(current_word)
      return text_list

    elif character.isalnum():
      current_word = current_word + character
    
    # otherwise it's punctuation, a special character, or a space
    else:
      #append the completed word
      text_list.append(current_word) 

      #append the non-letter character that follows that word
      text_list.append(character) 

      #reset the current_word "counter"
      current_word = "" 

def swap_words(language, text_list):
  """This function compares the list of words in the text to the list of words in the language and replaces common words."""

  # check if the text is in the new language
  if language == NAME_NEW_LANG:
    for word_in_text in text_list:
      for key, value in WORDS.items():
        if word_in_text == key:
          index_of_word = text_list.index(word_in_text)
          text_list[index_of_word] = value

  #otherwise, the text is in the original language
  else:
    for word_in_text in text_list:
      for key, value in WORDS.items():
        if word_in_text == value:
          index_of_word = text_list.index(word_in_text)
          text_list[index_of_word] = key

  return text_list
 
#
#   TASK FUNCTIONS
#

def add_word():
  """Add a word to the dictionary."""
  format_header('Add Word')

  while True:

    new_word = ""
    orig_word = ""

    #  make sure the new word only contains letters or numbers
    while not new_word.isalnum():
      print('\nWhat is the word you would like to add to {}?'.format(NAME_NEW_LANG))
      new_word = input('> ')
      if not new_word.isalnum():
        print('\n\tPlease enter a word that contains only letters and numbers.')

    while not orig_word.isalnum():
      print('\nWhat is the meaning of the word {} in {}?'.format(new_word, NAME_ORIG_LANG))
      orig_word = input('> ')
      if not orig_word.isalnum():
          print('\n\tPlease enter a word that contains only letters and numbers.')

    if not in_lang(new_word):
      WORDS[new_word] = orig_word
      print('\n\t"{}" with the meaning "{}" successfully added to {}.\n'.format(new_word, orig_word, NAME_NEW_LANG))
      if yes_or_no('Would you like to add another word?') == False:
        break

def delete_word():
  """Delete a word from the dictionary."""

  format_header('Delete Word')

  while True:

    # if the dictionary is empty, return to main menu
    if len(WORDS) == 0:
      print('\nYou currently have no words in your dictionary.')
      break

    # get valid language name and word name
    language = get_valid_language("delete from")
    word_to_delete = get_valid_word(language,'delete')

    if language == NAME_NEW_LANG:
      del WORDS[word_to_delete]
      print('\n\t"{}" successfully deleted from {}.\n'.format(word_to_delete,language))

    elif language == NAME_ORIG_LANG:
      for key, value in WORDS.items():
        if value == word_to_delete:
          del WORDS[key]
          print('\n\t"{}" with the meaning {} was successfully deleted from {}.\n'.format(value, key, language))
          break
    else:
      print('\tDelete unsuccessful.\n')

    # ask if the user wants to delete another word
    if yes_or_no('Would you like to delete another word?') == False:
      break

def look_up_word():
  """Look up a word in the dictionary."""

  format_header('Look Up Word')

  while True:

    # if the dictionary is empty, return to main menu
    if len(WORDS) == 0:
      print('\nYou currently have no words in your dictionary.')
      break

    # get language and word
    language = get_valid_language('look up the word in')
    word = get_valid_word(language,"look up")
    other_language = get_other_language(language)

    # see if word is in the dictionary
    for key, value in WORDS.items():
      
      # because the user could enter a word in the new language that also has a meaning in the original language
      if word == key and word == value:
        print('\n\t"{}" means "{}" in {}.'.format(word, key, NAME_NEW_LANGUAGE))
        print('\n\t"{}" means "{}" in {}.'.format(word, value, NAME_OTHER_))
        break

      elif word == key:
        print('\n\t"{}" means "{}" in {}.'.format(word, value, other_language))
        break
      
      elif word == value:
        print('\n\t"{}" means "{}" in {}.'.format(word, key, other_language))
        break

    else:
      print('Sorry! Word not found.')
    if not yes_or_no('\nWould you like to look up another word?'):
      break

def print_dictionary():
  """Prints the dictionary."""

  format_header('Print Dictionary')

  # if the dictionary is empty, return to main menu
  if len(WORDS) == 0:
    print('\nYou currently have no words in your dictionary.')

  else:

    language = get_valid_language("list first")
    
    #print the dictionary
    print('\n\tThe words in {} with their definitions are:'.format(language))

    if language == NAME_NEW_LANG:
      internal_print_dictionary(NAME_NEW_LANG)

    # otherwise, it's the original language
    else:
      internal_print_dictionary(NAME_ORIG_LANG)

def translate():
  """Translates words or text."""

  format_header('Translation')
  print('\n>>>>> You may translate a word or a full text.')

  while True:

      # if the dictionary is empty, return to main menu
    if len(WORDS) == 0:
      print('\nYou currently have no words in your dictionary and so cannot execute a translation.')
      break

    language = get_valid_language("translate from")
    
    text = str(input('\nWhat is the word or text you would like to translate?\n> '))

    text_list = parse_text(text)

    text_list = swap_words(language, text_list)

    print('\nYour original text in {} is:\n\n\t{}\n'.format(language,text))

    other_lang = get_other_language(language)
    print('Your translated text in {} is:\n\n\t{}\n'.format(get_other_language(language),"".join(text_list)))
  
    if not yes_or_no('Would you like to translate more text or words?'):
      break

#
#   MAIN PROGRAM
#

def run_main():
  """This is where the main program is run."""
  
  print('****************************')
  print('*                          *')
  print('*          myLang          *')
  print('*                          *')
  print('****************************\n')

  print(' Make up your own language!\n')
  print('****************************\n')

  # ask user to name the language
  set_up_dictionary()

  # this is where the action happens
  while True:
    format_header('Main Menu')
    print()
    print('\t[1] Add a word')
    print('\t[2] Delete a word')
    print('\t[3] Look up a word')
    print('\t[4] Print your dictionary')
    print('\t[5] Translate')
    print('\t[6] Exit')

    task = input('\nWhat would you like to do?\n> ')

    if task == '1':
      add_word()

    elif task == '2':
      delete_word()

    elif task == '3':
      look_up_word()

    elif task == '4':
      print_dictionary()

    elif task == '5':
      translate()

    elif task == '6':
      print('\nThis has been fun! Goodbye!')
      break

    else:
      print('\nPlease enter a valid menu number.')

run_main()
