import random

def choose_options():
    user_option = input("Elige piedra, papel o tijera => ")
    user_option = user_option.lower()
    options = ("piedra", "papel", "tijera")
    
    if not user_option in options:
        print("Esa opción no es válida")
        #continue
        return None, None

    computer_option = random.choice(options)

    print("User option: ", user_option)
    print("Computer option: ", computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins ):
    if user_option == computer_option:
            print("Empate")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra gana")
            print("Ganaste")
            user_wins += 1
        else:
            print("Tijera gana")
            print("Perdiste")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Gana papel")
            print("Ganaste")
            user_wins += 1
        else:
            print("Tijera gana")
            print("Perdiste")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana")
            print("Ganaste")
            user_wins += 1
        else:
            print("Piedra gana")
            print("Perdiste")
            computer_wins += 1
    return user_wins,computer_wins

def check_winner(user_wins, computer_wins):
    if computer_wins == 2:
        print("El rotundo ganador es la computadora")
        exit()
    if user_wins == 2:
        print("El rotundo ganador eres tú")
        exit()
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:

        print("*" * 10)
        print("Round", rounds)

        print("Computer wins ", computer_wins)
        print("User wins ", user_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        check_winner(user_wins, computer_wins)

    


run_game()

    

        