import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # Returns True if balanced and False if not
  # First read in the file and then convert everything to a list of tokenized characters
  # without any spaces

  # Big O notation of this is O(n) because it will have to iterate
  # through the entire file and all characters to check the delimiters
  with open(filename, 'r') as file:
    string = file.read()
    string  = ''.join(string.split())
    tokens = list(string)
    # Make a stack and then start checking delimiters
    A = Stack()
    for i in tokens:
      if i in '([{':
        A.push(i)
      elif i in ')]}':
        x = A.pop()
    if len(A) == 0:
      return True
    return False


if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')