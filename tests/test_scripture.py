import unittest

from scripture import Scripture


class TestScripture(unittest.TestCase):

    def test_scripture_creation(self):
        scripture = Scripture(
            "Psalm 23:1",
            "The Lord is my shepherd.",
            "God takes care of me."
        )

        self.assertEqual(scripture.location, "Psalm 23:1")
        self.assertEqual(scripture.scripture, "The Lord is my shepherd.")
        self.assertEqual(scripture.meaning, "God takes care of me.")


if __name__ == "__main__":
    unittest.main()
