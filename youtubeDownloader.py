import os
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from pytube.exceptions import PytubeError
from PIL import ImageTk, Image  # Added import for PIL


def download_video():
    try:
        video_links = []
        for entry in entry_links:
            video_link = entry.get()
            if video_link.strip() != "":
                video_links.append(video_link)
        for video_link in video_links:
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


def add_video_link():
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5, before=button_add)
    entry_links.append(entry)


# Create Tkinter window
root = tk.Tk()
root.title('YouTube MP3 Converter')

# Load image
img = Image.open("iconImage.png")  # Replace "image.png" with the actual filename of your image
img = img.resize((30, 30))  # Resize image as needed
img = ImageTk.PhotoImage(img)

# Create UI elements
label_info = tk.Label(root, text='Enter YouTube video links:')
label_info.pack()

label_image = tk.Label(root, image=img)  # Add image to a label
label_image.pack()

entry = tk.Entry(root, width=50)
entry.pack(pady=5)
entry_links = [entry]

button_add = tk.Button(root, text='+ Add Video', command=add_video_link)
button_add.pack()

# Add a smaller space
space_label = tk.Label(root, text='', height=1)
space_label.pack()

button_download = tk.Button(root, text='Download', command=download_video)
button_download.pack()

label_status = tk.Label(root, text='')
label_status.pack()

root.mainloop()
