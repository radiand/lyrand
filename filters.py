import random
import re

from typing import List

from lang import count_syllables


def pick_random_one(lines: List[str]) -> str:
    return lines[random.randint(0, len(lines) - 1)]


def shuffle(lines: List) -> List:
    return random.sample(lines, len(lines))


def syllables(lines: List[str], num_syllables: int) -> List[str]:
    filtered = []
    for line in lines:
        if sum([count_syllables(w) for w in re.findall(r"\w+", line)]) == num_syllables:
            filtered.append(line)
    return filtered


def rhymes(tracks: List[List[str]]):
    pass
