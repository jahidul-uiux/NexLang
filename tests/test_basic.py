
import unittest
from unittest.mock import patch
from io import StringIO

from nexlang import translate, show, ask, pause, roll, inside


class TestNexLang(unittest.TestCase):

    # Five custom keyword tests

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

    # Five built-in function tests

    def test_show_function(self):
        output = StringIO()
        with patch("sys.stdout", output):
            show("Hello NexLang")
        self.assertEqual(output.getvalue(), "Hello NexLang\n")

    def test_ask_function(self):
        with patch("builtins.input", return_value="Jahid"):
            result = ask("Enter name: ")
        self.assertEqual(result, "Jahid")

    def test_pause_function(self):
        with patch("nexlang.time.sleep") as mock_sleep:
            pause(2)
        mock_sleep.assert_called_once_with(2.0)

    def test_roll_function(self):
        result = roll(1, 10)
        self.assertTrue(1 <= result <= 10)

    def test_inside_function(self):
        self.assertTrue(inside(5, 1, 10))
        self.assertFalse(inside(15, 1, 10))

    # Nested block test

    def test_nested_blocks(self):
        code = translate(
            "repeat 2:\n"
            "    when 5 > 2:\n"
            "        show('Nested')"
        )

        self.assertIn("for _nexlang_i in range(2):", code)
        self.assertIn("if 5 > 2:", code)
        self.assertIn("        show('Nested')", code)


if __name__ == "__main__":
    unittest.main(verbosity=2)
