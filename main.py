# Imports
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import os

os.system('color a')

while True:
    # Taking link of the video
    url = input('link: ')
    os.system('cls')

    # Print the title
    try:
        ys = YouTube(url)
        print(f'video: {ys.title}')

    except RegexMatchError:
        print('video not found.')

    else:
        answer = input('format:\n1 - mp3\n2 - mp4\n> ')

        if answer == '1':
            # Getting audio only
            v = ys.streams.get_audio_only()
            print('downloading...')

            # Transforming the mp4 for mp3 and saving in the path 'videos'
            out_file = v.download(output_path="videos")
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print('success download.')

        elif answer == '2':
            # Getting by highest resolution
            v = ys.streams.get_highest_resolution()
            print('downloading...')
            v.download(output_path="videos")
            print('success download.')
        else:
            print("you need type '1' for mp3 and '2' for mp4")