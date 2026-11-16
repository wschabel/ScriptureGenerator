import unittest

from scripture import Scripture
from scriptures import scriptures


class TestScriptures(unittest.TestCase):

    def test_categories_exist(self):
        self.assertIn("uplifting_scriptures", scriptures)
        self.assertIn("teaching_scriptures", scriptures)
        self.assertIn("prayer_scriptures", scriptures)

    def test_category_counts(self):
        for category, items in scriptures.items():
            with self.subTest(category=category):
                self.assertEqual(len(items), 30)

    def test_scripture_objects(self):
        for category, items in scriptures.items():
            for item in items:
                with self.subTest(category=category, location=item.location):
                    self.assertIsInstance(item, Scripture)

    def test_scripture_fields_not_empty(self):
        for category, items in scriptures.items():
            for item in items:
                with self.subTest(category=category, location=item.location):
                    self.assertTrue(item.location.strip())
                    self.assertTrue(item.scripture.strip())
                    self.assertTrue(item.meaning.strip())


if __name__ == "__main__":
    unittest.main()
