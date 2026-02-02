

#Main function
def check_word():

    '''
    This function can check if your word is a palindrome or not
    '''

    word = str(input("Please Enter your word: ")).lower()
    reversed_word = list(word)
    original_word = list(word)
    reverse_word = reversed_word.reverse()
    
    if reversed_word == original_word:
        print("The string is a palindrome.")
    elif reversed_word != original_word:
        print("The string is not a palindrome.")        


#Run the program
if __name__ == "__main__":
    check_word()