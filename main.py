# Program to create an interface to download YouTube videos using Tkinter and Pytube

# Import the necessary libraries
from tkinter import *
from pytube import YouTube

# Interface window
root = Tk()
root.geometry('800x600')
root.resizable(0,0)
root.title("YouTube Video Downloader")

Label(root, text = "Youtube Video Downloader", font = "calibri 20 bold").pack()

# Variable and entry field
link = StringVar()
Label(root, text = "Paste YouTube Link here:", font = "calibri 15 bold").place(x = 160, y = 60)
link_enter = Entry(root, width =70, textvariable = link).place(x=32, y=90)


#Download function 
def Downloader():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download()
    '''stream=url.streams.get_by_itag(137)
    stream.download()'''
    Label(root, text = "Downloaded", font = "calibri 15").place(x = 180, y = 210)


#Download button
Button(root, text = "Download video", font = "calibri 15 bold", bg = "purple", padx = 2, command = Downloader).place(x = 180, y = 150)


root.mainloop()