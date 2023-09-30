import os

def launch_chrome_profiles():
    #Run getProfiles.py to find your chrome profile names.
    profiles = [
        "Profile 6",
        "Profile 7",
        "Profile 8",
        "Default"
    ]
    
    for profile in profiles:
        os.system(f'start chrome --profile-directory="{profile}"')

if __name__ == "__main__":
    launch_chrome_profiles()
