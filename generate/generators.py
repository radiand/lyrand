from typing import List

import filters


def line_per_track(tracks: List[List[str]]) -> List[str]:
    """Takes only one, randomly chosen line from each track."""
    tracks = filters.shuffle(tracks)
    return [filters.pick_random_one(track) for track in tracks]


def line_per_track_syllables(tracks: List[List[str]], syllables: int) -> List[str]:
    """Filters lines that have given number of syllables, and takes randomly chosen
    one from each track."""
    matching = []
    for track in tracks:
        matching_in_track = filters.syllables(track, syllables)
        if matching_in_track:
            matching.append(filters.pick_random_one(matching_in_track))
    matching = filters.shuffle(matching)
    return matching


def line_per_track_rhymes(tracks: List[List[str]]) -> List[str]:
    rhymes = filters.rhymes(tracks, mark_source=False)
    result = []
    for track in rhymes:
        d = filters.pick_random_one_dict(track)
        result.append(d[0])
        result.append(filters.pick_random_one(d[1]))
    return result
