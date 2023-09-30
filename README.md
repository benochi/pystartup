# Chrome Profiles and MP3 Playback Automation

This repository contains Python scripts to manage Chrome profiles and play MP3 files automatically on Windows startup.

## getProfiles.py

**Usage**

1. Install Python if not already installed. You can download it from [Python's official website](https://www.python.org/downloads/).

2. Open the `getProfiles.py` script in a text editor and update the `CHROME_USER_DATA_DIR` variable to your Chrome user data directory.

3. Run the script using the following command in your command prompt or terminal:

This script will display a list of Chrome profiles and their corresponding names as seen in the Chrome UI.

## start.py

**Usage**

1. Open the `start.py` script in a text editor.

2. Update the `profiles` list with the names of the Chrome profiles you want to launch.

3. Run the script using the following command:

This script will launch Chrome with the specified profiles.

## mechStart.py

**Usage**

1. Install the `playsound` module by running the following command:

2. Place your MP3 files in the same directory as `mechStart.py`.

3. Open the `mechStart.py` script in a text editor.

4. Update the `mp3_files` list with the names of the MP3 files you want to play on startup.

5. Run the script using the following command:

This script will play the specified MP3 files.

## Running Scripts on Startup

To run any of the above scripts on Windows startup:

1. Create a batch file (e.g., `startup_play_mp3.bat`) in the same directory as your Python script.

2. Open the batch file in a text editor and add the following lines, replacing `"path_to_script_directory"` with the full path to the directory containing your Python script:

For example, to run `mechStart.py`, replace `script_name.py` with `mechStart.py`.

3. Save the batch file.

4. Press `Win + R` to open the Run dialog, type `shell:startup`, and press Enter. This opens the Startup folder.

5. Move the batch file (`startup_play_mp3.bat`) into the Startup folder.

Now, when you log in to your Windows account, the batch file will run automatically, executing the associated Python script.

Feel free to customize the scripts and batch files to suit your specific needs.
