import json
import os

import requests
from modes import download_reel, merge_videos, upload_command


def insta_reels():
    usernames = ['ennada_panni__vachirukeenga', '_its_music_world_']

    for username in usernames:
        url = f"https://i.instagram.com/api/v1/feed/user/{username}/username/?count=12"
        payload = {}
        headers = {
            'authority': 'i.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-ig-app-id': '936619743392459',
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        reels_list = json.loads(response.text)
        reels_list = reels_list['items']

        with open('reels_list.json', 'w') as outfile:
            json.dump(reels_list, outfile, indent=4)

        reel_list_len = len(reels_list)
        print(reel_list_len)

        for reel in range(reel_list_len):
            if 'video_versions' in reels_list[reel]:
                reel_url = reels_list[reel]['video_versions'][-1]['url']
                # media_id = reels_list[reel]['caption']['media_id']
                media_id = reels_list[reel]['video_versions'][-1]["id"]
                print(media_id)
                print(reel_url)
                download_results = download_reel.download_to_mp4(media_id, reel_url)
                print(download_results)
            else:
                print('No Reels')

        files_list = os.listdir('/Users/mukthy/Desktop/py-projects/instagrambot/reels')
        print(files_list)
        merged_video_result = merge_videos.merge(files_list)
        print(merged_video_result)

        upload_results = upload_command.upload()
        print(upload_results)

        if upload_results == 0:
            print('Uploaded Successfully')
            os.system('ls -la /Users/mukthy/Desktop/py-projects/instagrambot/reels/')
            os.system('rm -rf /Users/mukthy/Desktop/py-projects/instagrambot/reels/*.mp4')
            os.system('ls -la /Users/mukthy/Desktop/py-projects/instagrambot/reels/')
        else:
            print('Error in Uploading')
            os.system('ls -la /Users/mukthy/Desktop/py-projects/instagrambot/reels/')

        files_list.clear()


if __name__ == '__main__':
    insta_reels()
