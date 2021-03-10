import CaesarCypher

user_continue = True  # asks user if they would like to continue running the program

while user_continue is True:  # run program until user decides to exit
    word = input("\nType your message: \n")
    shift = int(input("Enter your shift number: \n"))
    direction = input("'encode' or 'decode': \n")

    CaesarCypher.caesar(word, shift, direction)

    yes_or_no = input("Type 'yes' to go again, or 'no' to end the program: ")
    if yes_or_no == "no":
        user_continue = False
