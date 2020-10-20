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
def shift_string(text,shifts,direction='l'):
    
    assert type(text) == str
    assert type(shifts) == int

    updated_text = text
    accepted_directions = 'rRlL'

    if direction not in accepted_directions:
        direction = 'l'

    if abs(shifts) > len(text):

        if shifts > 0:
            shifts = shifts % len(text)
        else:
            shifts = abs(shifts) % len(text)
            shifts = -shifts
            # print('less')

    if shifts > 0:

        if direction == 'r' or direction == 'R':
            
            updated_text = updated_text[-shifts:] + updated_text[:-shifts]
            # print('r1')
        if direction == 'l' or direction == 'L':
        
            updated_text = updated_text[shifts:] + updated_text[:shifts]
            # print('l1')

    elif shifts < 0:
        if direction == 'r' or direction == 'R':
            
            updated_text = updated_text[-shifts:] + updated_text[:-shifts]
            # print('r2')
        if direction == 'l' or direction == 'L':
            
            updated_text = updated_text[shifts:] + updated_text[:shifts]
            # print('l2')

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
    
    assert type(input_list) == list

    for i in range(len(input_list)):
        j = 0
        while j < len(input_list[i]):
            if input_list[i][j] == item:
                return i, j
            j+=1
        
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

    updated_key = 0,0
    
    if type(key) == tuple:
        if isinstance(key[0], int) and isinstance(key[1], int) and key[0]>0:
            temp0 = key[0]
            temp1 = key[1]
            
            while (temp1>temp0):
                temp1 = temp1 - temp0
            while (temp1<0):
                if temp0 + temp1 < temp0:
                    temp1 = temp1 + temp0
            updated_key = (temp0, temp1)
            

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
    
    assert type(plaintext) == str

    ciphertext = ''
    
    space_positions = get_positions(plaintext, '\n')
    plaintext = clean_text(plaintext, '\n')

    key = _adjust_key_block_rotate(key)
    if key == (0,0):
        print("Error(e_block_rotate): invalid key")
    
    plainblocks = text_to_blocks(plaintext, key[0], padding=1, pad=PAD)
    # print(cipherblocks)

    for i in range(len(plainblocks)):
        plainblocks[i] = shift_string(plainblocks[i], key[1], direction='l')
        ciphertext = ciphertext + plainblocks[i]

    # for j in range(len(cipherblocks)):
    #     ciphertext = ciphertext + cipherblocks[j]

    ciphertext = insert_positions(ciphertext, space_positions)
    
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
    
    assert type(ciphertext) == str

    plaintext = ''
    
    space_positions = get_positions(ciphertext, '\n')
    ciphertext = clean_text(ciphertext, '\n')

    key = _adjust_key_block_rotate(key)
    if key == (0,0):
        print("Error(e_block_rotate): invalid key")

    cipherblocks = text_to_blocks(ciphertext, key[0])

    for i in range(len(cipherblocks)):
        cipherblocks[i] = shift_string(cipherblocks[i], key[1], direction='r')
        plaintext = plaintext + cipherblocks[i]

    plaintext = insert_positions(plaintext, space_positions)
    plaintext = plaintext.rstrip(PAD)

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

    dict_list = utilities.load_dictionary(DICT_FILE)

    # if arguments[1] == 0:
    #     arguments[1] = BLOCK_MAX_SIZE
    
    if (arguments[0] > 0 and arguments[1]> 0) and (arguments[0] == arguments[1]) and arguments[2] == 0:
        for i in range(arguments[1]):
            
            text = d_block_rotate(ciphertext, (arguments[1], i))
            # print(text)
            if utilities.is_plaintext(text, dict_list) == True:
                return (arguments[1],i), text
        

    if (arguments[0] == 0 and arguments[1] == 0) and (arguments[2] > 0):
        
        for i in range(arguments[0], arguments[1]):

            text = d_block_rotate(ciphertext, (i, arguments[2]))
            if utilities.is_plaintext(text, dict_list) == True:
                return (i, arguments[2]), text

    if (arguments[0] > 0 or arguments[1]> 0) and arguments[2] == 0:
        # print('test')
        
        if arguments[1] == 0:
            arguments[1] = BLOCK_MAX_SIZE
        if arguments[0] == 0:
            arguments[0] = 1
        # print(arguments[0], arguments[1])
        for i in range(arguments[0], arguments[1]): 

            for j in range(arguments[1]):
                
                text = d_block_rotate(ciphertext, (i, j))
                if utilities.is_plaintext(text, dict_list) == True:
                    # print(text)
                    return (i, j), text

        
    if (arguments[0] == 0 and arguments[1] == 0 and arguments[2] == 0):
        if arguments[1] == 0:
            arguments[1] = BLOCK_MAX_SIZE
        if arguments[0] == 0:
            arguments[0] = 1

        for i in range(arguments[0], arguments[1]): 

            for j in range(arguments[1]):
                
                text = d_block_rotate(ciphertext, (i, j))
                if utilities.is_plaintext(text, dict_list) == True:
                    return (i, j), text

    # The last two if statements could be combined in a single if statement (maybe)
    

    return '',''

