#Q.1- Print the current day using Datetime module.
import datetime as dt
d=dt.date.today()
print(d.day)

#Q.2- Open your browser and play a video using webbrowser module in python.
import webbrowser
url="https://youtu.be/N4mEzFDjqtA"
webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://youtu.be/N4mEzFDjqtA")

#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.
import os,sys
folder = r'C:\Users\Asmita Sharma\Desktop\New folder\python11'

for f in os.listdir(folder):
    i = os.path.join(folder,f)
    if not os.path.isfile(i):
        continue
    o = os.path.splitext(f)
    n = i.replace('.png', '.jpg')
    output = os.rename(i,n)
