# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import googleapiclient.discovery
import googleapiclient.errors

from dotenv import load_dotenv

from db import DB
from search_string import SearchStringGenerator
from yt_utils import normalize_search_item

load_dotenv()
api_key = os.getenv("API_KEY")

def main():
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    db = DB()

    q_gen = SearchStringGenerator(max_words=1)

    while True:
        q_rand = q_gen.get_search_string()
        print('what does the random query look like', q_rand)

        request = youtube.search().list(
           part="snippet",
           q=q_rand,
           maxResults=50,
           type="video"
        )
        try:
            response = request.execute()
        except googleapiclient.errors.HttpError as e:
            if 'quotaExceeded' in str(e):
                print('quota exceeded...shiiiiiiii... brb tomorrow')
                db.close()
                return
            else:
                db.close()
                raise e
        #print(response)
        #print(response['items'][0])

        #rows = [normalize_search_item(item) for item in response.get("items", [])]
        rows = [normalize_search_item(item) for item in response.get('items', [])
                if item.get('id', {}).get('kind') == 'youtube#video']
        print('are there any rows here', rows[:3])
        print('number of rows: ', len(rows))

        if not rows:
            print('no results for query:', q_rand)
        else:
            db.insert_vids(rows)

    db.close()

if __name__ == "__main__":
    main()
