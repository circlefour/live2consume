import subprocess
from db import DB

vid_link="https://www.youtube.com/watch?v=" # video id gets appended here
video_id = "Et_HlBCRjdE" # bussin game play

# select video_id from vids order by random() limit 1
DB_FILE = 'vids.db'
db = DB()


def play_dat(video_id):
    run = subprocess.run(["yt-dlp", "-o", "./vid.%(ext)s", vid_link + video_id])
    
    #subprocess.run(["ffplay", "vid.mp4"])
    # 20x speed filter applied
    subprocess.run(["ffplay", "-vf", "setpts=0.05*PTS", 'vid.mp4', '-autoexit'])
    
    subprocess.run(["rm", "vid.mp4"])

while True:
    video_id = db.get_rand_id()
    play_dat(video_id)
