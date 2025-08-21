# gpt written

def normalize_search_item(item):
    """Convert a YouTube search API item into our DB schema dict."""
    return {
        "video_id": item["id"]["videoId"],
        "published_at": item["snippet"]["publishedAt"],
        "title": item["snippet"]["title"],
        "description": item["snippet"]["description"],
        "channel_title": item["snippet"]["channelTitle"],
        "channel_id": item["snippet"]["channelId"],
    }

