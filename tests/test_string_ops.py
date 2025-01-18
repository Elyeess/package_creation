import unittest
from package_creation_tutorial.string_ops import (reverse_string, 
                                                  count_vowels, 
                                                  capitalize_words)

class TestStringOps(unittest.TestCase):
    
    def test_reverse_string(self):
        """Test the reverse_string function."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("python"), "nohtyp")
        self.assertEqual(reverse_string(""), "")  # Cas d'une chaîne vide

    def test_count_vowels(self):
        """Test the count_vowels function."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels(""), 0)  # Cas d'une chaîne vide

    def test_capitalize_words(self):
        """Test the capitalize_words function."""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python programming"), "Python Programming")
        self.assertEqual(capitalize_words("summer"), "Summer")  # Correction ici

    def test_capitalize_words_failing(self):
        """Test the capitalize_words function for failing case."""
        self.assertEqual(capitalize_words("summer"), "Summer")  # Cas corrigé

if __name__ == '__main__':
    unittest.main()
