from pytube import YouTube
from tkinter import Tk, filedialog, simpledialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        stream = streams.get_highest_resolution()
        stream.download(save_path)
        print('Downloaded successfully')
    except Exception as e:
        print(e)
        print('Something went wrong')

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print('Selected:', folder)
    else:
        print('No folder selected')
    return folder

def main():
    root = Tk()
    root.withdraw()  # Hide the main window
    
    url = simpledialog.askstring("Input", "Enter the video URL:")
    if not url:
        print('No URL entered')
        return
    
    save_path = open_file_dialog()
    if save_path:
        download_video(url, save_path)

if __name__ == '__main__':
    main()
