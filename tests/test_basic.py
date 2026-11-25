import unittest

from nexlang import translate, show, roll, inside


class TestNexLang(unittest.TestCase):

    def test_repeat_keyword(self):
        code = translate("repeat 3:\n    show('Hi')")
        self.assertIn("for _nexlang_i in range(3):", code)

    def test_when_keyword(self):
        code = translate("when 5 > 2:\n    show('Yes')")
        self.assertIn("if 5 > 2:", code)

    def test_otherwise_keyword(self):
        code = translate(
            "when 5 > 2:\n"
            "    show('Yes')\n"
            "otherwise:\n"
            "    show('No')"
        )
        self.assertIn("else:", code)

    def test_unless_keyword(self):
        code = translate("unless ready:\n    show('Wait')")
        self.assertIn("if not (ready):", code)

    def test_forever_keyword(self):
        code = translate("forever:\n    show('Running')")
        self.assertIn("while True:", code)

    def test_show_function(self):
        self.assertIsNone(show("Testing NexLang"))

    def test_roll_function(self):
        result = roll(1, 10)
        self.assertTrue(1 <= result <= 10)

    def test_inside_function(self):
        self.assertTrue(inside(5, 1, 10))
        self.assertFalse(inside(15, 1, 10))


if __name__ == "__main__":
    unittest.main()