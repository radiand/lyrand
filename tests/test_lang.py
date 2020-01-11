from unittest import TestCase, mock

from lyrand import lang


class TestLang(TestCase):
    @mock.patch("pronouncing.rhymes")
    def test_rhymes(self, mock_rhymes):
        mock_rhymes.return_value = ["stay"]
        self.assertTrue(lang.does_rhyme("Let me stay", "You are so far away"))
        self.assertFalse(lang.does_rhyme("Random short sentence", "Should not rhyme"))

        mock_rhymes.return_value = ["x", "y"]
        self.assertTrue(lang.does_rhyme("x", "y"))
        self.assertTrue(lang.does_rhyme("y", "x"))
        self.assertTrue(lang.does_rhyme("A B C x", "D E F y"))
