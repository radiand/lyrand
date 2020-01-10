import argparse
import json

from typing import List

from generators import line_per_track, line_per_track_syllables, line_per_track_rhymes
from track import Credits, Track, Verse


def newline2list(raw_str: str) -> List[str]:
    return list(filter(None, raw_str.split("\n")))


def get_args():
    ap = argparse.ArgumentParser(description="generate random lyrics out of given titles")

    ap.add_argument("input", help="path to json dump with downloaded lyrics")
    ap.add_argument("--max-lines", help="max length of output record", type=int)
    ap.add_argument("--rhymes", help="rhymes!", action="store_true")
    ap.add_argument("--syllables", help="exact number of syllables for each line", type=int)
    ap.add_argument(
        "--print-origin", help="print also artist and title of a verse", action="store_true")

    return ap.parse_args()


def print_verses(verses: List[Verse], origin: bool):
    if not origin:
        for verse in verses:
            print(verse.value)
        return

    padding = len(sorted(verses, key=lambda elem: len(elem.value), reverse=True)[0].value)

    for verse in verses:
        value = verse.value.strip().ljust(padding)  # TODO: generate.py should not sanitize strings
        print(f"{value} {verse.credits.artist} - {verse.credits.title}")


def main():
    args = get_args()

    path_in = args.input
    max_lines = args.max_lines
    rhymes = args.rhymes
    syllables = args.syllables

    with open(path_in) as f:
        data = json.load(f)
        tracks = [Track(Credits(artist=t[0], title=t[1]), newline2list(t[2])) for t in data]

        if syllables:
            result = line_per_track_syllables(tracks, syllables)
        elif rhymes:
            if max_lines and max_lines % 2 != 0:
                print("odd max-lines!")
                return
            result = line_per_track_rhymes(tracks)
        else:
            result = line_per_track(tracks)

        if args.max_lines:
            result = result[:max_lines]

        print_verses(result, args.print_origin)


if __name__ == "__main__":
    main()
