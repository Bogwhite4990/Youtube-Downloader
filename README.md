# YouTube MP3 Converter

YouTube MP3 Converter is a Python application that allows you to convert YouTube videos to MP3 audio files using the `pytube` library and a graphical user interface (GUI) built with Tkinter.

## Features

- Enter YouTube video links to convert to MP3 audio files.
- Add multiple video links to convert in batch.
- Save converted MP3 files with custom file names and locations.
- Provides status updates on the download process.

## Requirements

- Python 3.x
- `pytube` library
- Tkinter library
- Pillow library (for image display)

## Usage

1. Install the required libraries using `pip`:

**pip install pytube pillow**

2. Run the `youtube_mp3_converter.py` script using Python:

**python youtube_mp3_converter.py**

3. Enter the YouTube video links that you want to convert in the GUI window. Click the "+ Add Video" button to add multiple video links.
4. Click the "Download" button to start the conversion process. Converted MP3 files will be saved with custom file names and locations that you can specify using the file dialog.
5. The status label will show updates on the download process, and the converted MP3 files will be saved to the locations you specified.

Note: Make sure you have a stable internet connection to download YouTube videos efficiently.

## Acknowledgements

- [pytube](https://github.com/nficano/pytube): A library for downloading YouTube videos.
- [Tkinter](https://docs.python.org/3/library/tkinter.html): A standard Python library for creating GUI applications.
- [Pillow](https://pillow.readthedocs.io/en/stable/): A library for handling images in Python.
