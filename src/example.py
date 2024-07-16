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
    except TypeError:
        logger.error(f"Data must be an integer, got {type(data)}")
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
    return data + 10
