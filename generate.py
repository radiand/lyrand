import random


def random_line(lines):
    return lines[random.randint(0, len(lines) - 1)]


def line_per_track(tracks, max_lines):
    random.shuffle(tracks)
    if max_lines:
        tracks = tracks[:max_lines]
    return [random_line(list(filter(None, track.split("\n")))) for track in tracks]
