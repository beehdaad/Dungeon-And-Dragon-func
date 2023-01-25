import os
import time
import logging

import cowsay
import pyfiglet

logger = logging.getLogger(__name__)


def main():
    ...


def dash_help():
    """
    There is only print and input to display-
    the auxiliary information of the user

    Parameters
    ----------

    Returns
    -------

    """
    logger.info("The user is 'inside' the '-help' section")
    os.system("clear")
    print("-"*79)
    print("""
    Hello, my friend, welcome to the dragon and dungeon game!
    I am '-HELP'
    My duty is to be by your side everywhere in the game if you need help
    For this purpose, we have prepared a guide for you so that
    you don't have any problems in the process of running the game
    So stay with me...
    You need a username and password to enter the game
    If you have, enter "-login" in the input field, otherwise,
    enter "-register" and create an account for yourself.
    And if you want to leave the game for any reason,
    use the '-exit' command and you can even go back to the previous page with '-return'
    Even the '-hint' command is built in to help you
    Wherever you are in the program and you see the '>>>  ' icon,
    you can enter the desired command in it.
    After these steps, you will enter the game level setting section
    There are easy, medium and hard respectively
    For each of these levels you have to pay a coin from the wallet in your command
    And winning in each of those coin levels will be awarded to you
    By default, anyone who creates an command for
    the first time will be given 50 coins as a gift
    Now, if you don't have enough coins to run the game,
    you can get coins by watching sponsors' ads with the '-adv' command
    Don't forget to log out after entering your account
    Now we get to the start of the game
    You must use the four directions up, down, left, right to move
    the game character and you must try to reach the dungeon and escape from the dragons.
    I hope you can escape from the dragon :))
    Good luck





    This game created by
    Behdad Siavoshi
    In Dec 2022
    Version 1.2.0
    """) # noqa E501
    print("-"*79)
    input("Press 'enter' on the keyboard to exit -help ")
    os.system("clear")
    logger.info("The user of the '-help' section has 'exited'")


def dash_exit():
    """Display text for when the user wants to exit the game"""
    logger.info("The user is 'inside' the '-exit' section")
    os.system("clear")
    print("Hope To See You Again...\n")
    print("Copyright© 2022 Behdad Siavoshi\n")
    time.sleep(2)
    os.system("clear")
    logger.info("The user of the '-exit' section has 'exited'")


def dash_adv(username: str) -> int:
    """It only prints some shapes

    Parameters
    ----------
    username: str :
        The user's username inside the program

    Returns
    -------


    """
    logger.info(f"{username} is 'inside' the '-adv' section")
    os.system("clear")
    cowsay.fox(f"Hi {username}, what are you doing here?")
    time.sleep(1.3)
    os.system("clear")
    cowsay.cow("Hello dude, I had come to play Dungeons and Dragons, but I didn't have enough money") # noqa E501
    time.sleep(1.3)
    os.system("clear")
    cowsay.fox("stop saying bullshits, What did you do with your money?")
    time.sleep(1.3)
    os.system("clear")
    cowsay.cow("I gave all the money I had to Mapsa for Django boot camp")
    time.sleep(1.3)
    os.system("clear")
    cowsay.fox("Mapsa? What are you talking about?")
    time.sleep(1.3)
    os.system("clear")
    cowsay.cow("A company in the field of oil and petrochemicals, but in one of its floors, programming is taught") # noqa E501
    time.sleep(1.3)
    os.system("clear")
    cowsay.fox("serious? Good, then I will go to register")
    time.sleep(1.3)
    os.system("clear")
    cowsay.cow("good luck, Just pay your money for the boot camp first, Can you please lend me 5 coins?") # noqa E501
    time.sleep(1.3)
    os.system("clear")
    cowsay.fox("why not")
    time.sleep(1.3)
    os.system("clear")
    cowsay.cow("thank you")
    time.sleep(1.3)
    os.system("clear")
    logger.info(f"{username} of the '-adv' section has 'exited'")
    return 5


def loading_logo():
    """Show the title of the game and loading"""
    logger.info("'loading logo' being displayed")
    os.system("clear")
    TXT_PYFIGLET = pyfiglet.Figlet(font='rectangles')
    # print (TXT_PYFIGLET.renderText('Dungeon and Dragon'))
    # time.sleep(2)
    count: int = 0
    while count < 40:
        print(TXT_PYFIGLET.renderText('Dungeon and Dragon'))
        print(f"{'.'*(count)}{count}%{'.'*count}", end="")
        time.sleep(0.07)
        count += 1
        os.system("clear")
    print(TXT_PYFIGLET.renderText('Dungeon and Dragon'))
    print(f"{'.'*(40)}{100}%{'.'*(40)}", end="")
    time.sleep(0.07)
    os.system("clear")
    time.sleep(1.1)
    logger.info("'loading logo' is finished")


def loading_icon(second: float | int):
    """Loading screen

    Parameters
    ----------
    second: Union[float :
        Sets the icon display speed,
        which can be either a decimal number or a fixed number
    int] :


    Returns
    -------


    """
    logger.info("'loading logo' being displayed")
    os.system("clear")
    count: int = 0
    while count < 3:
        print("Loading.")
        time.sleep(second)
        os.system("clear")
        print("Loading..")
        time.sleep(second)
        os.system("clear")
        print("Loading...")
        time.sleep(second)
        os.system("clear")
        count += 1
    logger.info("'loading logo' is finished")


if __name__ == "__main__":
    ...
