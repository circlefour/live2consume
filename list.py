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

    q_gen = SearchStringGenerator()
    q_rand = q_gen.get_search_string()

    request = youtube.search().list(
       part="snippet",
       q=q_rand,
       maxResults=50,
       type="video"
    )
    response = request.execute()

    #print(response)

    rows = [normalize_search_item(item) for item in response.get("items", [])]

    db = DB()
    db.insert_vids(rows)

if __name__ == "__main__":
    main()
