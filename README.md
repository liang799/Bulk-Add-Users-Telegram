# Bulk Add Users Telegram
## About
Reads list of users from an excel file, and sends group invite link to the list of users.

## Demo
[![Demo youtube video](https://img.youtube.com/vi/1pGGPR0eIZ0/0.jpg)](https://www.youtube.com/watch?v=1pGGPR0eIZ0)

## Setup Instructions
### Git
Download the [64-bit Git for windows setup](https://git-scm.com/download/win)
### Python
Download [python](https://www.python.org/downloads/)
### Configuration
Inside terminal:
```commandline
git clone https://github.com/liang799/Bulk-Add-Users-Telegram
cd Bulk-Add-Users-Telegram
start .
```
1. Make a copy of `.env.example` and rename it to `.env`
2. Edit the variables accordingly
3. Open `users.xlsx` in excel and edit accordingly
### Install Python Dependencies
```commandline
pip install -r requirements.txt
```
### Running the code
```commandline
python main.py
```
