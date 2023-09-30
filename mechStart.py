from playsound import playsound

# Path to the MP3 file (now in the same directory as the script)
mp3_files = [
    'mw2start.mp3',  # Assuming the file is named "mw2start.mp3"
    # ... other paths if needed
]

def play_mp3s():
    for mp3 in mp3_files:
        print(f"Playing {mp3}...")
        playsound(mp3)

if __name__ == "__main__":
    play_mp3s()
