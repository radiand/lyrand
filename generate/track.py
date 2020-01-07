from typing import List, NamedTuple


Credits = NamedTuple("Credits", [("artist", str), ("title", str)])
Track = NamedTuple("Track", [("credits", Credits), ("lyrics", List[str])])
