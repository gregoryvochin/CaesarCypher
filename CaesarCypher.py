import DoubleAlphabet

def caesar(word, shift, direction):  # define cypher function
    alphabet = DoubleAlphabet.alphabet
    output = ""  # initialize output string
    word = word.lower()  # normalize input to lowercase characters
        
    if direction == "encode" or direction == "decode":
        if direction == "decode":
                shift *= -1
                
        for char in word:
            char_position = alphabet.index(char)
            new_position = char_position + shift
            output += alphabet[new_position]
        print("\nYour mesage is: \n" + output + "\n")

    else:
        return "Please enter either 'encode' or 'decode'."
