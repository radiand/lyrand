import filters


def line_per_track(tracks, max_lines):
    tracks = filters.shuffle(tracks)
    if max_lines:
        tracks = tracks[:max_lines]
    return [filters.pick_random_one(list(filter(None, track.split("\n")))) for track in tracks]