"""
----------------------------------------------------
            Task 3: Wheatstone Playfair Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   text (str)
Return:       f_text (str): formatted text
Description:  Formats a plaintext
              1- Every W/w is converted to VV/vv
              2- Append an x if the text length is odd (excluding non-alpha chars)
              3- Convert every double character pair ## to #x or #X
----------------------------------------------------
"""
def _format_playfair(plaintext):
    
    # plaintext =  clean_text(plaintext, utilities.get_base('nonalpha'))
    special = utilities.get_base('nonalpha')

    plaintext = plaintext.replace('w', 'vv')
    plaintext = plaintext.replace('W', 'VV')

    positions = []
    for a in range(len(plaintext)):
        if plaintext[a] == ' ':
            positions.append([' ',a])
        if plaintext[a] in special:
            positions.append([plaintext[a],a])
        if plaintext[a] == '\n':
            positions.append([plaintext[a],a])

    plaintext = clean_text(plaintext,' ')
    plaintext = clean_text(plaintext,special)
    plaintext = clean_text(plaintext,'\n')

    i=0
    while i < len(plaintext)-1:
          
        if plaintext[i] == plaintext[i+1] and plaintext[i].isupper() == True:
            plaintext = plaintext[:i+1] + 'X' + plaintext[i+2:]
        if plaintext[i] == plaintext[i+1] and plaintext[i].islower() == True:
            plaintext = plaintext[:i+1] + 'x' + plaintext[i+2:]

        
        i += 2


    if len(plaintext) % 2 != 0:
        plaintext = plaintext + 'x'
    
      
    plaintext = insert_positions(plaintext, positions)



    return plaintext

"""
----------------------------------------------------
Parameters:   text (str)
Return:       r_text (str): restored text
Description:  Restores a plaintext by:
              1- Converting VV/vv back to W/w
              2- Append an x if the text length is odd (excluding non-alpha chars)
              3- Convert every double character pair ## to #x or #X
Asserts:      None
----------------------------------------------------
"""
def _restore_playfair(text): 
    # print(text)
    # r_text =  clean_text(text, utilities.get_base('nonalpha'))
    r_text = text
 
    dict_list = utilities.load_dictionary(DICT_FILE)

    new_text = ''



    i = 0
    # print(r_text)
    
    while i < len(r_text)-1:
      
        if r_text[i] == 'V' and r_text[i+1] == 'X' and r_text[i-1]!='V':
            r_text = r_text[:i+1] + 'V' + r_text[i+2:]
            # r_text = r_text.replace('VV', 'W')
        if r_text[i] == 'v' and r_text[i+1] == 'x'and r_text[i-1]!='v':
            r_text = r_text[:i+1] + 'v' + r_text[i+2:]
            # r_text = r_text.replace('vv', 'w')
            # print(r_text)
        
        i += 1
    # print(r_text)
    r_text = r_text.replace('VV', 'W')
    r_text = r_text.replace('vv', 'w')
    # print(r_text)

    specials = utilities.get_base('nonalpha')
    positions = []

    for a in range(len(r_text)):
        if r_text[a] == ' ':
            positions.append([' ',a])
        if r_text[a] in specials:
            positions.append([r_text[a],a])
        if r_text[a] == '\n':
            positions.append([r_text[a],a])

   

    if len(r_text)-1 % 2 != 0:
        r_text = r_text.rstrip('x')
        # print(r_text)
        # print('YES')

    word_list = utilities.text_to_words(r_text)
    # print(word_list)
    

    for i in range(len(word_list)):
        word_list[i] = _restore_word_playfair(word_list[i], dict_list)
        new_text = new_text + word_list[i]
    
    # print(new_text)

    r_text = new_text

    # print(r_text)

    r_text = clean_text(r_text,' ')
    r_text = clean_text(r_text, specials)
    r_text = clean_text(r_text, '\n')
    if len(r_text) % 2 != 0:
        r_text = r_text.rstrip('x')
    

    # print('W placed', r_text)

    
    r_text = insert_positions(r_text, positions)
    return r_text

