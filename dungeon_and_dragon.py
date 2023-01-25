import os
import csv
import time
import random
import logging
import logging.config

import cowsay
import pyfiglet
from stringcolor import cs

from helper.custom_types import Accounts
from package_dd.other_func import (
    dash_help,
    dash_adv,
    dash_exit,
    loading_icon,
    loading_logo
)
from package_dd.game_functions import (
    move_dragon,
    draw_map,
    allowed_direction,
    move_character,
)


logging.config.fileConfig(fname='log/log_setting.toml', disable_existing_loggers=False) # noqa E501
logger = logging.getLogger(__name__)

INTERNAL_DATABASE: Accounts = list()
USER_INFORMATION = dict()


def main():
    """
    Running the base programs
    First, the logo of the game
    Then the user information will be read from the database,
    and then the main part of the program will be executed,
    and after the database is finished, it will be rewritten
    """
    logger.info("start game")
    loading_logo()
    read_database_file()
    while True:
        os.system("clear")
        logger.info("The user is in the 'main' section")
        print("••• Main Page •••\n")
        print("Use the '-register' or '-login' command but if you need help,enter the '-help' command") # noqa E501
        command: str = input(">>>  ").casefold()
        if command == "-register":
            logger.info("The user entered the '-register' command in the 'main' section") # noqa E501
            commend = dash_register()
            if commend == "EXIT":
                dash_exit()
                break
            else:
                continue
        elif command == "-login":
            logger.info("The user entered the '-login' command in the 'main' section") # noqa E501
            command = dash_login()
            if command == "BAN":
                break
                # Other options will be added later
            elif command == "START":
                get_level()
                # play function game
                continue
            else:
                continue
        elif command == "-help":
            logger.info("The user entered the '-help' command in the 'main' section") # noqa E501
            dash_help()
            continue
        elif command == "-exit":
            logger.info("The user entered the '-exit' command in the 'main' section") # noqa E501
            dash_exit()
            break
        elif command == "-hint":
            logger.info("The user entered the '-hint' command in the 'main' section") # noqa E501
            print("Valid commands: -register -login -exit -help ")
            time.sleep(1)
        else:
            logger.info(f"the user entered an unauthorized command >>> {command} in the 'main' section") # noqa E501
            print("Use the authorized command.")
            time.sleep(1)
    write_database_file()
    os.system("clear")
    logger.info("end game")


def dash_register() -> str | None:
    """
    Creating an account that is related to the database inside\
    the program,after creation,
    the command to exit the game must be given,
    otherwise the user's information will not be saved.
    """
    while True:
        os.system("clear")
        logger.info("The user is in the 'register' section")
        print("••• Register Page •••\n")
        print("Username:")
        input_user: str = input(">>>  ").casefold()
        if input_user == "-return":
            logger.info("The user entered the '-return' command in the 'register' section") # noqa E501
            return
        elif input_user == "-exit":
            logger.info("The user entered the '-exit' command in the 'register' section") # noqa E501
            return "EXIT"
        elif input_user == "-help":
            logger.info("The user entered the '-help' command in the 'register' section") # noqa E501
            dash_help()
        elif input_user == "-hint":
            logger.info("The user entered the '-hint' command in the 'register' section") # noqa E501
            print("Valid commands: -exit -help -return")
            time.sleep(1)
        else:
            for line in INTERNAL_DATABASE:
                if line["username"] == input_user:
                    print(f"This username '{input_user}' has been used before you") # noqa E501
                    logger.info(f"'{input_user}' Duplicate username")
                    time.sleep(1)
                    os.system("clear")
                    break
            else:
                input_pass: str = input("Password: ")
                INTERNAL_DATABASE.append(dict(
                                            username=input_user,
                                            password=input_pass,
                                            wallet=50
                                            ))
                logger.info(f"'{input_user}' registered")
                write_database_file()
                read_database_file()
                loading_icon(0.12)
                print("You have successfully registered")
                time.sleep(1)
                return


