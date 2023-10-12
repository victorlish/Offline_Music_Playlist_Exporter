import glob
import argparse
import os.path
import mutagen

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path of songs/music.")
    parser.add_argument("playlist", help="Playlist name of songs/music.")
    parser.add_argument("filetype", choices=['flac', 'wav', 'mp3'], help="Filetype of songs/music.")

    args = parser.parse_args()
    src = args.path
    lst = args.playlist
    filetype = args.filetype

    print("The program wish to process a playlist with the filename in the format of '00 - SongName.flac'.")
    checkpoint = input("Continue? (Y/N) ")
    
    if (checkpoint == 'N' or checkpoint == 'n'):
        print('Program terminated.')
        exit()

    ext = ['.m3u8', '.wav', '.mp3', '.flac']

    try:
        if not src or not lst or not filetype:
            raise RuntimeError('### Missing input')

        if ext[0] not in lst:
            lst += ext[0] 

        filetype.lower()
        if (filetype == 'wav'):
            filetype = '.wav'
        elif (filetype == 'mp3'):
            filetype = '.mp3'
        elif (filetype == 'flac'):
            filetype = '.flac'

        src = src + '/**/*' + filetype

        files = glob.glob(src, recursive=True)
        f_list = {}
        counter = 0

        for f in files:
            fpath = os.path.split(f)[0]     # fpath = folder path
            fname = os.path.split(f)[1]     # fname = file name
            sep = ' - '
            if sep not in fname:
                counter += 1
                continue

            fname = fname.split(" - ")[1]   # split symbol ' - ' (with space)
            f_list[f] = fname
            
        # remove duplicates using dictionary comprehension
        temp = {val: key for key, val in f_list.items()}
        comps = {val: key for key, val in temp.items()}
        print('# Total song found:', len(f_list))
        print('# Without duplication:', len(comps))

        with open(lst, 'w', encoding='utf-8') as m3u:   # create M3U8 file
            m3u.write('#EXTM3U\n\n')
            for i, j in comps.items():
                audio = mutagen.File(i)     # read media file using mutagen
                p = audio['artist'][0]
                q = audio['title'][0]
                r = audio.info.length
                s = '#EXTINF: ' + str(r) + ', ' + p + ' - ' + q
                m3u.write(s + '\n' + i + '\n\n')
        print('# Done.', counter, 'not included.')
    
    except RuntimeError as e:
        print(e)

if __name__ == "__main__":
    main()
