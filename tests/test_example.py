import logging
from unittest import TestCase
from src.example import square
from src.example import addition

logger = logging.getLogger(__name__)


class TestExample(TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)

    def test_square_exception(self):
        self.assertEqual(square('test'), -1)

    def test_addition(self):
        self.assertEqual(addition(10), 20)

    def test_addition_exception(self):
        with self.assertRaises(TypeError):
            addition('test')
