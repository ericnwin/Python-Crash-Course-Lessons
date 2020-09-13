import unittest
from full_name import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """ Tests for get_formatted_name properly outputs a full name"""

    def test_full_name(self):
        full_name = get_formatted_name("eric", "nguyen")
        self.assertEqual(full_name, "Eric Nguyen")

    def test_full_name_middle(self):
        full_name = get_formatted_name("captain", "falcon", 'g')
        self.assertEqual(full_name, "Captain G Falcon")


if __name__ == '__main__':
    unittest.main()
