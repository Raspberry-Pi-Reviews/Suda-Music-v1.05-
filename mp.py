from tkinter import *
import pygame
import os

class MusicPlayer:

  def __init__(self,root):
    self.root = root
    self.root.title("Suda Music")
    self.root.geometry("1000x500")
    pygame.init()
    pygame.mixer.init()
    self.track = StringVar()
    self.status = StringVar()

    trackframe = LabelFrame(self.root,text="Song Track",font=("arial",15,"bold"),bg="lightblue",fg="Black",bd=5,relief=GROOVE)
    trackframe.place(x=0,y=0,width=600,height=100)
    songtrack = Label(trackframe,textvariable=self.track,width=20,font=("arial",24,"bold"),bg="lightgrey",fg="black").grid(row=0,column=0,padx=10,pady=5)
    trackstatus = Label(trackframe,textvariable=self.status,font=("arial",24,"bold"),bg="lightgrey",fg="Black").grid(row=0,column=1,padx=10,pady=5)
    infoframe = LabelFrame(root,text="Updates",font=("times new roman",15,"bold"),bg="lightblue",fg="black",bd=5,relief=GROOVE)
    buttonframe = LabelFrame(self.root,text="Control Panel",font=("arial",15,"bold"),bg="lightblue",fg="black",bd=5,relief=GROOVE)
    buttonframe.place(x=0,y=100,width=600,height=100)
    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("arial",16,"bold"),fg="Black",bg="lightgrey").grid(row=0,column=0,padx=10,pady=5)
    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("arial",16,"bold"),fg="Black",bg="lightgrey").grid(row=0,column=1,padx=10,pady=5)
    playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("arial",16,"bold"),fg="Black",bg="lightgrey").grid(row=0,column=2,padx=10,pady=5)
    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("arial",16,"bold"),fg="Black",bg="lightgrey").grid(row=0,column=3,padx=10,pady=5)
    infoframe.place(x=0,y=200,width=1000,height=300)
    songsframe = LabelFrame(self.root,text="Song Playlist",font=("arial",15,"bold"),bg="lightblue",fg="Black",bd=5,relief=GROOVE)
    songsframe.place(x=600,y=0,width=400,height=200)
    scroll_y = Scrollbar(songsframe,orient=VERTICAL)
    self.playlist = Listbox(songsframe,yscrollcommand=scroll_y.set,selectbackground="lightblue",selectmode=SINGLE,font=("arial",12,"bold"),bg="lightgrey",fg="Black",bd=5,relief=GROOVE)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)
    label1 = Label(root, text = "Suda Music (v1.05)", bg = "black", fg = "lightgrey", font =("times new roman",15,"bold"), bd=5,relief=GROOVE)
    label1.pack()
    label2 = Label(root, text = "- Added Newly Designed Control Panel", bg = "lightgrey", fg = "black", font =("times new roman",15,"bold"))
    label2.pack()
    label4 = Label(root, text = "- Added Song Playlist", bg = "lightgrey", fg = "black", font =("times new roman",15,"bold"))
    label4.pack()
    label3 = Label(root, text = "- Changed Design of Music Player", bg = "lightgrey", fg = "black", font =("times new roman",15,"bold"))
    label3.pack()
    label1.place(x=800,y=240)
    label2.place(x=15,y=240)
    label3.place(x=15,y=280)
    label4.place(x=15,y=320)
    os.chdir('/home/pi/Music/')
    songtracks = os.listdir()
    for track in songtracks:
      self.playlist.insert(END,track)

  def playsong(self):
    self.track.set(self.playlist.get(ACTIVE))
    self.status.set("-Playing")
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    pygame.mixer.music.play()

  def stopsong(self):
    self.status.set("-Stopped")
    pygame.mixer.music.stop()

  def pausesong(self):
    self.status.set("-Paused")
    pygame.mixer.music.pause()

  def unpausesong(self):
    self.status.set("-Playing")
    pygame.mixer.music.unpause()

root = Tk()
MusicPlayer(root)
root.mainloop()