"""
----------------------------------------------------
Parameters:   word (str)
              dict_list (list): 2d dictionary list
Return:       r_word (str): restored word
Description:  Restores a word by removing the 'x' character whenever necessary
              Assumes a word has no more than two x's
              Assumes word is either lower, UPPER or Capitalized
Asserts:      None
----------------------------------------------------
"""
def _restore_word_playfair(word,dict_list):
    
    new_word = word
    x_count = 0
    i = 0
    x_char = 'x'
    if new_word.isupper()==True:
        x_char = 'X'
    if utilities.is_plaintext(new_word, dict_list, 1) == True:
        return new_word
    else:
        while i < len(new_word):
            if new_word[i] == x_char and i != 0 and x_count < 2:
                # print('test1')
                new_word = new_word[:i] + new_word[i-1] + new_word[i+1:]
                if utilities.is_plaintext(word, dict_list, 1) == True:
                    return new_word
                x_count+=1
            i+=1

    if utilities.is_plaintext(new_word, dict_list, 1) == False:
        j = 0
        x_count = 0
        x_skip = 1
        new_word = word
        while j < len(new_word):
            if new_word[j] == x_char and j != 0 and x_count < 2:
                # print('test2')
                if x_skip == 0:
                    x_skip-=1
                    new_word = new_word[:j] + new_word[j-1] + new_word[j+1:]
                    if utilities.is_plaintext(word, dict_list, 1) == True:
                        return new_word
                else:
                    x_skip-=1
                x_count+=1
            j+=1

    if utilities.is_plaintext(new_word, dict_list, 1) == False:
        k = 0
        x_count = 0
        x_skip = 1
        new_word = word
        while k < len(new_word):
            if new_word[k] == x_char and k != 0 and x_count < 2:
                # print('test3')
                if x_skip == 1:
                    x_skip-=1
                    new_word = new_word[:k] + new_word[k-1] + new_word[k+1:]
                    if utilities.is_plaintext(word, dict_list, 1) == True:
                        return new_word
                else:
                    x_skip-=1
                x_count+=1
            k+=1

    
    return new_word