def dash_login() -> str | None:
    """
    The login part that uses the program's internal database-
    that is read in the main() function
    After logging in
    The user account will be put in a dictionary and-
    we will not have anything to do with the internal database
    """
    while True:
        os.system("clear")
        logger.info("The user is in the 'login' section")
        print("••• Login Page •••\n")
        print("Username:")
        input_user: str = input(">>>  ").casefold()
        if input_user == "-return":
            logger.info("The user entered the '-return' command in the 'login' section") # noqa E501
            return
        elif input_user == "-help":
            logger.info("The user entered the '-help' command in the 'login' section") # noqa E501
            dash_help()
        elif input_user == "-hint":
            logger.info("The user entered the '-hint' command in the 'login' section") # noqa E501
            print("Valid commands: -help -return")
            time.sleep(1)
        else:
            for line in range(len(INTERNAL_DATABASE)):
                if INTERNAL_DATABASE[line]["username"] == input_user:
                    logger.info(f"{input_user}'s username is classified")
                    for count in range(1, 4):
                        os.system("clear")
                        print("••• Login Page •••\n")
                        print(f"Username: {input_user}")
                        input_pass: str = input("Password: ").casefold()
                        if INTERNAL_DATABASE[line]["password"] == input_pass:
                            loading_icon(0.2)
                            print(f"Hi,{input_user}\nYou are logged in") # noqa E501
                            USER_INFORMATION.update(dict(INTERNAL_DATABASE.pop(line))) # noqa E501
                            logger.info(f"'{input_user}' login")
                            time.sleep(1)
                            os.system("clear")
                            return "START"
                        elif INTERNAL_DATABASE[line]["password"] != input_pass:
                            print(f"Password is wrong {count}")
                            logger.info(f"'{input_user}' entered '{input_pass}' password incorrectly {count} time") # noqa E501
                            time.sleep(0.5)
                    else:
                        os.system("clear")
                        print("Sorry, you are banned :(")
                        logger.info(f"'{input_user}' banned")
                        time.sleep(1.5)
                        os.system("clear")
                        return "BAN"
            else:
                logger.info(f"{input_user} did not exist in the database")
                print(f"This username '{input_user}' is not registered")
                time.sleep(2)
                os.system("clear")


def dash_logout():
    """
    As soon as it is executed,
    the dictionary containing user account information is-
    added to the internal database
    And then the two functions that transfer-
    the internal database to the external one are executed
    """
    INTERNAL_DATABASE.append(USER_INFORMATION)
    write_database_file()
    read_database_file()


def get_level() -> None:
    """
    It is inside the loop that selects the level of the game-
    and only if return is pressed,
    the user's information is stored in the external database
    """
    while True:
        username: str = USER_INFORMATION["username"]
        password: str = USER_INFORMATION["password"]
        wallet: int = int(USER_INFORMATION["wallet"])
        os.system("clear")
        logger.info(f"{username} is in the 'level' section, wallet:{wallet}")
        print("••• Levels Page •••\n")
        print(f"{username}, you have {wallet} ₵\n")
        input_level: str = input(">>>  ").casefold()
        if input_level == "-easy":
            if wallet < 4:
                print("Coins are not enough for this level")
                print("You can use '-adv' command to see ads to get 5 coins")
                logger.info(f"{username} is not enough coin for 'level easy', wallet:{wallet}") # noqa E501
                time.sleep(1)
            else:
                wallet -= 4
                logger.info(f"{username} entered the '-easy' and lost 4 coins, wallet:{wallet}") # noqa E501
                loading_icon(0.1)
                logger.info(f"{username} inside the 'game start' page, wallet:{wallet}") # noqa E501
                game_starter(username, wallet, 4)
                logger.info(f"{username} entered the game with a counter of 1 2 3, wallet:{wallet}") # noqa E501
                easy_level(username, password, wallet)
        elif input_level == "-normal":
            if wallet < 10:
                print("Coins are not enough for this level")
                print("You can use '-adv' command to see ads to get 5 coins")
                logger.info(f"{username} is not enough coin for 'level normal', wallet:{wallet}") # noqa E501
                time.sleep(1)
            else:
                wallet -= 10
                logger.info(f"{username} entered the '-normal' and lost 10 coins, wallet:{wallet}") # noqa E501
                loading_icon(0.1)
                logger.info(f"{username} inside the 'game start' page, wallet:{wallet}") # noqa E501
                game_starter(username, wallet, 10)
                logger.info(f"{username} entered the game with a counter of 1 2 3, wallet:{wallet}") # noqa E501
                normal_level(username, password, wallet)
        elif input_level == "-hard":
            if wallet < 22:
                print("Coins are not enough for this level")
                print("You can use '-adv' command to see ads to get 5 coins")
                logger.info(f"{username} is not enough coin for 'level hard', wallet:{wallet}") # noqa E501
                time.sleep(1)
            else:
                wallet -= 22
                logger.info(f"{username} entered the '-hard' and lost 22 coins, wallet:{wallet}") # noqa E501
                loading_icon(0.1)
                logger.info(f"{username} inside the 'game start' page, wallet:{wallet}") # noqa E501
                game_starter(username, wallet, 22)
                logger.info(f"{username} entered the game with a counter of 1 2 3, wallet:{wallet}") # noqa E501
                hard_level(username, password, wallet)
        elif input_level == "-adv":
            logger.info(f"{username} entered the '-adv', wallet:{wallet}")
            wallet += dash_adv(username)
            USER_INFORMATION.update(
                                    username=username,
                                    password=password,
                                    wallet=wallet
                                    )
            print(f"{username} 5 coins have been added to your wallet!")
            time.sleep(2)
        elif input_level == "-logout":
            loading_icon(0.1)
            print(f"{username}, You are logged outs")
            logger.info(f"'{username}' entered the '-logout', wallet:{wallet}") # noqa E501
            time.sleep(2)
            dash_logout()
            return
        elif input_level == "-help":
            logger.info(f"{username} typed the '-help' command, wallet:{wallet}") # noqa E501
            dash_help()
        elif input_level == "-hint":
            logger.info(f"{username} typed the '-hint' command, wallet:{wallet}") # noqa E501
            print("Valid commands: -easy -normal -hard -logout -help -adv")
            time.sleep(2)
        else:
            logger.info(f"{username} entered an unauthorized command >>> {input_level}") # noqa E501
            print("You must give a valid command...")
            time.sleep(2)


