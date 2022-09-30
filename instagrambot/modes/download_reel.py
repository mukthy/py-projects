import requests


def download_to_mp4(media_id, url):
    # url = 'https://instagram.fmaa11-1.fna.fbcdn.net/v/t50.2886-16/10000000_569282344946952_2513450440819325015_n.mp4?_nc_ht=instagram.fmaa11-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=nYodztV6bIcAX9bqWUu&edm=ACWDqb8BAAAA&ccb=7-5&oe=6336F7D8&oh=00_AT8Fm_ukFPn_774-fro9O3AbvuHt3kLRvItYDugxTGXStQ&_nc_sid=1527a3'
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
    r = requests.get(url, headers=headers)
    with open(f'/Users/mukthy/Desktop/py-projects/instagrambot/reels/{media_id}.mp4', 'wb') as f:
        f.write(r.content)
        f.close()

    return r.status_code
