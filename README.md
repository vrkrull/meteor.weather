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
To add a Python GUI to your system's application menu (Start Menu, Dock, or Dash), you need to convert your script into a standalone application or create an OS-specific shortcut file, and then place that file into your system's designated applications directory.1. WindowsOn Windows, you can add your GUI to the Start Menu by creating a .lnk file (shortcut) and placing it in the Start Menu folder, or by packaging your script.Using a Shortcut Maker:Open your command prompt or terminal and install pyshortcuts: pip install pyshortcutsRun the command to make a shortcut to your script without the terminal window opening:pyshortcut --icon myicon.ico --name "My App" my_gui_script.pyAlternatively, manually create a shortcut to your Python file and drop it in C:\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs.Creating a Standalone Executable (Recommended for distribution):Install PyInstaller: pip install pyinstallerRun: pyinstaller --noconsole --onefile my_gui_script.pyA .exe file will be generated in the dist folder. Right-click this file, select Create shortcut, and drag that shortcut into your Start Menu directory.2. macOSOn macOS, applications are bundles that reside in the Applications folder. To get your Python GUI into your Launchpad and Dock, you must create a .app wrapper.Using Py2App or PyInstaller:Install py2app: pip install py2appGenerate a setup file: py2applet --make-setup my_gui_script.pyBuild the application: python setup.py py2appA dist folder will be created. Drag the my_gui_script.app file into your main Applications folder. It will now appear in your Launchpad and Spotlight Search.3. LinuxOn Linux, desktop applications appear in the application menu using .desktop configuration files.Creating a .desktop file:Open your terminal and create a new .desktop file in the user applications directory using a text editor:nano ~/.local/share/applications/my_gui_script.desktopPaste the following configuration, adjusting the paths and names to match your environment:ini[Desktop Entry]
Name=My Python App
Exec=/usr/bin/python3 /path/to/your/my_gui_script.py
Icon=/path/to/your/icon.png
Type=Application
Terminal=false
Categories=Utility;Application;