def easy_level(user_dict: str, pass_dict: str, wallet_dict: int):
    """
    The level is easy to run. After the coin is finished,
    it enters the user's wallet and returns to the level page

    Parameters
    ----------
    user_dict : The user name that was transferred-
        from the internal database to the dictionary

    pass_dict :
        Password to update user dictionary

    wallet_dict :
        The user's wallet, which is replenished by winning it in the game

    Returns
    -------

    """
    TABLE_SIZE: int = 5
    xy_list = [(x, y) for y in range(TABLE_SIZE) for x in range(TABLE_SIZE)]
    player, dragon, dungeon = random.sample(xy_list, k=3)
    logger.info(f"{user_dict} is in the game on 'easy level', wallet:{wallet_dict}") # noqa E501
    while True:
        draw_map(player, TABLE_SIZE, xy_list)
        navigation = allowed_direction(player, TABLE_SIZE)
        move = input(f"allowed {navigation} : ")
        os.system("clear")
        if move in navigation:
            player = move_character(player, move)
            if player == dragon:
                USER_INFORMATION.update(username=user_dict,
                                        password=pass_dict,
                                        wallet=wallet_dict
                                        )
                cowsay.dragon("YOU LOSE!")
                logger.info(f"{user_dict} lost the game, wallet:{wallet_dict}")
                time.sleep(2)
                break
            elif player == dungeon:
                wallet_dict += 7
                USER_INFORMATION.update(username=user_dict,
                                        password=pass_dict,
                                        wallet=wallet_dict
                                        )
                cowsay.cow("YOU WON!")
                logger.info(f"{user_dict} won the game and received 7 coins, wallet:{wallet_dict}") # noqa E501
                print(f"\nCongratulations {user_dict}, you won 7 coins")
                time.sleep(2)
                break
        else:
            os.system("clear")


def normal_level(user_dict: str, pass_dict: str, wallet_dict: int):
    """
    The level is normal to run. After the coin is finished,
    it enters the user's wallet and returns to the level page

    Parameters
    ----------
    user_dict : The user name that was transferred-
        from the internal database to the dictionary

    pass_dict :
        Password to update user dictionary

    wallet_dict :
        The user's wallet, which is replenished by winning it in the game

    Returns
    -------

    """

    TABLE_SIZE = 8
    xy_list = [(x, y) for y in range(TABLE_SIZE) for x in range(TABLE_SIZE)]
    player, dragon, dungeon, hint = random.sample(xy_list, k=4)
    logger.info(f"{user_dict} is in the game on 'normal level', wallet:{wallet_dict}") # noqa E501
    while True:
        draw_map(player, TABLE_SIZE, xy_list, hint=hint)
        navigation = allowed_direction(player, TABLE_SIZE)
        move = input(f"allowed {navigation} : ")
        os.system("clear")
        if move in navigation:
            player = move_character(player, move)
            dragon, alarm = move_dragon(dragon, player, TABLE_SIZE)
            if player == dragon:
                USER_INFORMATION.update(username=user_dict,
                                        password=pass_dict,
                                        wallet=wallet_dict)
                cowsay.dragon("YOU LOSE!")
                logger.info(f"{user_dict} lost the game, wallet:{wallet_dict}")
                time.sleep(2)
                break
            elif player == dungeon:
                wallet_dict += 16
                USER_INFORMATION.update(username=user_dict,
                                        password=pass_dict,
                                        wallet=wallet_dict)
                cowsay.cow("YOU WON!")
                logger.info(f"{user_dict} won the game and received 16 coins, wallet:{wallet_dict}") # noqa E501
                print(f"\nCongratulations {user_dict}, you won 16 coins")
                time.sleep(2)
                break
            elif player == hint:
                hint = None
                input("Please unmute your speaker\nPress 'enter' and listen carefully") # noqa E501
                hint_dungeon(dungeon)
            if alarm == "smell":
                print(cs("!!! The dragon has smelled you !!!", "yellow"))
            elif alarm == "hearing":
                print(cs("!!! The dragon heard your footsteps !!!", "red"))
        else:
            os.system("clear")


