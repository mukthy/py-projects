import os
import time
from os.path import exists
import datetime


def upload():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    print(date)
    result = os.system(
        f'python /Users/mukthy/Desktop/py-projects/instagrambot/modes/uploadtoyoutube.py --file="/Users/mukthy/Desktop/py-projects/instagrambot/reels/merged.mp4" --title="MemeCompilation ~ InstaReels - {date}" --description="Daily Dose of Meme Compilation freshly brewed from Instagram. Please leave a Like and Commend. Share and Subscribe to help us grow! Credits the Creators of these Funny Reels, please follow them as well on Instagram" --keywords="reels,Meme,funnyclips,funnyvideos,meme compilations,funny reels,timepass,instagram" --category="22" --privacyStatus="public"')
    print(result)
    return result
