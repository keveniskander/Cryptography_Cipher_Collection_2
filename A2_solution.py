"""
-----------------------------
CP460 (Fall 2020)
Name: Keven Iskander
ID:   160634540
Assignment 2
-----------------------------
"""

"""
-----------------------------
CP460 (Fall 2020)
Assignment 2 Solution
-----------------------------
"""
import utilities
import math

"""--------- Constants ----------- """
DICT_FILE = 'engmix.txt'
PAD = 'q'
BLOCK_MAX_SIZE = 20

"""
----------------------------------------------------
            Task 1: Utilities
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   text (str)
              base (str)
Return:       positions (2D list)
Description:  Analyzes a given text for any occurrence of base characters
              Returns a 2D list with characters and their respective positions
              format: [[char1,pos1], [char2,pos2],...]
              Example: get_positions('I have 3 cents.','c.h') -->
              [['h',2],['c',9],['.',14]]
              Text and base are not changed
Asserts:      text and base are strings
---------------------------------------------------
"""
def get_positions(text,base):
    
    assert type(text) == str
    assert type(base) == str

    positions = []

    for i in range(len(text)):
        for j in range(len(base)):
            if text[i] == base[j]:
                positions.append([base[j], i])

    return positions

"""
----------------------------------------------------
Parameters:   text (str)
              base (str)
Return:       updated_text (str)
Description:  Removes all base characters from text
Asserts:      text and base are strings
---------------------------------------------------
"""
def clean_text(text,base):
    
    assert type(text) == str
    assert type(base) == str

    updated_text = text

    for i in range(len(text)):
        for j in range(len(base)):
            if text[i] == base[j]:
                # print('ha', end='')
                updated_text = updated_text.replace(base[j], '')


    return updated_text

"""
----------------------------------------------------
Parameters:   text (str)
              positions (lsit): [[char1,pos1],[char2,pos2],...]]
Return:       updated_text (str)
Description:  Inserts all characters in the positions 2D list into their respective
Asserts:      text is a string and positions is a list
---------------------------------------------------
"""
def insert_positions(text, positions):
    
    assert type(text) == str
    assert type(positions) == list

    updated_text = text

    for i in range(len(positions)):
        updated_text = updated_text[:positions[i][1]] + positions[i][0] + updated_text[positions[i][1]:]
    return updated_text

"""
----------------------------------------------------
Parameters:   text (str)
              block_size (int)
              padding (bool): False/default = no padding, True = padding
              pad (str): default = PAD
Return:       blocks (list)
Description:  Create a list containing strings each of given block size
              if padding flag is set, pad using given padding character
              if no padding character given, use global PAD
Asserts:      text is a string and b_size is a positive integer
---------------------------------------------------
"""
def text_to_blocks(text,b_size,padding = 0,pad =PAD):
    
    assert type(text) == str
    assert type(b_size) == int
    assert b_size > 0

    blocks = []
    i = 0
    
    while i < (len(text)):
        if len(text) - i < b_size and padding == 1:
           
            # print('hey2')
            blocks.append(text[i:i+b_size] + (pad * (b_size-(len(text)-i))))
                
        else:
            blocks.append(text[i:i+b_size])
        i+=b_size
    return blocks

"""
----------------------------------------------------
Parameters:   text (string): input string
              shifts (int): number of shifts
              direction (str): 'l' or 'r'
Return:       update_text (str)
Description:  Shift a given string by given number of shifts (circular shift)
              If shifts is a negative value, direction is changed
              If no direction is given or if it is not 'l' or 'r' set to 'l'
Asserts:      text is a string and shifts is an integer
---------------------------------------------------
"""
def shift_string(text,shifts,direction):
    # your code here
    return updated_text

"""
----------------------------------------------------
Parameters:   input_list (list): 2D list
              item (?)
Return:       i,j (int,int)
Description:  Performs linear search on input list to find "item"
              returns i,j, where i is the row number and j is the column number
              if not found returns -1,-1
Asserts:      input_list is a list
---------------------------------------------------
"""
def index_2d(input_list,item):
    # your code here
    return -1,-1

"""
----------------------------------------------------
            Task 2: Block Rotation Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   key (b,r): tuple(int,int)
Return:       updated_key (b,r): tuple(int,int)
Description:  Private helper function for block rotate cipher
              Update the key to smallest positive value
              if an invalid key return (0,0)
Asserts:      None
---------------------------------------------------
"""
def _adjust_key_block_rotate(key):
    # your code here
    return updated_key

"""
----------------------------------------------------
Parameters:   plaintext (str)
              key (tuple(int,int))
Return:       ciphertext (str)
Description:  Encryption using Block Rotation Cipher
              Uses left circular rotation + padding
Asserts:      plaintext is a string
Errors:       if invalid key: 
                print: "Error(e_block_rotate): invalid key"
                return empty string
---------------------------------------------------
"""
def e_block_rotate(plaintext,key):
    # your code here
    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              key (tuple(int,int))
Return:       plaintext (str)
Description:  Decryption using Block Rotation Cipher
              Removes padding if it exist
Asserts:      ciphertext is a string
Errors:       if invalid key: 
                print: "Error(d_block_rotate): invalid key" 
                return empty string
---------------------------------------------------
"""
def d_block_rotate(ciphertext,key):
    # your code here
    return plaintext

"""
----------------------------------------------------
Parameters:   ciphertext (string)
              arguments (list): [b0,bn,r] default = [0,0,0]
                          b0: minimum block size
                          bn: maximum block size
                          r: rotations
Return:       key,plaintext
Description:  Cryptanalysis of Block Rotate Cipher
              Returns plaintext and key (r,b)
              Attempts block sizes from b1 to b2 (inclusive)
              If bn is invalid or unspecified use BLOCK_MAX_SIZE
              Minimum valid value for b0 is 1
---------------------------------------------------
"""
def cryptanalysis_block_rotate(ciphertext,arguments=[0,0,0]):
    # your code here
    return '',''
