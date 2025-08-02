# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import googleapiclient.discovery
import googleapiclient.errors

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def main():
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    request = youtube.search().list(
       part="snippet",
       q="random",
       maxResults=50,
       type="video"
    )
    response = request.execute()

    print(response)

    #for item in response.get("items", []):
    #    print(f"{item['snippet']['title]} (ID: {item['id']['videoId']})")

if __name__ == "__main__":
    main()
