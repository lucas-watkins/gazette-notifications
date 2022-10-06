# About
Get desktop notifications for the gazette. This app uses Python 3 and TKinter.messagebox along with a webscraper to display notifications on your desktop. It displays notifications when it detects a change in the gazette or when your computer wakes up from a shutdown or hibernation.

![image](https://user-images.githubusercontent.com/114666925/193298885-aaa760d7-ec17-481b-aa22-91aabe654bae.png)



  
# Windows Installation
Download and run the installer. Then, follow the prompts on screen.

# Mac Installation
I have not made plans to port this to mac yet.

# How it works
This program works by scraping web data from the gazette website and displaying it in a message box. It will check for changes when your computer is awake every 10 minutes and will also detect if your computer went to sleep and notify you after you log on again. It will also show the gazette at startup. The sleep detection on Windows works by writing a timestamp to a tsfile.txt in your user profile every 10 seconds and checking when the last timestamp was.

# Special Thanks
Thank you to the Inno Setup developers for making my life easier!