"""
----------------------------------------------------
Parameters:   plaintext(str)
              key (list): Playfair Square
Return:       ciphertext (str)
Description:  Encryption using Wheatstone Playfair Cipher
              Preserves all non-alpha characters
              Preserves case of characters
              Uses vv for w
              Invokes _format_playfair utility function
Asserts:      plaintext is a string and key is a list
----------------------------------------------------
"""
def e_playfair(plaintext, key):
    
    assert type(plaintext) == str
    assert type(key) == list
    
    ciphertext = _format_playfair(plaintext)
    # print(ciphertext)

    specials = utilities.get_base('nonalpha')
    positions = []

    for a in range(len(ciphertext)):
        if ciphertext[a] == ' ':
            positions.append([' ',a])
        if ciphertext[a] in specials:
            positions.append([ciphertext[a],a])
        if ciphertext[a] == '\n':
            positions.append([ciphertext[a],a])

    ciphertext = clean_text(ciphertext,' ')
    ciphertext = clean_text(ciphertext, specials)
    ciphertext = clean_text(ciphertext, '\n')

    cipherblock = text_to_blocks(ciphertext, 2)
    # print(cipherblock, ciphertext)
    # print(cipherblock)

    new_text = ''

    
    for i in range(len(cipherblock)):

        first = index_2d(key, cipherblock[i][0].upper())
        second = index_2d(key, cipherblock[i][1].upper())

        fi = first[0]
        fj = first[1]
        si = second[0]
        sj = second[1]

        # print(cipherblock, fi, fj, si, sj, ciphertext)
        # print(cipherblock)
        # print(fi,fj,si,sj)
        if fi == si and fi != -1 and si != -1:
            # print('TEST1')
            if fj != len(key)-1:
                fj+=1
            else:
                fj = 0
            if sj != len(key)-1:
                sj+=1
            else:
                sj = 0
            
        elif fj == sj and fj != -1 and sj != -1:
            # print('TEST2')
            if fi != len(key)-1:
                fi +=1
            else:
                fi = 0
            if si != len(key)-1:
                si+=1
            else:
                si = 0

        elif sj < fj and sj != -1 and fj != -1:
            # print('TEST3')
            if first[1] - (first[1]-second[1])>=0:
                fj = fj - (first[1]-second[1])
            else:
                fj = len(key)-1
            if second[1] + (first[1]-second[1]) < 5:
                sj = sj + (first[1]-second[1])
            else:
                sj = len(key)-1

        elif fj < sj and fj != -1 and sj != -1:
            # print('TEST4')
            if first[1] - (first[1]-second[1]) >= 0:
                fj = fj - (first[1]-second[1])
            else:
                fj = 0
            if second[1] - (second[1]-first[1]) >= 0:
                sj = sj - (second[1]-first[1])
            else:
                # print('TEST')

                sj=0 #+ (second[1]-first[1])
        
        # print(cipherblock[i], fi, fj, si, sj)
        if fi < 0 or fj < 0:
            if cipherblock[i][1].islower():
                cipherblock[i] = ' ' + key[si][sj].lower()
            else:
                cipherblock[i] = ' ' + key[si][sj]
        elif si < 0 or sj < 0:
            if cipherblock[i][0].islower():
                cipherblock[i] = key[fi][fj].lower() + ' '
            else:
                cipherblock[i] = key[fi][fj] + ' '
        else:
            if cipherblock[i].islower():
                cipherblock[i] = key[fi][fj].lower() + key[si][sj].lower()
            elif cipherblock[i][0].islower()==False and cipherblock[i][1].islower()==True:
                cipherblock[i] = key[fi][fj] + key[si][sj].lower()
            elif cipherblock[i][0].islower()==True and cipherblock[i][1].islower()==False:
                cipherblock[i] = key[fi][fj].lower() + key[si][sj]
            else:
                cipherblock[i] = key[fi][fj] + key[si][sj]
        new_text+=cipherblock[i]

    
    ciphertext = new_text
    ciphertext = insert_positions(ciphertext, positions)

    # print(cipherblock)
    # print(ciphertext)

    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
              key (list): Playfair Square
Return:       plaintext (str)
Description:  Decryption using Wheatstone Playfair Cipher
              Invokes _restore_playfair function to restore plaintext
