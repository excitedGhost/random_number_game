import random

help_values = ("help", "?")
exit_values = ("gu", "exit", "quit", "giveup")
helpmsg = '''Need help?
Guess the number. That simple. You set the range for guessing. It goes without saying that the larger the range, the more difficult.
If you think you've got enough luck... I dare you to do so in 3 tries. *smirk'''

def guess_num_func(start_num, end_num):
    give_up_count = 0
    #Random Number Generator
    random_number = random.randrange(start_num,end_num)


    user_guess = input("Guess the number between " + str(start_num) + " and " + str(end_num) + ": ")#Asks the user for input
    #Checks if guess num is true
    while True:
        if user_guess.isdigit():#Checks if can be converted to num safely
            if int(user_guess) == random_number:
                print("Congratulations, You have guessed correctly!")
                print("The number is " + str(random_number))
                break
            else:
                user_guess = input("Try Again: ")
        elif user_guess in exit_values:
                print("You couldn't guess the number")
                print("Better Luck Next Time")
                break
        elif user_guess in help_values:
            print(helpmsg)
        else:
            give_up_count += 1
            if give_up_count%3 == 0:
                user_guess = input("Enter Valid Input[If you want to give up type `giveup`,`exit`, `gu` or `quit` or press Ctrl+C]: ")
            else:
                user_guess = input("Enter Valid Input: ")

while True:
    print('''   Written by Zetsubou.
        Type `help` or `?` for help''')
    try:
        start_num = input("Enter Beginning of Range: ")
        end_num = input("Enter End of Range: ")
        guess_num_func(int(start_num),int(end_num))
    except ValueError:
        if start_num in exit_values or end_num in exit_values:
            break
        elif start_num in help_values or end_num in help_values:
            print(helpmsg)
        else:
            print("An error has occured")