import unittest

import bot_feedback


class Bot_feedbackTestCase(unittest.TestCase):

    def setUp(self):
        self.app = bot_feedback.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to bot_feedback', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
