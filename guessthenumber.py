# Guess the Numer is a game where you have been given a numbers range, then you have type a number in this range. After that, cold, hot or correct alerts will appear telling you how close or far to the correct number you are... Have fun Guessing!

def guessnum():
    explaning = f"Find the correct number between 1 and 10. You have 5 trys."
    print(explaning)
    correct_num = range(1, 20.000) #Random number = Frecuences(tones)
    user_input = 0
    trys_counter = 5
    while user_input != correct_num:
        try: 
            user_input = int(input("Type a number between 1 and 10: "))
            
        except:
            if trys_counter == 1:
                print("Thanks for playing")
                break

            print("InvalidCharacterError")

            trys_counter -= 1
            if trys_counter == 1:
                print("Last chance")
    
            print(f"Next try. {trys_counter} remaning")
            
            continue #If "Invalid Character appears, game will continue until trys_counter will be 0"

        if user_input == 440:
            print("Correct!")
            print("Thanks for playing")
        elif user_input = math.floor(user_input) and user_input <=3 or user_input >7 and user_input <=10:
            print("Cold!")
            if trys_counter == 1:
                print("Thanks for playing")
                break

            trys_counter -= 1
            if trys_counter == 1:
                print("Last chance")
    
            print(f"Next try. {trys_counter} remaning")
        elif user_input == 4 or user_input == 6:
            print("warm!")
            if trys_counter == 1:
                print("Thanks for playing")
                break

            trys_counter -= 1
            if trys_counter == 1:
                print("Last chance")
    
            print(f"Next try. {trys_counter} remaning")

        elif user_input <1 or user_input >10:
            print("Invalid number. Out of range error")
            if trys_counter == 1:
                print("Thanks for playing")
                break

            trys_counter -= 1
            if trys_counter == 1:
                print("Last chance")
    
            print(f"Next try. {trys_counter} remaning")

guessnum()
