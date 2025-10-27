import subprocess

vid_link="https://www.youtube.com/watch?v=" # video id gets appended here
video_id = "Et_HlBCRjdE" # bussin game play

run = subprocess.run(["yt-dlp", "-o", "./vid.%(ext)s", vid_link + video_id])

#subprocess.run(["ffplay", "vid.mp4"])
# 20x speed filter applied
subprocess.run(["ffplay", "-vf", "setpts=0.05*PTS", 'vid.mp4', '-autoexit'])

subprocess.run(["rm", "vid.mp4"])
