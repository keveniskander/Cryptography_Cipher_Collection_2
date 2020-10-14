"""
-----------------------------
CP460 (Fall 2020)
Utilities
Assignment 2
-----------------------------
"""
import string
import math

"""
----------------------------------------------------
Parameters:   base_type (str) 
Return:       result (str)
Description:  Return a base string containing a subset of ASCII charactes
              Defined base types:
              lower: lower case characters
              upper: upper case characters
              alpha: upper and lower case characters
              num: numerical characters
              lowernum: lower case and numerical characters
              uppernum: upper case and numerical characters
              alphanum: upper, lower and numerical characters
              nonalpha: all non alphabetical characters
              special: punctuations and special characters (no white space)
              all: upper, lower, numerical and special characters
---------------------------------------------------
"""
def get_base(base_type):
    lower = "".join([chr(ord('a')+i) for i in range(26)])
    upper = lower.upper()
    num = "".join([str(i) for i in range(10)])
    special = ''
    for i in range(ord('!'),127):
        if not chr(i).isalnum():
            special+= chr(i)
            
    result = ''
    if base_type == 'lower':
        result = lower
    elif base_type == 'upper':
        result = upper
    elif base_type == 'alpha':
        result = upper + lower
    elif base_type == 'num':
        result = num
    elif base_type == 'lowernum':
        result = lower + num
    elif base_type == 'uppernum':
        result = upper + num
    elif base_type == 'alphanum':
        result = upper + lower + num
    elif base_type == 'special':
        result = special
    elif base_type == 'nonalpha':
        result = special + num
    elif base_type == 'all':
        result = upper + lower + num + special
    else:
        print('Error(get_base): undefined base type')
        result = ''
    return result

"""
----------------------------------------------------
Parameters:   text (str)
              dict_list (list)
Return:       match (int)
              mismatch (int)
Description:  Reads a given text, checks if each word appears in given dictionary
              Returns number of matches and number of mismatches.
              Words are compared in lowercase
              Assumes a proper dict_list
Asserts:      text is a string and dict_list is a string
---------------------------------------------------
"""
def analyze_text(text, dict_list):
    assert type(text) == str and type(dict_list) == list, 'invalid inputs'
    word_list = text_to_words(text)
    alphabet = get_base('lower')
    match = 0
    mismatch = 0
    for w in word_list:
        if w.isalpha():
            list_num = alphabet.index(w[0].lower())
            if w.lower() in dict_list[list_num]:
                match+=1
            else:
                mismatch+=1
        else:
            mismatch+=1
    return match,mismatch

"""
----------------------------------------------------
Parameters:   text (str)
              dict_list (str): dictionary list
              threshold (float): number between 0 to 1
Return:       True/False
Description:  Check if a given file is a plaintext
              If #matches/#words >= threshold --> True
                  otherwise --> False
              If invalid threshold or not given, default is 0.9
              An empty string should return False
              Assumes a valid dict_list is passed
---------------------------------------------------
"""
def is_plaintext(text, dict_list, threshold=0.9):
    if text == '':
        return False
    result = analyze_text(text, dict_list)
    percentage = result[0]/(result[0]+result[1])
    if threshold <= 0 or threshold > 1:
        threshold = 0.9
    if percentage >= threshold:
        return True
    return False

"""
----------------------------------------------------
Parameters:   None 
Return:       square (2D List)
Description:  Constructs Playfair Square as lower case
              alphabets placed in spiral fashion
              Each element is a character
              Square size is 5x5
              The square does not have the character 'w'
---------------------------------------------------
"""
def get_playfair_square():
    square = [['I', 'H', 'G', 'F', 'E'],
              ['J', 'U', 'T', 'S', 'D'],
              ['K', 'V', 'Z', 'R', 'C'],
              ['L', 'X', 'Y', 'Q', 'B'],
              ['M', 'N', 'O', 'P', 'A']]
    return square


"""
----------------------------------------------------
Parameters:   filename (str)
Return:       contents (str)
Description:  Utility function to read contents of a file
              Can be used to read plaintext or ciphertext
---------------------------------------------------
"""
def file_to_text(filename):
    # put your code here
    return contents

"""
----------------------------------------------------
Parameters:   text (str)
              filename (str)            
Return:       no returns
Description:  Utility function to write any given text to a file
              If file already exist, previous content will be erased
---------------------------------------------------
"""
def text_to_file(text, filename):
    # put your code here
    return

"""
----------------------------------------------------
Parameters:   r: #rows (int)
              c: #columns (int)
              fill (str,int,double)
Return:       empty matrix (2D List)
Description:  Create an empty matrix of size r x c
              All elements initialized to fill
---------------------------------------------------
"""
def new_matrix(r,c,fill):
    # put your code here
    return []

"""
----------------------------------------------------
# Parameters:   marix (2D List)
# Return:       text (string)
# Description:  convert a 2D list of characters to a string
#               left to right, then top to bottom
#               Assumes given matrix is a valid 2D character list
---------------------------------------------------
"""
def matrix_to_string(matrix):
    # put your code here
    return text

"""
----------------------------------------------------
Parameters:   dict_file (str): filename
Return:       dict_list (list): 2D list
Description:  Reads a given dictionary file
              dictionary is assumed to be formatted: each word in a separate line
              Returns a list of lists, list 0 contains all words starting with 'a'
              list 1 all words starting with 'b' and so forth.
Asserts:      dict_file is a non-empty string
---------------------------------------------------
"""
def load_dictionary(dict_file):
    # put your code here
    return dict_list

"""
----------------------------------------------------
Parameters:   text (str)
Return:       word_list (list)
Description:  Reads a given text
              Returns a list of strings, each pertaining to a word in file
              Words are separated by a white space (space, tab or newline)
              Gets rid of all special characters at the start and at the end
Asserts:      text is a string
---------------------------------------------------
"""
def text_to_words(text):
    # put your code here
    return word_list
