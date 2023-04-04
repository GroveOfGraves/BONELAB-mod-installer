# BONELAB-mod-installer
A Python and 7-Zip-based BONELAB mod installation tool for Windows, written with the help of ChatGPT

USAGE:

NOTE - this script only works with native mods, code mods are stored in an installation-dependant direcotry and are therefore not supported.

This Python script requires 7-Zip and the Python requests and tqdm libaries (and obviously Python) to be installed to work. If you don't have all of them installed, run the following commands (in the Windows Command Prompt), or (recommended) run the included .bat file, which will run these all automatically:

```
winget install --id Python.Python -e
pip install requests
pip install tqdm
winget install --id 7zip.7zip -e
```

To install mods:

(0) Open the BONELAB_mod_installer.py file once Python and 7-Zip are installed, if it won't open when clicked on in Windows Explorer, run the .py through the Windows Command Prompt
(1) Find the mod.io page for the mod you want to install
(2) Right-click on the "Download file" button for the mod's Windows download option
(3) Select "Copy link address"
(4) Paste it into the Python code's prompt for a link
(5) Follow remaining prompts as you see fit

This script will install the mod directly into your %APPDATA%\..\LocalLow\Stress Level Zero\BONELAB\Mods folder, where the game stores all native mods. This code will still work even if you have the Mods folder on a different drive to save space using a Windows junction link, as I do. If you follow the above instuctions, the code should work without any issue. I may link a YouTube video showing proper usage if I see fit.
