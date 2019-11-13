import random
import re

from typing import List

from lang import count_syllables


def pick_random_one(lines: List[str]) -> str:
    return lines[random.randint(0, len(lines) - 1)]


def shuffle(lines: List[str]) -> List[str]:
    return random.sample(lines, len(lines))


def syllables(lines: List[str], num_syllables: int) -> List[str]:
    filtered = []

    for line in lines:
        syllables_in_line = 0
        # list comprehension to remove empty strings
        for word in [w for w in re.split(r"\W+", line) if w]:
            syllables_in_line += count_syllables(word)
            if syllables_in_line > num_syllables:
                break
        if syllables_in_line == num_syllables:
            filtered.append(line)

    return filtered
