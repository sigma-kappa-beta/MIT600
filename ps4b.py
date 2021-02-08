# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
word_set = load_words(WORDLIST_FILENAME)
story = get_story_string()


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        
        
        
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text.copy()
        
        
        
       
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy() 
    
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                  another letter (string). 
        '''
        self.shift_dict = {}
        self.lower_l = string.ascii_lowercase
        self.upper_l = string.ascii_uppercase
        
        for self.i in range(len(self.lower_l)):
            if self.i + shift <= 25:
                self.shift_dict[self.lower_l[self.i]] = self.lower_l[self.i+shift]
            else:           
                self.shift_dict[self.lower_l[self.i]] = self.lower_l[(26 - (self.i+shift))*-1]
       
        for self.x in range(len(self.upper_l)):
            if self.x + shift <= 25:          
                self.shift_dict[self.upper_l[self.x]] = self.upper_l[self.x+shift]
            else:
                self.shift_dict[self.upper_l[self.x]] = self.upper_l[(26 - (self.x+shift))*-1]
   
   
        return(self.shift_dict)
    
           
                

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        self.cipher = self.build_shift_dict(shift)
        self.encripted_list =[]
        for self.i in self.message_text:
            if self.i not in self.cipher:
                self.encripted_list.append(self.i)
            else:
                self.encripted_list.append(self.cipher[self.i])
        self.message_text_encrypted = ''.join(self.encripted_list)
        return self.message_text_encrypted


            
        
                
            

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        self.message_text = text
        self.message_text_encrypted = text
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)
       


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted
      

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        # self.valid_words = load_words(WORDLIST_FILENAME)
        self.final_max = 0
        self.decrypted_message = ""
        self.max_index = 0
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        for self.index in range(26):
            self.to_be_decrypted = self.apply_shift(self.index)
            self.checklist = str.split(self.to_be_decrypted)
            for self.l_index in self.checklist:
                self.wordn = 0
                if is_word(word_set, self.l_index) == True:
                    self.wordn +=1
                else:
                    continue
            self.prelim_max = self.wordn
            if self.prelim_max > self.final_max:
                self.final_max = self.prelim_max
                self.decrypted_message = self.to_be_decrypted
                self.max_index = self.index
            else:
                continue
        return (self.max_index, self.decrypted_message)
                

if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
    # plaintext = PlaintextMessage('hello', 2)
    # print('Expected Output: jgnnq')
    # print('Actual Output:', plaintext.get_message_text_encrypted())
#
    #Example test case (CiphertextMessage)
    # ciphertext = CiphertextMessage('jgnnq')
    # print('Expected Output:', (24, 'hello'))
    # print('Actual Output:', ciphertext.decrypt_message())
    
    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage(story)
   
    print('Actual Output:', ciphertext.decrypt_message())


    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    pass #delete this line and replace with your code here
