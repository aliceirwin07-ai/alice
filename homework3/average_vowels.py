# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

def counting_vowels_and_consonants(string):
    vowels=set("aeiou") #say what vowels are
    consonants = set("bcdfghjklmnpqrstvwxyz")   #say what consonants are
    numvow=0  
    numcons=0
    for i in range(len(string)):    #loop through string
        if string[i] in vowels: #check if it's a vowel
            numvow+=1
        elif string[i] in consonants:   #check if it's a consonant
            numcons+=1
    return (numvow,numcons)

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph):
    numsentences=0 
    punctuation = set(".?!")    #declare what punctuation i care about
    for i in range(len(paragraph)): #loop through the string
        if paragraph[i] in punctuation: #check if the current part of the string is a . or ? or ! cuz that means end of a sentence
            numsentences+=1 #add 1 to number of sentences
    avgvow=counting_vowels_and_consonants(paragraph)[0]/(len(paragraph)-numsentences)   #formula for average
    avgcons=counting_vowels_and_consonants(paragraph)[1]/(len(paragraph)-numsentences) #the number of letters in the paragraph is the length of it minus the number of punctuation marks
    return(numsentences,avgvow,avgcons)


# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

print(f"Number of sentences: {average_vowels_and_consonants(paragraph)[0]}")
print(f"Average vowels per sentence: {average_vowels_and_consonants(paragraph)[1]}")
print(f"Average consonants per sentence: {average_vowels_and_consonants(paragraph)[2]}")