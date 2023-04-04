# Import necessary libraries
import os
import requests
import subprocess
import getpass
from tqdm import tqdm

# Define a function to download a mod
def download_mod():
    # Get the download URL from user input
    url = input("Enter the download URL: ")

    # Get the file name from the download URL
    filename = os.path.basename(url)

    # Set the path to the Mods folder of the current user
    mods_path = os.path.realpath(os.path.join(os.getenv("LOCALAPPDATA"), "..", "LocalLow", "Stress Level Zero", "BONELAB", "Mods"))

    # Download the file with a progress bar
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(filename, 'wb') as f:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
    progress_bar.close()

    # Use 7zip to extract the file to the Mods folder with a progress bar
    zip_path = os.path.join(os.getcwd(), filename)
    command = ['C:\\Program Files\\7-Zip\\7z.exe', 'x', '-o' + mods_path, zip_path]
    with tqdm(total=len(command), desc='Extracting', unit='cmds') as command_progress:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(process.stdout.readline, b''):
            command_progress.update(1)
            print(line.decode().strip())
    command_progress.close()

    # Delete the downloaded zip file
    os.remove(zip_path)

    # Ask the user if they want to open the extracted files location
    while True:
        choice = input("Do you want to open the Mods folder? (Y/N): ")
        if choice.lower() == "y":
            os.startfile(mods_path)
            break
        elif choice.lower() == "n":
            break
        else:
            print("Invalid choice, please enter Y or N")

# Loop to continue downloading mods until the user chooses to quit
while True:
    # Call the download_mod function
    download_mod()

    # Ask the user if they want to download another mod
    choice = input("Would you like to download another mod? (Y/N): ")
    if choice.lower() == "n":
        break
    elif choice.lower() == "y":
        # Clear the screen before downloading another mod
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Invalid choice, please enter Y or N")