def hard_level(user_dict: str, pass_dict: str, wallet_dict: int):
    """
    The level is hard to run. After the coin is finished,
    it enters the user's wallet and returns to the level page

    Parameters
    ----------
    user_dict : The user name that was transferred-
        from the internal database to the dictionary

    pass_dict :
        Password to update user dictionary

    wallet_dict :
        The user's wallet, which is replenished by winning it in the game

    Returns
    -------

    """

    TABLE_SIZE = 12
    xy_list = [(x, y) for y in range(TABLE_SIZE) for x in range(TABLE_SIZE)]
    player, dragon, dungeon, hint, *wall = random.sample(xy_list, k=25)
    logger.info(f"{user_dict} is in the game on 'hard level', wallet:{wallet_dict}") # noqa E501
    while True:
        draw_map(player, TABLE_SIZE, xy_list, hint=hint, wall=wall)
        navigation = allowed_direction(player, TABLE_SIZE, wall=wall)
        move = input(f"allowed {navigation} : ")
        os.system("clear")
        if move in navigation:
            player = move_character(player, move)
            dragon, alarm = move_dragon(dragon, player, TABLE_SIZE, wall=wall)
            if player == dragon:
                USER_INFORMATION.update(username=user_dict,
                                        password=pass_dict,
                                        wallet=wallet_dict)
                cowsay.dragon("YOU LOSE!")
                logger.info(f"{user_dict} lost the game, wallet:{wallet_dict}")
                time.sleep(2)
                break
            elif player == dungeon:
                wallet_dict += 40
                USER_INFORMATION.update(username=user_dict,
                                        password=pass_dict,
                                        wallet=wallet_dict)
                cowsay.cow("YOU WON!")
                logger.info(f"{user_dict} won the game and received 40 coins, wallet:{wallet_dict}") # noqa E501
                print(f"\nCongratulations {user_dict}, you won 40 coins")
                time.sleep(2)
                break
            elif player == hint:
                hint = None
                input("Please unmute your speaker\nPress 'enter' and listen carefully") # noqa E501
                hint_dungeon(dungeon)
            elif alarm == "smell":
                print(cs("!!! The dragon has smelled you !!!", "yellow"))
            elif alarm == "hearing":
                print(cs("!!! The dragon heard your footsteps !!!", "red"))
        else:
            os.system("clear")


def hint_dungeon(dungeon: tuple[int, int]):
    """
    It informs the location of the dungeon with a beep

    Parameters
    ----------
    dungeon :
        The position of the dungeon, which is a tuple type
    """
    x, y = dungeon
    file = "Beep.mp3"
    for i in range(x):
        os.system("afplay " + file)
    time.sleep(1)
    for i in range(y):
        os.system("afplay " + file)
    time.sleep(0.5)
    os.system("clear")


def game_starter(username: str, wallet: int, num: int):
    """
    Before the start of the easy level of the game,
    this part is executed and the seconds counter-
    is displayed by hitting the interval

    Parameters
    ----------
    username :
    The user name is taken from the dictionary at the top of the page
    wallet :
        Also wallet

    Returns :
        Just print
    -------

    """

    count = pyfiglet.Figlet(font='big')
    os.system("clear")
    print(f"{username}, you lost {num} ₵ from your wallet, Now you have {wallet} ₵\n") # noqa E501
    print("GAME GUIDE: You can only use 'up', 'down', 'left' and 'right'\n")
    input("if you are ready, press 'enter' on the keyboard ")
    os.system("clear")
    print(count.renderText('1'))
    time.sleep(1)
    os.system("clear")
    print(count.renderText('2'))
    time.sleep(1)
    os.system("clear")
    print(count.renderText('3'))
    time.sleep(1)
    os.system("clear")


def read_database_file():
    """
    Reading the external file of the database and transferring-
    it to the internal database of the program
    """
    logger.info("Start reading database information from 'accounts_database.csv'") # noqa E501
    with open("accounts_database.csv", "r") as myfile:
        database = csv.DictReader(myfile)
        for line in database:
            INTERNAL_DATABASE.append(line)
    logger.info("End of reading database information")


def write_database_file():
    """
    Creating a new database file with the updated information-
    of the internal database and deleting it
    """
    logger.info("Start writing database information from within the program")
    with open("accounts_database.csv", "w") as myfile:
        database = csv.DictWriter(myfile, fieldnames=["username", "password", "wallet"]) # noqa E501
        database.writeheader()
        for line in INTERNAL_DATABASE:
            database.writerow(line)
    INTERNAL_DATABASE.clear()
    logger.info("End of writing database information and saved in 'accounts_database.csv'") # noqa E501


if __name__ == "__main__":
    main()
