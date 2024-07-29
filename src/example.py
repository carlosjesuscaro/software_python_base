import logging

logger = logging.getLogger(__name__)


class CustomError(Exception):
    pass


def square(data: int) -> int:
    """Returns the square value of an integer
    Args:
        data (int): The data to be squared
    Returns:
        int: The squared value of data
    Raises
        None. The TYpeError is caught with a try-except block
    """
    try:
        squared = data ** 2
        logger.info(f'The square of {data} is {squared}')
        return squared
    except Exception as error:
        logger.error(f"Data must be an integer, got {type(data)}")
        logger.error(f'An exception has occurred: {type(error).__name__}')
        return -1


def addition(data: int) -> int:
    """Returns the square value of an integer
    Args:
        data (int): The data to be squared
    Returns:
        int: The squared value of data
    Raises
        TypeError: If the data is not an integer
    """
    try:
        return data + 10
    except Exception as error:
        logger.error(f"An error has occurred: {type(error).__name__}")
