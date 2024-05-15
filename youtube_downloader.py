import pytube
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
  folder = filedialog.askdirectory()
  if folder:
      # Confirmation message
      print(f"You selected: {folder}")  
      return folder
  return folder

def download(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        high_res = streams.get_highest_resolution()
        high_res.download(output_path=save_path)
        print('Video downloaded successfully!')
    except pytube.exceptions.PytubeError as e:
        print(f"Download error: {e}")  
    except Exception as e:
        print(f"An error occurred: {e}") 

def main():
    root = tk.Tk()
    root.withdraw()
    video_url = input("Please enter the YouTube video link: ")
    save_dir = open_file_dialog()
    if save_dir:
      download(video_url, save_dir)
    else:
      print("Please enter a valid folder path: ")

if __name__ == "__main__":
  main()