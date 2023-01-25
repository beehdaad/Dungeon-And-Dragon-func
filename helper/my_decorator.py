import os
import logging


def main():
    """ """
    ...


def clear_terminal(func):
    """
    Receives a function and cleans the terminal first and last

    Parameters
    ----------
    func :
        Any function

    Returns
    -------

    """
    def wrapper():
        """ """
        os.system("clear")
        func()
        os.system("clear")
    return wrapper


def debugging_function(func):
    """
    If the function encounters an error, it will log us

    Parameters
    ----------
    func :
        Any function

    Returns
    -------

    """
    def wrapper():
        """ """
        try:
            func()
        except Exception as e:
            logging.error(e, exc_info=True)
    return wrapper


if __name__ == "__main__":
    main()
