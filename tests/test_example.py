import logging
from src.example import square

logger = logging.getLogger(__name__)


def test_square():
    assert square(2) == 4
