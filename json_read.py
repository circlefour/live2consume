import json

with open('pretty_out0.json', 'r') as f:
    data = json.load(f)

print('type', type(data))
keys = list(data.keys())
print('keys:', keys)
items = data['items'][0]
print('keys in items:', list(items.keys()))
print('keys in id in items:', list(items['id'].keys()))
print('keys in snippet in items:', list(items['snippet'].keys()))
pretty = json.dumps(items, indent=4)
print(pretty)

'''
EXAMPLE OUTPUT

{
    "kind": "youtube#searchResult",
    "etag": "qgVrm203QclnFHdAgQdR_jbnDyQ",
    "id": {
        "kind": "youtube#video",
        "videoId": "CBLvNb5Ehgs"
    },
    "snippet": {
        "publishedAt": "2025-07-28T10:00:30Z",
        "channelId": "UC8efBuMd2Tsolb5uTfpex3A",
        "title": "Brian Tyler Cohen | Club Random",
        "description": "Bill Maher and YouTube star Brian Tyler Cohen dive into the chaos of modern politics in a freewheeling conversation covering ...",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/CBLvNb5Ehgs/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/CBLvNb5Ehgs/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/CBLvNb5Ehgs/hqdefault.jpg",
                "width": 480,
                "height": 360
            }
        },
        "channelTitle": "Club Random Podcast",
        "liveBroadcastContent": "none",
        "publishTime": "2025-07-28T10:00:30Z"
    }
}
'''
