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
        TypeError: If the data is not an integer
    """
    try:
        squared = data ** 2
        logging.info(f'The square of {data} is {squared}')
        return squared
    except TypeError:
        logging.error(f"Data must be an integer, got {type(data)}")
