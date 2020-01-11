from typing import List, NamedTuple


Credits = NamedTuple("Credits", [("artist", str), ("title", str)])
Verse = NamedTuple("Verse", [("credits", Credits), ("value", str)])
Track = NamedTuple("Track", [("credits", Credits), ("lyrics", List[str])])
