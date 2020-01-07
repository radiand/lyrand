from unittest import TestCase, mock

import filters
from track import Credits, Track


PHRASES = {
    # mapping: num of syllables -> phrase
    5: ["I like butterflies"],
    7: ["I like to cook spaghetti.",
        "Water will kill you one day.",
        "Oxygen is poisonous."],
}


def make_track(lyrics):
    return Track(Credits(artist="artist", title="title"), lyrics=lyrics)


class TestFilters(TestCase):
    def test_syllables(self):
        self.assertListEqual(PHRASES[5], filters.syllables(PHRASES[5], 5))
        self.assertListEqual(PHRASES[7], filters.syllables(PHRASES[7], 7))
        self.assertListEqual(PHRASES[5], filters.syllables(PHRASES[5] + PHRASES[7], 5))

    @mock.patch("lang.does_rhyme")
    def test_rhymes_do_not_return_empty_lists(self, mock_does_rhyme):
        mock_does_rhyme.return_value = False
        lyrics = [
            [
                "track_1 line_1",
                "track_1 line_2"
            ],
            [
                "track_2 line_1",
                "track_2 line_2"
            ],
        ]
        tracks = [make_track(l) for l in lyrics]

        self.assertListEqual(filters.rhymes(tracks), [])

