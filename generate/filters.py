import random
import re

from typing import Any, Dict, List, Tuple

from lang import count_syllables, does_rhyme
from track import Track, Verse


def pick_random_one(container: List[Any]) -> Any:
    return random.choice(container)


def pick_random_key_and_value(d: Dict[Any, List[Any]]) -> Tuple[Any, List[Any]]:
    key = random.choice(list(d.keys()))
    return key, d[key]


def shuffle(lines: List) -> List:
    return random.sample(lines, len(lines))


def syllables(lines: List[str], num_syllables: int) -> List[str]:
    filtered = []
    for line in lines:
        if sum([count_syllables(w) for w in re.findall(r"\w+", line)]) == num_syllables:
            filtered.append(line)
    return filtered


def rhymes(tracks: List[Track], limit=10) -> List[Dict[Verse, List[Verse]]]:
    """ Given
        `tracks`, which is a list of lists of lines in track
       returns
        list of dicts, wherein key is a line from specific track, and value is a list of lines that
        come from any other track and rhyme."""

    def without(index: int, l: List) -> List:
        return l[:index] + l[index + 1:]

    matches = []
    print("processing tracks in search for rhymes...")
    for t, track in enumerate(tracks):
        print(f"[{t+1}/{len(tracks)}] {track.credits.artist} - {track.credits.title}")
        matches_in_track = {}
        for l, line in enumerate(track.lyrics):
            line_matches = []
            for wtrack in without(t, tracks):
                rhyme_ctr = 0
                for wline in wtrack.lyrics:
                    if does_rhyme(line, wline):
                        line_matches.append(Verse(credits=wtrack.credits, value=wline))
                        rhyme_ctr += 1
                    if limit and rhyme_ctr >= limit:
                        break
            if line_matches:
                matches_in_track[Verse(credits=track.credits, value=line)] = line_matches
        if matches_in_track:
            matches.append(matches_in_track)
    return matches
