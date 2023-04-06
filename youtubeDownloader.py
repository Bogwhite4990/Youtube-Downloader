import os
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from pytube.exceptions import PytubeError


def download_video():
    try:
        video_link = entry_link.get()
        yt = YouTube(video_link)
        file_name = yt.title + ".mp3"
        file_path = filedialog.asksaveasfilename(defaultextension='.mp3', initialfile=file_name,
                                                 filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            yt.streams.get_audio_only().download(output_path=os.path.dirname(file_path))
            os.rename(yt.streams.get_audio_only().default_filename, file_path)
            label_status.config(text='Download successful!')
        else:
            label_status.config(text='Download cancelled.')
    except PytubeError as e:
        label_status.config(text=str(e))


# Create Tkinter window
root = tk.Tk()
root.title('YouTube Video to MP3 Converter')

# Create UI elements
label_info = tk.Label(root, text='Enter YouTube video link:')
label_info.pack()

entry_link = tk.Entry(root, width=50)
entry_link.pack()

button_download = tk.Button(root, text='Download', command=download_video)
button_download.pack()

label_status = tk.Label(root, text='')
label_status.pack()

root.mainloop()