Asserts:      ciphertext is a string and key is a list
----------------------------------------------------
"""
def d_playfair(ciphertext, key):
    
    assert type(ciphertext) == str
    assert type(key) == list

    plaintext = ciphertext

    specials = utilities.get_base('nonalpha')
    positions = []

    for a in range(len(plaintext)):
        if plaintext[a] == ' ':
            positions.append([' ',a])
        if plaintext[a] in specials:
            positions.append([plaintext[a],a])
        if plaintext[a] == '\n':
            positions.append([plaintext[a],a])

    plaintext = clean_text(plaintext,' ')
    plaintext = clean_text(plaintext, specials)
    plaintext = clean_text(plaintext, '\n')

    plainblock = text_to_blocks(plaintext, 2)
    # print(cipherblock, ciphertext)
    # print(plainblock)

    new_text = ''

    for i in range(len(plainblock)):

        first = index_2d(key, plainblock[i][0].upper())
        second = index_2d(key, plainblock[i][1].upper())

        fi = first[0]
        si = second[0]
        fj = first[1]
        sj = second[1]

        if fi == si and fi != -1 and si != -1:
            # print('TEST1')
            if fj != 0:
                fj-=1
            else:
                fj = len(key)-1
            if sj != 0:
                sj-=1
            else:
                sj = len(key)-1

        elif fj == sj and fj != -1 and sj != -1:
            # print('TEST2')
            if fi != 0:
                fi -=1
            else:
                fi = len(key)-1
            if si != 0:
                si-=1
            else:
                si = len(key)-1

        elif fj < sj and sj != -1 and fj != -1:
            # print('TEST3')
            if first[1] - (first[1]-second[1])>=0:
                fj = fj - (first[1]-second[1])
            else:
                fj = len(key)-1
            if second[1] + (first[1]-second[1]) < 5:
                sj = sj + (first[1]-second[1])
            else:
                sj = len(key)-1

        elif sj < fj and fj != -1 and sj != -1:
            # print('TEST4')
            if first[1] - (first[1]-second[1]) >= 0:
                fj = fj - (first[1]-second[1])
            else:
                fj = 0
            if second[1] - (second[1]-first[1]) >= 0:
                sj = sj - (second[1]-first[1])
            else:
                # print('TEST')
                sj = 0
        #         sj=len(key)-1 #+ (second[1]-first[1])

        if fi < 0 or fj < 0:
            if plainblock[i][1].islower():
                plainblock[i] = ' ' + key[si][sj].lower()
            else:
                plainblock[i] = ' ' + key[si][sj]
        elif si < 0 or sj < 0:
            if plainblock[i][0].islower():
                plainblock[i] = key[fi][fj].lower() + ' '
            else:
                plainblock[i] = key[fi][fj] + ' '
        else:
            if plainblock[i].islower():
                plainblock[i] = key[fi][fj].lower() + key[si][sj].lower()
            elif plainblock[i][0].islower()==False and plainblock[i][1].islower()==True:
                plainblock[i] = key[fi][fj] + key[si][sj].lower()
            elif plainblock[i][0].islower()==True and plainblock[i][1].islower()==False:
                plainblock[i] = key[fi][fj].lower() + key[si][sj]
            else:
                plainblock[i] = key[fi][fj] + key[si][sj]
        new_text+=plainblock[i]

    # print(new_text)
    plaintext = new_text
    plaintext = insert_positions(plaintext, positions)
    plaintext = _restore_playfair(plaintext)
    # print(plaintext)
    
    


    return plaintext

"""
----------------------------------------------------
        Task 4: Columnar Transposition Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   key (str)           
Return:       key_order (list)
Description:  Returns key order, e.g. [face] --> [1,2,3,0]
              If invalid key --> return []
              Applies to all ASCII characters from space to ~
Asserts:      None
----------------------------------------------------
"""
def _get_order_ct(key):
    # your code here
    return key_order

"""
----------------------------------------------------
Parameters:   plaintext (str)
              kye (str)
Return:       ciphertext (list)
Description:  Encryption using Columnar Transposition Cipher
              Does not include whitespaces in encryption
              Uses padding
Asserts:      plaintext is a string
Errors:       if key is invalid:
                print: Error(e_ct): invalid key
----------------------------------------------------
"""
def e_ct(plaintext,key):
    # your code here
    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              kye (str)
Return:       plaintext (list)
Description:  Decryption using Columnar Transposition Cipher
Asserts:      ciphertext is a string
Errors:       if key is invalid:
                print: Error(d_ct): invalid key
----------------------------------------------------
"""
def d_ct(ciphertext,key):
    # your code here
    return plaintext