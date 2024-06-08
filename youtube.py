from pytube import YouTube
from tkinter import Tk
from tkinter import filedialog

def download_video(url,save_path):
    try:
        yt = YouTube(url)
        streams =yt.streams.filter(progressive=True,file_extension='mp4')
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

root = Tk()  
root.withdraw()        
        
def main():
    url = input('Enter the video URL: ')
    save_path = open_file_dialog()
    download_video(url,save_path)
    
    
if __name__ == '__main__':
    main()