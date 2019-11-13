# what?

Generate brand new (random) lyrics out of the tracks that you keep in your playlists.

# installation

[Manually](https://github.com/sahib/glyr/wiki/Compiling) compile and install `glyr`.
Don't use your Linux distrubution packages manager to install `libglyr-dev` because it is probably
outdated and does not include patches to properly parse lyrics providers.

```bash
pip3 install -r requirements.txt
```

# usage

1. convert Spotify playlist to .csv file with https://github.com/watsonbox/exportify
2. fetch lyrics with `python3 lyrand.py download YOUR_CSV_FILE -o out.json`
3. randomize with `python3 lyrand.py generate out.json --max-lines=10`

# data layout

`lyrand.py download` should be feeded with .csv file that contains something like:

```
Spotify URI,Track Name,Artist Name,Album Name,Disc Number,Track Number,Track Duration (ms),Added By,Added At                            
"spotify:track:4O4xuKdvJvl7HpFlYGwudS","Replica","The xx","I See You","1","6","249000","spotify:user:XYZ","2018-12-09T18:01:18Z"      
"spotify:track:7vUHtMNMVFNT2VmHKSLiKp","Walking Home Through the Park","Aim","Flight 602","1","2","347573","spotify:user:XYZ","2018-12
-09T18:02:15Z"
```
