# Instagram-Bot
An Instagram bot written in Python using Selenium on Google Chrome. It is a basic bot and it will like the first post displayed on your login page and save the post.

Table of Contents

->Getting Started
->Prerequisites
->Instructions
->File Structure
->Demo
->Contributing
->Creator / Maintainer
->Additional Information
->Getting Started

###Please be aware of Instagram's daily limits for likes and comments to avoid getting your account banned.

Prerequisites

++Python 3

++Pip - a python package manager

++Download this file, open a command prompt and navigate to the folder containing the get-pip.py installer, and run python get-pip.py to install

++Run pip --version to check if it has installed correctly

++ChromeDriver - a WebDriver for Chrome

++See Additional Information for more details on installing

++Selenium - a python package used to automate web browser interaction pip install -U selenium

++Instructions

++Download ChromeDriver and extract the file.

++Check the version of your Google Chrome and download the matching ChromeDriver version

++Check Chrome Version

In config.py change the chromedriver_path to the local path of where your ChromeDriver executable file is located 

chromedriver_path = "C:\chromedrivers\chromedriver.exe"

Adjustments you can make in config.py to tweak the bot to your liking. (Please be aware of Instagram's daily limits for likes and comments to avoid getting banned.)


Create a file named credentials.py to hold your account login information using the format below.

See File Structure for where the file should be placed.

USERNAME = "xxx"

PASSWORD = "xxx"

Run the script. Enjoy your Instagram bot!

python insta-bot.py

File Structure

Twitter-Retweet-Bot

|-- config.py

|-- credentials.py

|-- insta-bot.py
 
Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.


If you have any questions, comments, or concerns, feel free to contact me below.

Connect via Email
bariddhi14@gmail.com

This project was created for educational purposes and for personal and open-source use.
