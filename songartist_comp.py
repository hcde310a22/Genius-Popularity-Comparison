import requests
access_token = "w-59mN-elcgR5fCXv4kxkWNzTk1g5rtbH54OyvxMK7I8BTc6D1lWUJz9_2sT3WKD"

def get_songs(song_title, artist_name):
    # Set the base URL for the Genius API
    base_url = "https://api.genius.com"

    # Search endpoint
    search_endpoint = "/search"

    # Headers for the request
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Parameters for the request
    params = {
        "q": song_title,
        "per_page": 1,
        "sort": "popularity"
    }

    # GET request to the Genius API for the inputted song
    response = requests.get(f"{base_url}{search_endpoint}", headers=headers, params=params)

    # Pageviews for the inputted song
    inputted_song_pageviews = response.json()["response"]["hits"][0]["result"]["stats"]["pageviews"]

    # Parameters for the request to find songs by the specified artist
    params = {
        "q": artist_name,
        "per_page": 50,
        "sort": "popularity"
    }

    # GET request to the Genius API to search for songs by the specified artist
    response = requests.get(f"{base_url}{search_endpoint}", headers=headers, params=params)

    # List of songs by the specified artist
    songs = response.json()["response"]["hits"]

    count = 0
    ret_list = []
    # Print songs with pageview counts >= 90% of the inputted song
    for song in songs:
        pageviews = song["result"]["stats"]["pageviews"]
        if pageviews >= inputted_song_pageviews * 0.90 and pageviews <= inputted_song_pageviews * 1000.40:
            count += 1
            ret_list.append(song["result"]["title"])

    if count < 1:
            ret_list.append(artist_name + " has no songs as popular as " + song_title + ".")

    print(ret_list)
    return ret_list