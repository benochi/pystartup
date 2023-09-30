import os
import json

CHROME_USER_DATA_DIR = r'C:\Users\[YOUR NAME HERE]\AppData\Local\Google\Chrome\User Data'

def get_chrome_profile_names(directory):
    """Returns the profile name as seen in Chrome UI from the Preferences file."""
    preferences_path = os.path.join(CHROME_USER_DATA_DIR, directory, 'Preferences')
    try:
        with open(preferences_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('profile', {}).get('name', directory)
    except Exception as e:
        return directory  # If there's any issue reading the Preferences, return the directory name

def get_chrome_profiles():
    """Returns a list of available Chrome profile directories."""
    profiles = [name for name in os.listdir(CHROME_USER_DATA_DIR) if os.path.isdir(os.path.join(CHROME_USER_DATA_DIR, name)) and "Profile" in name]
    if "Default" in os.listdir(CHROME_USER_DATA_DIR):
        profiles.append("Default")
    return profiles

if __name__ == "__main__":
    profile_directories = get_chrome_profiles()
    print("Found Chrome profiles:")
    for directory in profile_directories:
        profile_name = get_chrome_profile_names(directory)
        print(f"- {directory} ({profile_name})")
