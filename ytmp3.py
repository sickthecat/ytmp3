from pytube import YouTube
from moviepy.editor import *
import os
import sys

def download_and_extract_audio(video_url, output_folder='.'):
    # Download video using pytube
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(output_folder)

    # Extract audio and save as .mp3 using moviepy
    video_path = os.path.join(output_folder, video.default_filename)
    audio_path = os.path.join(output_folder, f"{yt.title}.mp3")

    audioclip = AudioFileClip(video_path)
    audioclip.write_audiofile(audio_path)
    
    # Remove the temporary audio file
    os.remove(video_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <video_url> [output_folder]")
        sys.exit(1)
    
    video_url = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else '.'

    download_and_extract_audio(video_url, output_folder)
