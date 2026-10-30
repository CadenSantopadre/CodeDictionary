# PyQt Code Dictionary

A lightweight, desktop-based **Code Dictionary** built with PyQt. This application allows developers to store, categorize, and quickly search for code snippets, programming terms, and syntax references completely offline.

## Features

* **Quick Search:** Instant filtering of snippets by title
* **Categorization:** Organize your entries via folders
* **Offline First:** All data is stored locally in `data.json`.

## Requirements

* Python
* PyQt6

## Installation

1. **Create a virtual environment & install dependencies:**
   ~~~bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install PyQt6
   ~~~

2. **Give executable permissions**
`chmod +x /home/cadensantopadre/VSCode/CodeDictionary/exec.sh` - your name folder will be different than mine
`chmod +x /home/cadensantopadre/VSCode/CodeDictionary/exec2.sh` - your name folder will be different than mine


## 💻 Usage

Use the shell scripts (`exec.sh`, `exec2.sh`) provided in a desktop application shortcut to quickly open the program
For an example app shortcut:
~~~
[Desktop Entry]
Type=Application
Name=My Code Dictionary
Comment=Launch Python script with venv
Exec=/home/cadensantopadre/VSCode/CodeDictionary/exec.sh
Path=/home/cadensantopadre/VSCode/CodeDictionary/
Icon=/home/cadensantopadre/Pictures/dictionary.png
Terminal=false
StartupNotify=false
~~~