import pandas as pd
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
import re

def convert_to_seconds(time_str):
    """
    Convert a time string in the format 'HH:MM:SS,ms' to total seconds.
    """
    pattern = r'(\d+):(\d+):(\d+),(\d+)'
    match = re.match(pattern, time_str)
    if match:
        hours, minutes, seconds, milliseconds = [int(group) for group in match.groups()]
        total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
        return total_seconds
    else:
        raise ValueError(f"Invalid time string format: {time_str}")

# Read the CSV file
data = pd.read_csv('chapter_details_from_file.csv')

# Load the video
video = VideoFileClip("video11.mp4")

# Iterate through each row in the CSV data
for index, row in data.iterrows():
    chapter_number = row['Chapter No.']
    chapter_end_time_str = row['Chapter End Time']
    chapter_end_time = convert_to_seconds(chapter_end_time_str)

    # Load the image for the current chapter
    image = ImageClip(f"chapter_{chapter_number}.png").set_duration(5)

    # Insert the image at the chapter end time
    final_clip = video.set_start(chapter_end_time - 5.0)  # Trim the video from 5 seconds before the end time
    final_clip = CompositeVideoClip([final_clip, image])  # Overlay the image on the video

    # Write the final clip to a new video file
    output_filename = f"output_video_{chapter_number}.mp4"
    final_clip.write_videofile(output_filename)