from unittest import TestCase

import filters


PHRASES = {
    # mapping: num of syllables -> phrase
    5: ["I like butterflies"],
    7: ["I like to cook spaghetti.",
        "Water will kill you one day.",
        "Oxygen is poisonous."],
}


class TestFilters(TestCase):
    def test_syllables(self):
        self.assertListEqual(PHRASES[5], filters.syllables(PHRASES[5], 5))
        self.assertListEqual(PHRASES[7], filters.syllables(PHRASES[7], 7))
        self.assertListEqual(PHRASES[5], filters.syllables(PHRASES[5] + PHRASES[7], 5))
