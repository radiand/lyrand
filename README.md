# what?

Generate brand new (random) lyrics out of the tracks that you keep in your playlists.

# installation

```bash
pip3 install cython
pip3 install -r requirements.txt
```

# usage

1. convert Spotify playlist to .csv file with https://github.com/watsonbox/exportify
2. fetch lyrics with `python3 lyrand.py download YOUR_CSV_FILE -o out.json`
3. randomize with `python3 lyrand.py generate out.json --max-lines=10`
