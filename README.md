# Meteor.weather
A simple weather app that gets out of your way
It is a weather app that tells you the weather. Simple. Easy to use.
By default, it just looks at your location, but you can also type in specific locations.
You can choose between weather sources Open-Meteo (default) and wttr.in.
Click the link below to learn more about Open-Meteo
https://open-meteo.com/en/about
Click the link below to install python
https://www.python.org/downloads/
Click the link below to install pip
https://pip.pypa.io/en/stable/installation/
## INSTALLATION
THIS WILL RUN ON EVERYTHING THAT CAN RUN PYTHON 11 OR LATER AND CAN RUN PIP
First, download the zip file and extract it.
Then open your terminal - https://alacritty.org/#Installation click this link to install a terminal
and type
```zsh
pip install PySide6 requests
python main.py
```

## I want to add this to my start menu! (how to do that)
To add a Python GUI application to your system’s application launcher (Start Menu, Dock, Dash, Launchpad, etc.), you can either package the app into a standalone executable or create an OS-specific launcher entry. Below are the recommended installation and launcher setup methods for Windows, macOS, Ubuntu, Arch Linux, Fedora, Raspberry Pi OS, and other Linux distributions.
### Installing and Adding a Python App to the Application Menu
####  Windows

On Windows, applications appear in the Start Menu through shortcuts (.lnk files) or installed executables.

Option 1: Create a Start Menu Shortcut

Install pyshortcuts:

pip install pyshortcuts

Create a shortcut for your app:

pyshortcut --icon myicon.ico --name "My App" my_gui_script.py

This automatically adds the app to your Start Menu without opening a terminal window.

You can also manually:

Right-click your Python script or executable
Select Create shortcut
Move the shortcut to:
C:\Users\YOUR_USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
Option 2: Build a Standalone .exe (Recommended)

Install PyInstaller:

pip install pyinstaller

Build the application:

pyinstaller --noconsole --onefile my_gui_script.py

Your executable will appear in the dist folder.

You can then:

Right-click the .exe
Select Create shortcut
Move the shortcut into the Start Menu folder

This method is best for distributing your application to other users.

#### macOS

On macOS, applications are distributed as .app bundles and placed in the Applications folder.

Using py2app

Install py2app:

pip install py2app

Generate a setup file:

py2applet --make-setup my_gui_script.py

Build the app:

python setup.py py2app

A .app bundle will be created inside the dist folder.

Move it into:

/Applications

Your app will now appear in:

Launchpad
Spotlight Search
The Dock
Alternative: PyInstaller on macOS

You can also use PyInstaller:

pip install pyinstaller
pyinstaller --windowed my_gui_script.py

The generated .app file can also be moved into /Applications.

#### Linux

Most Linux desktop environments use .desktop launcher files to display applications in the app menu.

The general process is:

Create a .desktop file
Place it in your applications directory
Make it executable
#### Ubuntu / Debian / Raspberry Pi OS

Create a launcher file:

nano ~/.local/share/applications/my-python-app.desktop

Paste:

[Desktop Entry]
Name=My Python App
Exec=python3 /path/to/my_gui_script.py
Icon=/path/to/icon.png
Type=Application
Terminal=false
Categories=Utility;

Save the file.

Make it executable:

chmod +x ~/.local/share/applications/my-python-app.desktop

Your app should now appear in:

GNOME Activities
Application Menu
Dock search
Raspberry Pi Menu (on Raspberry Pi OS)
Arch Linux

The process is identical to Ubuntu, but make sure Python is installed:

sudo pacman -S python

Then create the .desktop file:

nano ~/.local/share/applications/my-python-app.desktop

Example:

[Desktop Entry]
Name=My Python App
Exec=python /path/to/my_gui_script.py
Icon=/path/to/icon.png
Type=Application
Terminal=false
Categories=Utility;

Enable it:

chmod +x ~/.local/share/applications/my-python-app.desktop
Fedora

Install Python if needed:

sudo dnf install python3

Create the launcher:

nano ~/.local/share/applications/my-python-app.desktop

Use:

[Desktop Entry]
Name=My Python App
Exec=python3 /path/to/my_gui_script.py
Icon=/path/to/icon.png
Type=Application
Terminal=false
Categories=Utility;

Then:

chmod +x ~/.local/share/applications/my-python-app.desktop

Your app will appear in the GNOME app launcher.

#### Raspberry Pi OS

Raspberry Pi OS uses the same .desktop launcher system as Debian.

Create:

nano ~/.local/share/applications/my-python-app.desktop

Example:

[Desktop Entry]
Name=My Raspberry Pi App
Exec=python3 /home/pi/my_gui_script.py
Icon=/home/pi/icon.png
Type=Application
Terminal=false
Categories=Utility;

Then run:

chmod +x ~/.local/share/applications/my-python-app.desktop

Your application will appear in the Raspberry Pi menu.

Other Linux Distributions

Most Linux distributions follow the FreeDesktop.org desktop entry standard, so the same .desktop approach works across nearly all desktop environments, including:

KDE Plasma
GNOME
XFCE
Cinnamon
MATE
LXQt
Budgie
Generic Method

Create:

~/.local/share/applications/my-python-app.desktop

Add:

[Desktop Entry]
Name=My Python App
Exec=python3 /path/to/my_gui_script.py
Icon=/path/to/icon.png
Type=Application
Terminal=false
Categories=Utility;

Then enable it:

chmod +x ~/.local/share/applications/my-python-app.desktop

Refresh your desktop environment or log out and back in if the launcher does not immediately appear.

Optional: Package Your App for Distribution

For a more professional installation experience, you can package your app into native installers:

Platform	Packaging Tool
Windows	PyInstaller, cx_Freeze
macOS	py2app, PyInstaller
Linux	AppImage, Flatpak, Snap, .deb, .rpm

Examples:

AppImage → portable Linux executable
Flatpak → universal Linux app distribution
Snap → Ubuntu-friendly packaging
.deb → Debian/Ubuntu/Raspberry Pi OS packages
.rpm → Fedora/RHEL packages

These methods allow users to install your app like any other desktop application.
