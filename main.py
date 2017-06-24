import random
list_of_names = []


def main():
    generate_players_list(create_number_of_players())
    set_players_order()
    players_game()
    return 0


def create_number_of_players():
    number_of_players = int(raw_input("Please, choose number of players "))
    check_number_of_players(number_of_players)
    return number_of_players


def check_number_of_players(number_of_players):
    if 2 <= number_of_players <= 6:
        print"Number of players is ", number_of_players
    else:
        print"Number of players is not from two to six "
        create_number_of_players()
    return number_of_players


def create_name():
    name = raw_input("Please, type name of player ")
    return name


def generate_players_list(number_of_players):
    for player in range(number_of_players):
        list_of_names.append(create_name())


def set_players_order():
    random.shuffle(list_of_names)


def through_dice():
    return random.randint(1, 6)


def players_game():
    while True:
        for player_name in list_of_names:
            print player_name, (through_dice(), through_dice())



main()


