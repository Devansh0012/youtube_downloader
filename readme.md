# YouTube Downloader

This project is a YouTube downloader that allows users to download videos from YouTube and save them locally. It provides a simple and intuitive graphical interface for users to enter the URL of the YouTube video they want to download and choose the desired save location.

## Features

- Download YouTube videos in the highest available quality
- Save downloaded videos locally
- Easy-to-use graphical interface

## Installation

1. Clone the repository: `git clone https://Devansh0012/youtube_downloader.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create an executable (optional):
   - Install PyInstaller: `pip install pyinstaller`
   - Create the executable: `pyinstaller --onefile youtube_downloader_gui.py`
   - Locate the executable in the `dist` folder

## Usage

### Running from Command Line

1. Run the application: `python youtube_downloader_gui.py`
2. A dialog will appear asking for the URL of the YouTube video you want to download.
3. Enter the URL and click "OK".
4. Select the folder where you want to save the downloaded video.
5. The video will be downloaded and saved to the selected folder.

### Running the Executable

1. Double-click the `youtube_downloader_gui.exe` file.
2. A dialog will appear asking for the URL of the YouTube video you want to download.
3. Enter the URL and click "OK".
4. Select the folder where you want to save the downloaded video.
5. The video will be downloaded and saved to the selected folder.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License.
