import utilities
import A2_solution

def task1():
    print('{}'.format('-'*40))
    print("Start of Task 1: Utilities Testing")
    print()

    print('Testing get_positions:')
    str1 = 'One Must Acknowledge With Cryptography No Amount of Violence Will Ever Solve a Math Problem.'
    print('str1 = {}'.format(str1))
    print('get_positions(str1,get_base("upper")) --> ',end='')
    print('{}'.format(A2_solution.get_positions(str1,utilities.get_base('upper'))))
    print('get_positions(str1,get_base("vwxyz")) --> ',end='')
    print('{}'.format(A2_solution.get_positions(str1,'vwxyz')))
    print('get_positions(str1,get_base("special")) --> ',end='')
    print('{}'.format(A2_solution.get_positions(str1,utilities.get_base('special'))))
    print()
    
    print('Testing clean_text:')
    str2 = A2_solution.clean_text(str1,utilities.get_base('upper'))
    print('clean_text(str1,get_base("upper")) = {}'.format(str2))
    str3 = A2_solution.clean_text(str1,utilities.get_base('lower'))
    print('clean_text(str1,get_base("lower")) = {}'.format(str3))
    str4 = A2_solution.clean_text(str1,'abcdefghij')
    print('clean_text(str1,"abcdefghij") = {}'.format(str4))
    str5 = A2_solution.clean_text(str1,' \n')
    print('clean_text(str1," \\n") = {}'.format(str5))
    print()
    
    print('Testing insert_positions:')
    string = A2_solution.get_positions(str1,utilities.get_base('upper'))
    print(A2_solution.insert_positions(str2,string))
    string = A2_solution.get_positions(str1,utilities.get_base('lower'))
    print(A2_solution.insert_positions(str3,string))
    string = A2_solution.get_positions(str1,'abcdefghij')
    print(A2_solution.insert_positions(str4,string))
    string = A2_solution.get_positions(str1,' \n')
    print(A2_solution.insert_positions(str5,string))
    print()
    
    print('Testing text_to_blocks:')
    str6 = 'Cryptography is the fun part of math'
    print(A2_solution.text_to_blocks(str6,4))
    print(A2_solution.text_to_blocks(str6,5,0))
    print(A2_solution.text_to_blocks(str6,7))
    print(A2_solution.text_to_blocks(str6,8,1))
    print(A2_solution.text_to_blocks(str6,10,1,'x'))
    print()
    
    print('Testing shift_string:')
    print(A2_solution.shift_string(str6,4))
    print(A2_solution.shift_string(str6,-4))
    print(A2_solution.shift_string(str6,5,'l'))
    print(A2_solution.shift_string(str6,5,'r'))
    print(A2_solution.shift_string(str6,6,'k'))
    print(A2_solution.shift_string(str6,300,))
    print(A2_solution.shift_string(str6,-99,))
    print()
    
    print('Testing index_2d:')
    list1 = [[1,2,3],[4,5],[6,7,8,9,10],[11],[12,13]]
    print('list1 = {}'.format(list1))
    cases = [2,5,6,11,12,18]
    for case in cases:
        print('{} is at {}'.format(case,A2_solution.index_2d(list1,case)))
    print()
    
    print('End of Task 1: Utilities Testing')
    print('{}'.format('-'*40))
    print()
    return

def task2():
    print('{}'.format('-'*40))
    print("Start of Task 2: Block Rotation Cipher")
    print()

    print('Testing adjust Key:')
    print('({},{})\t--> '.format(4,3.5),end='')
    print('{}'.format(A2_solution._adjust_key_block_rotate((4,3.5))))
    print('{}\t--> '.format([4,5]),end='')
    print('{}'.format(A2_solution._adjust_key_block_rotate([4,5])))
    print('{}\t--> '.format(10),end='')
    print('{}'.format(A2_solution._adjust_key_block_rotate(10)))
    print('({},{})\t--> '.format(-2,1),end='')
    print('{}'.format(A2_solution._adjust_key_block_rotate((-2,1))))
    print('({},{})\t--> '.format(5,7),end='')
    print('{}'.format(A2_solution._adjust_key_block_rotate((5,7))))
    print('({},{})\t--> '.format(3,11),end='')
    print('{}'.format(A2_solution._adjust_key_block_rotate((3,11))))
    print('({},{})\t--> '.format(7,-6),end='')
    print('{}'.format(A2_solution._adjust_key_block_rotate((7,-6))))
    print('({},{})\t--> '.format(11,4),end='')
    print('{}'.format(A2_solution._adjust_key_block_rotate((11,4))))
    print()

    print('Testing encryption and decryption:')
    key = (4,3)
    print('Key = ',key)
    plaintext = utilities.get_base('lower')
    print('plaintext = ',end=' ')
    print(plaintext)
    ciphertext = A2_solution.e_block_rotate(plaintext,key)
    print('After encryption:',end=' ')
    print(ciphertext)
    print('After Decryption:',end=' ')
    recovered = A2_solution.d_block_rotate(ciphertext,key)
    print(recovered)
    print()

    key = (10,6)
    print('Key = ',key)
    plaintext = 'The internet, our greatest tool of emancipation, has been transformed into '
    plaintext+= 'the most dangerous facilitator of totalitarianism we have ever seen'
    print('plaintext = ')
    print(plaintext)
    ciphertext = A2_solution.e_block_rotate(plaintext,key)
    print('After encryption:')
    print(ciphertext)
    print('After Decryption:')
    recovered = A2_solution.d_block_rotate(ciphertext,key)
    print(recovered)
    print()
    
    key = (8,5)
    print('Key = ',key)
    plaintext = 'One must acknowledge with cryptography '
    plaintext+= 'no amount of violence will ever solve a math problem.'
    print('plaintext = ')
    print(plaintext)
    ciphertext = A2_solution.e_block_rotate(plaintext,key)
    print('After encryption:')
    print(ciphertext)
    print('After Decryption:')
    recovered = A2_solution.d_block_rotate(ciphertext,key)
    print(recovered)
    print()
    
    print('Testing Cryptanalysis: ')
    base_plaintext = utilities.file_to_text('plaintext1.txt')
    arguments = [[2,15,0],[0,0,0],[10,0,0],[0,10,0],[12,12,0]]
    for i in range(len(arguments)):
        filename = 'ciphertext'+str(i+1)+'.txt'
        ciphertext = utilities.file_to_text(filename)
        key, plaintext = A2_solution.cryptanalysis_block_rotate(ciphertext,arguments[i])
        if plaintext == '' and key == '':
            print('Cryptanalysis failed')
        else:
            print('key = {}'.format(key))
            if plaintext == base_plaintext:
                print('plaintext validated')
            else:
                print('plaintext validation failed')
        print()
        
    print('End of Task 2: Block Rotation Testing')
    print('{}'.format('-'*40))
    print()
    return

