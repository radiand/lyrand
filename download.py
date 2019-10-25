import multiprocessing
import plyr


def fetch_track_lyrics(artist, title):
    query = plyr.Query(artist=artist, title=title, get_type="lyrics")
    items = query.commit()
    if not items:
        print("ERROR: {} - {} has no lyrics".format(artist, title))
        return None
    decoded = items[0].data.decode("utf-8")
    if decoded == "Instrumental":
        print("{} - {} is instrumental".format(artist, title))
        return None
    return decoded


def fetch_track_lyrics_worker(artist, title, storage):
    lyrics = fetch_track_lyrics(artist, title)
    if lyrics:
        storage.append((artist, title, lyrics))


def sanitize(txt):
    return txt.split("-")[0]


def download_lyrics(tracks):
    manager = multiprocessing.Manager()
    lyrics = manager.list()

    processes = []

    for artist, title in tracks:
        p = multiprocessing.Process(target=fetch_track_lyrics_worker, args=(artist, title, lyrics))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return list(lyrics)
