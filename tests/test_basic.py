
import unittest
from nexlang import translate


class TestNexLang(unittest.TestCase):

    def test_say(self):
        result = translate('say "Hello"')
        self.assertIn('print("Hello")', result)

    def test_loop(self):
        result = translate("loop 3:")
        self.assertIn("range(3)", result)

    def test_pause(self):
        result = translate("pause 2")
        self.assertIn("time.sleep(2)", result)


if __name__ == "__main__":
    unittest.main()
