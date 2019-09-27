from random import*
def main():
    print ("What is your name?")
    name = input()
    number = randint(1,5)
    print("Hi " + name + " the number i am thinking of is between 1 and 5.")
    number_of_guesses = 0
    max_guesses = 20
    number_of_guesses= number_of_guesses + 1
    while(number_of_guesses<=20):
        print ("Guess the number:")
        guess = input()
        if int(guess) == number:
            print ("Nooice!")
            break
        else:
            print ("Wrong!")  
main()

