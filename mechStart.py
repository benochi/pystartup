import os

# Path to the MP3 files
mp3_files = [
    r'C:\path\to\mechwarrior\song1.mp3',
    r'C:\path\to\mechwarrior\song2.mp3',
    # ... add more paths as needed
]

def play_mp3s():
    for mp3 in mp3_files:
        os.system(f'"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" "{mp3}"')
        
if __name__ == "__main__":
    play_mp3s()
