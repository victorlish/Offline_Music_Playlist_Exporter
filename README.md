# Offline Music Playlist Generator
Generate a M3U8 playlist from folders of song in harddrive.

## Implementation Notes
1. The program runs with python, so make sure you have python installed on your computer.
2. Copy the repo.
3. Install dependencies using `pip install -r requirements.txt`.
4. You are good to go.

## Usage
`playlist_generator.py` requires three arguements to run the program.
```
usage: playlist_generator.py [-h] path playlist {flac,wav,mp3}

positional arguments:
  path            Path of songs/music.
  playlist        Playlist name of songs/music.
  {flac,wav,mp3}  Filetype of songs/music.

optional arguments:
  -h, --help      show help message and exit
```

The program determines duplication using filename in the format of `[trackNumber] - title.[filetype]`. For instance, `01 - ABC.mp3`.

The program also requires dependency of:
```
mutagen==1.45.1
```
You may install the dependency via `pip install -r requirements.txt`.
