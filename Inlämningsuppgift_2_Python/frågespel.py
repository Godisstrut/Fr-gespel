win = 0
lose = 0

"""Huvudfunktionen som köra alla funktioner"""
def main():
    welcome()
    options()

"""Välkommnar och frågor användaren om deras namn """
def welcome():
    print("-"*30)
    name = input(" Välkommen till mitt fina frågespel! Hur var ditt namn? ")
    print("-"*30)
    print(f" Välkommen {name} !")


def menu():
    print( " här nedanför har du dina val ")
    print(" Meny ")
    print("-"*30)
    print(" Val ")
    print("1. Frågespel ")
    print("2. Statistik ")
    print("3. Avsluta ")

def options():
    while True:
        menu()
        user_choice = input(" Val: ")

        if user_choice == "1":
            print( "Du valde att spela frågespelet ")
            intro()
            question_game()
        elif user_choice == "2":
            print( "Du valde visa statistik ")
            statistics()
        elif user_choice == "3":
            print( "Du valde att avsluta spelet, hejdå! ")
            break
        else: print(" Du valde inte ett giltigt alternativ, vänligen försök igen ")


def intro():
    print("*"*30)
    print( " Då kör vi! ")
    print("*"*30)

def question_game():
    question( "Vilken är Sveriges huvudstad? ", "Stockholm")
    question( "Vilket band släppte succé albumet Abbey road? ", "The beatles")
    question( "Vem har skapat hit spelet League of legends? ", "Riot games")
    

def question(question, answer):
    global win
    global lose
    while True:
        print(question)
        user_answer = input(" Ditt svar: ")
        if user_answer == answer:
            print(" Helt rätt! Snyggt jobbat! ")
            win +=1
            return True
        else: 
            print( " Tyvärr fel svarat, vänligen försök igen! ")
            lose +=1
        
def statistics():
    print("*"*30)
    print(" Välkommen till statistik delen! ")
    print("*"*30)
    print( " Du har svarat på " + str(win) + " frågor ")
    print( " Och du har svarat fel på " + str(lose) + " frågor ")
    

main()