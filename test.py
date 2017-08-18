import unittest
import app


class TestApp(unittest.TestCase):

    def test_validate_player_good(self):
        value = 'xyz'
        self.assertIsInstance(app.validate_player(value), str)

    def test_validate_player_bad(self):
        value = 123
        with self.assertRaises(Exception) as context:
            app.validate_player(value)

        self.assertTrue('Please enter only string' in str(context.exception))

    def test_minimum_value_bad(self):
        value = ''
        with self.assertRaises(Exception) as context:
            app.validate_minimum_required(value)

        self.assertTrue('Please enter minimum one character for player.' in str(context.exception))

    def test_get_players_strings(self):
        value = 'z'
        player_value = 'zxczdd'
        self.assertIsInstance(app.get_players_strings(value, player_value), list)

    def test_get_valid_strings_of_player(self):
        player_value = 'zxczdd'
        self.assertIsInstance(app.get_valid_strings_of_player(player_value), list)


if __name__ == '__main__':
    unittest.main()