from unittest import TestCase, mock

import lang


class TestLang(TestCase):
    @mock.patch("pronouncing.rhymes")
    def test_rhymes(self, mock_rhymes):
        mock_rhymes.return_value = ["stay"]
        self.assertTrue(lang.does_rhyme("Let me stay", "You are so far away"))
        self.assertFalse(lang.does_rhyme("Random short sentence", "Should not rhyme"))