def task3():
    print('{}'.format('-'*40))
    print("Start of Task 3: Playfair Square Cipher")
    print()
    
    print('--------- Testing _format_playfair:')
    plaintexts = ['Light','lesson','door','floor','window','Widow','Are you happy?','What?! Angry!!','Wow!! That is wonderful!']
    for i in range(len(plaintexts)):
        print(plaintexts[i],'\t',A2_solution._format_playfair(plaintexts[i]))
    print()
     
    print('-------- Testing _restore_word_playfair: ')
    dict_list = utilities.load_dictionary('engmix.txt')
    words = ['a','road','ox','fox','anxious','doxr','exl','afxix','excesx','foxtbalx','Football','England']
    for word in words:
        print('{:8s} --> {:15s}'.format(word,A2_solution._restore_word_playfair(word,dict_list)),end='')
        print('{} --> {}'.format(word.upper(),A2_solution._restore_word_playfair(word.upper(),dict_list)))
    print()
     
    print('--------- Testing _restore_playfair:')
    cases = ['Lesxon Lightx','vxindovx floxrx','VXidovv floxr','Is it why or what?']
    for case in cases:
        print('Before: {}'.format(case))
        print('After : {}'.format(A2_solution._restore_playfair(case)))
        print()
         
    print('-------- Testing Encryption/Decryption: ')
    key = utilities.get_playfair_square()
    for i in range(len(plaintexts)):
        print('plaintext  = {}'.format(plaintexts[i]))
        ciphertext = A2_solution.e_playfair(plaintexts[i],key)
        print('ciphertext = {}'.format(ciphertext))
        plaintext = A2_solution.d_playfair(ciphertext,key)
        print('plaintext  = {}'.format(plaintext))
        print()
    
    print('------------ Testing encrypt/decrypt over files:')
    plaintext = utilities.file_to_text('plaintext2.txt')
    ciphertext = A2_solution.e_playfair(plaintext,key)
    print()
    if ciphertext == utilities.file_to_text('ciphertext6.txt'):
        print('Encryption validated')
    else:
        print('Encryption validation failed')
    plaintext2 = A2_solution.d_playfair(ciphertext,key)
    if plaintext == plaintext2:
        print('Decryption validated')
    else:
        print('Decryption validation failed')    
    print()
    
    print('End of Task 3: Playfair Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return

    
def task4():
    print('{}'.format('-'*40))
    print("Start of Task 4: Columnar Transposition Cipher")
    print()

    print('----------- Testing get_keyOrder_columnarTrans:')
    keys = ['','r','?','RAINY?', 'dad','face','Face','apple','good day','German']
    for key in keys:
        print('Key order for {} ='.format(key),end=' ')
        keyOrder = A2_solution._get_order_ct(key)
        print(keyOrder)
    print()
    
    print('Testing Encryption/Decryption:')
    keys = ['','German','Truth Seeker']
    plaintext = utilities.file_to_text('plaintext3.txt')
    plaintexts = ['ABC','DEFENDEASTERNWALLOFTHECASTLE',plaintext]
    for i in range(len(keys)):
        print('key = ',keys[i])
        print('plaintext  =\n{}'.format(plaintexts[i]))
        ciphertext = A2_solution.e_ct(plaintexts[i],keys[i])
        print('ciphertext =\n{}'.format(ciphertext))
        plaintext2 = A2_solution.d_ct(ciphertext,keys[i])
        print('plaintext2 =\n{}'.format(plaintext2))
        print()
    
    print('End of Task 4: Columnar Transposition Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return

task1()
task2()
task3()
task4()