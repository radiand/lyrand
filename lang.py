import re

import pronouncing


def count_syllables(word: str) -> int:
    """Shamelessly stolen from:
    https://stackoverflow.com/a/46759549"""

    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count


def does_rhyme(lhs_line: str, rhs_line: str) -> bool:
    last_word = lambda line: re.findall(r"\w+", line)[-1]  # noqa: E731
    return last_word(lhs_line) in pronouncing.rhymes(last_word(rhs_line))
