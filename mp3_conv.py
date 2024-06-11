import os
import constants
from moviepy.editor import VideoFileClip

def create_destination_dir():
    mp3_dir = os.path.join(constants.CONTAINER_DIRECTORY, "mp3_files")
    os.makedirs(mp3_dir, exist_ok=True)

    print(f"A directory has been created: {mp3_dir}")
    return mp3_dir

def change_extension(filename):
    file, _ = os.path.splitext(filename)
    return f"{file}.mp3"


def convert(filename):
    destination_dir = create_destination_dir() # mp3_files

    video_file_clip = VideoFileClip(filename)

    audio = video_file_clip.audio # Returns an AudioFileClip instance

    file_basename = os.path.basename(filename)
    destination_full_path = os.path.join(destination_dir, change_extension(file_basename))

    audio.write_audiofile(destination_full_path, codec="mp3")

    video_file_clip.close()
