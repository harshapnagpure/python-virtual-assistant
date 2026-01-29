# python-virtual-assistant: 

This is a simple Python virtual assistant project named Jarvis.

I created this project while learning Python programming.

Project Learning Source

This project is inspired by the Jarvis Assistant shown at the end of the video:

Python Tutorial For Beginners in Hindi | Complete Python Course

Instructor: CodeWithHarry

Platform: YouTube

About This Project

This project is a beginner-level Python automation project.

It is made to understand:

Python functions

Conditional statements

Loops

Working with Python libraries

Basic automation using Python

What This Assistant Can Do

Jarvis can perform the following tasks:

Greet the user according to time

Open YouTube

Open Google

Open StackOverflow

Tell the current time

Search information on Wikipedia

Speak responses using text-to-speech

How This Project Works

The program starts and greets the user

It waits for a command

The command is taken as text input

Python checks the command using if and elif

According to the command, an action is performed

Example:

If you type:

open youtube


Jarvis will open YouTube in the browser.

Voice Input Information (Important)

This project is written using Python 3.14

Microphone-based voice input libraries like PyAudio
do not fully support Python 3.14 on Windows

Because of this limitation, text input is used instead of voice input

This is not a coding mistake, it is a library compatibility issue.

Libraries Used in This Project

Python 3.14

pyttsx3 (for text to speech)

wikipedia

webbrowser

datetime

os

How to Run This Project

Step 1: Activate the virtual environment

.\.venv\Scripts\Activate.ps1


Step 2: Run the Python file:

-python jarvis_314.py

Project Files Structure
jarvis_314.py   -> Main Python file
.venv/          -> Virtual environment folder

What I Learned From This Project

From this project, I learned:

How Python automation works

How to use external libraries

How to fix installation and dependency errors

How to work with virtual environments

How to structure a Python project
