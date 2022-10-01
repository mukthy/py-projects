import os
from os.path import exists

from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip


def merge(files_list):
    if exists('/Users/mukthy/Desktop/py-projects/instagrambot/reels/.DS_Store'):
        print('Removing .DS_Store')
        os.system('rm -rf /Users/mukthy/Desktop/py-projects/instagrambot/reels/.DS_Store')

        clips = [VideoFileClip(f'/Users/mukthy/Desktop/py-projects/instagrambot/reels/{clip}') for clip in files_list]

        # you can increase the number of clips by increase the 5 to 10 or 15 but max number of clips is 22 that we get from instagram.
        # clips = clips[:5]
        print(clips)
        final_clip = concatenate_videoclips(clips, method="compose")
        final_clip.write_videofile("/Users/mukthy/Desktop/py-projects/instagrambot/reels/merged.mp4", threads=8,
                                   temp_audiofile='temp-audio.m4a', codec='libx264', audio_codec='aac')

    else:
        print('No .DS_Store file')
        clips = [VideoFileClip(f'/Users/mukthy/Desktop/py-projects/instagrambot/reels/{clip}') for clip in files_list]

        # you can increase the number of clips by increase the 5 to 10 or 15 but max number of clips is 22 that we get from instagram.
        # clips = clips[:5]
        print(clips)
        final_clip = concatenate_videoclips(clips, method="compose")
        final_clip.write_videofile("/Users/mukthy/Desktop/py-projects/instagrambot/reels/merged.mp4", threads=8,
                                   temp_audiofile='temp-audio.m4a', codec='libx264', audio_codec='aac')

    return final_clip
