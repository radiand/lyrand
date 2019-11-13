from typing import List

import filters


def newline2list(raw_str: str) -> List[str]:
    return list(filter(None, raw_str.split("\n")))


def line_per_track(tracks: List[str], max_lines: int) -> List[str]:
    tracks = filters.shuffle(tracks)
    if max_lines:
        tracks = tracks[:max_lines]
    return [filters.pick_random_one(newline2list(track)) for track in tracks]


def line_per_track_syllables(tracks: List[str], max_lines: int, syllables: int) -> List[str]:
    matching = []
    for track in tracks:
        matching_in_track = filters.syllables(newline2list(track), syllables)
        if matching_in_track:
            matching.append(filters.pick_random_one(matching_in_track))
    matching = filters.shuffle(matching)
    if max_lines:
        matching = matching[:max_lines]
    return matching
