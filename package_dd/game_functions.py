import math
import random
import logging
from typing import Tuple

logger = logging.getLogger("game")


def main():
    """ """
    ...


def draw_map(
            player: Tuple[int, int],
            table: int,
            range_list: list[Tuple[int, int]],
            dragon: Tuple = None,
            hint: Tuple = None,
            wall: Tuple = []
            ):
    """Prints the game map

    Parameters
    ----------
    character: Tuple[int : x
        Player coordinates
    int] :
        y
    table: int :
        Table dimensions
    range_list: List[Tuple[int :
        All the coordinates of the table
    int]] :
    dragon: Tuple : Coordinates of dragon
        (Default value = None)
    hint: Tuple : Coordinates of hint
        (Default value = None)
    wall: Tuple : Coordinates of walls
        (Default value = [])

    Returns
    -------
    """
    logger.info(f"Player position: {player}")
    print("-"*((table*3) + 2))
    for item in range_list:
        x, y = item
        if x == 0:
            print("|", end="")
        if item == player:
            print(" 유", end="")
        elif item == dragon:
            print(" D ", end="")
        elif item == hint:
            print(" ? ", end="")
        elif item in wall:
            print(" ▒ ", end="")
        else:
            print("   ", end="")
        if x == (table-1):
            print("|")
            if y != (table-1):
                print("-"+" "*(table*3)+"-")
    print("-"*((table*3) + 2))
    logger.info("The map was drawn")


def allowed_direction(player: Tuple[int, int], table, wall=[]) -> list:
    """

    Parameters
    ----------
    player: Tuple[int :
        Player coordinates
    int] :

    table :
        Table dimensions

    wall :
        Coordinates of walls
        (Default value = [])

    Returns:
        Allowed directions
    -------

    """
    NAVIGATION = ["up", "down", "left", "right"]
    x_line, y_column = player
    if x_line == table-1:
        NAVIGATION.remove("right")
    if y_column == table-1:
        NAVIGATION.remove("down")
    if y_column == 0:
        NAVIGATION.remove("up")
    if x_line == 0:
        NAVIGATION.remove("left")
    if (x_line+1, y_column) in wall:
        NAVIGATION.remove("right")
    if (x_line-1, y_column) in wall:
        NAVIGATION.remove("left")
    if (x_line, y_column-1) in wall:
        NAVIGATION.remove("up")
    if (x_line, y_column+1) in wall:
        NAVIGATION.remove("down")
    logger.info(f"Allowed directions: {NAVIGATION}")
    return NAVIGATION


def move_character(character: Tuple[int, int], move: str):
    """
    Parameters
    ----------
    character: Tuple[int :
        Coordinates of player
    int] : number

    move: str :
        Choose a direction
    Returns:
        Changed character position
    -------
    """
    x_line, y_column = character
    if move == "up":
        y_column -= 1
        logger.info("The character chose 'UP'")
    elif move == "down":
        y_column += 1
        logger.info("The character chose 'DOWN'")
    elif move == "left":
        x_line -= 1
        logger.info("The character chose 'LEFT'")
    elif move == "right":
        x_line += 1
        logger.info("The character chose 'RIGHT'")
    return (x_line, y_column)


def move_dragon(
                dragon: Tuple[int, int],
                player: Tuple[int, int],
                table,
                wall=[]
                ):
    """

    Parameters
    ----------
    dragon: Tuple[int :
        Coordinates of dragon
    int] :

    player: Tuple[int :
        player Coordinates
    table :
        Table dimensions
    wall :
        Coordinates of walls
        (Default value = [])

    Returns:
        Changed position of the dragon and reversed the smell or hearing word
    -------

    """
    NAVIGATION = allowed_direction(dragon, table, wall)
    x_player, y_player = player
    x_dragon, y_dragon = dragon
    if math.dist(player, dragon) <= 2:
        if y_player == y_dragon and "left" in NAVIGATION and x_player < x_dragon: # noqa E501
            logger.info(f"Dragon position: {dragon} and left direction")
            return move_character(dragon, "left"), "hearing"
        elif y_player == y_dragon and "right" in NAVIGATION and x_player > x_dragon: # noqa E501
            logger.info(f"Dragon position: {dragon} and right direction")
            return move_character(dragon, "right"), "hearing"
        elif x_player == x_dragon and "up" in NAVIGATION and y_player < y_dragon: # noqa E501
            logger.info(f"Dragon position: {dragon} and up direction")
            return move_character(dragon, "up"), "hearing"
        elif x_player == x_dragon and "down" in NAVIGATION and y_player > y_dragon: # noqa E501
            logger.info(f"Dragon position: {dragon} and down direction")
            return move_character(dragon, "down"), "hearing"
        else:
            move = random.choice(NAVIGATION)
            logger.info(f"Dragon position: {dragon} and deciding direction")
            return move_character(dragon, move), "hearing"
    elif math.dist(player, dragon) <= 4:
        move = random.choice(NAVIGATION)
        logger.info(f"Dragon position: {dragon} and deciding direction")
        return move_character(dragon, move), "smell"
    else:
        logger.info(f"Dragon position: {dragon} and did not move")
        return dragon, None


if __name__ == "__main__":
    ...
