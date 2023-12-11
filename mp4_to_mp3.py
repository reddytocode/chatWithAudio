from moviepy.editor import *

file_name = ""
video = VideoFileClip(f"{file_name}.mp4")
video.audio.write_audiofile(f"{file_name}.mp3")

