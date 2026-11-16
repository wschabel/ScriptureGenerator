import unittest
from unittest.mock import Mock, patch

from scripture_generator import ScriptureGenerator
from scriptures import scriptures


class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = ScriptureGenerator.__new__(ScriptureGenerator)

        self.generator.scriptures = scriptures
        self.generator.category_select = Mock()
        self.generator.verse_label = Mock()
        self.generator.scripture_label = Mock()
        self.generator.meaning_label = Mock()

    def test_category_selection(self):
        self.generator.category_select.get.return_value = "Uplifting"

        result = self.generator.scrip_cat_select()

        self.assertIs(result, scriptures["uplifting_scriptures"])

    def test_generate_scripture(self):
        self.generator.category_select.get.return_value = "Teaching"

        selected = scriptures["teaching_scriptures"][0]

        with patch("scripture_generator.choice", return_value=selected):
            self.generator.generate_scripture()

        self.generator.verse_label.config.assert_called_once_with(
            text=selected.location
        )

        self.generator.scripture_label.config.assert_called_once_with(
            text=selected.scripture
        )

        self.generator.meaning_label.config.assert_called_once_with(
            text=selected.meaning
        )

    def test_empty_category(self):
        self.generator.category_select.get.return_value = "Prayer"
        self.generator.scriptures = {"prayer_scriptures": []}

        self.generator.generate_scripture()

        self.generator.verse_label.config.assert_not_called()
        self.generator.scripture_label.config.assert_not_called()
        self.generator.meaning_label.config.assert_not_called()


if __name__ == "__main__":
    unittest.main()
