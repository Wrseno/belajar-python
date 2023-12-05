import pygame
from tkinter import *
from tkinter import Tk, filedialog
import os

class musicPlayer(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.fileContainer=[]
        self.nameContainer=[]

        self.a=StringVar()
        self.a.set("Play")

        parent.geometry("470x290")
        self.parent = parent

        self.name = StringVar()
        self.name.set("Silahkan Buka File")

        self.locationContainer = ""

        self.finish = True
        self.onStop = False
        self.openAgain = True

        self.fileAlreadyPlaying = []
        self.nameAlreadyPlaying = []
        self.playAgain = True
        self.textColumn()
        self.createText()
        self.deleteColumn()
        self.deleteButton()
        self.createPlayButton()
        self.createStopButton()
        self.nextButton()
        self.createOpen()
        self.slider()

    def fileInisialitation(self, file, path):
        self.fileContainer.append(path)
        self.nameContainer.append(file)
        self.refreshColumn()
    
    def refreshColumn(self):
        fill = ""
        no = 1
        for i in self.nameContainer:
            fill += str(no)+". "+i+"\n"
            no += 1
        self.setColumn(fill)
    
    def getFile(self):
        file=""
        if len(self.nameContainer) > 0:
            file = self.fileContainer.pop(0)
            name = self.nameContainer.pop(0)

            self.fileAlreadyPlaying.append(file)
            self.nameAlreadyPlaying.append(name)
            self.name.set("Now playing :"+name)
        self.refreshColumn()
        return file
    
    def playMusic(self):
        self.finish = True
        pygame.init()
        pygame.mixer.init()
        if self.onStop:
            self.onStop = False
            pygame.mixer.music.unpause()
            self.a.set("Pause")
        else:
            self.b = pygame.mixer.music.get_busy()
            a = len(self.fileContainer)
            if self.b:
                if self.a.get() == "Play":
                    self.a.set("Pause")
                    pygame.mixer.music.unpause()
                elif self.a.get() == "Pause":
                    self.a.set("Play")
                    self.pauseOrStop = False
                    pygame.mixer.music.pause()
                    self.pauseOrStop = True
            elif a != 0:
                getFile = self.getFile()
                pygame.mixer.music.load(getFile)
                pygame.mixer.music.play()
                self.playAgain = True
                self.refreshColumn()
                self.getPosition()
                self.a.set("Pause")
    
    def stopMusic(self):
        self.b = pygame.mixer.music.get_busy()
        self.onStop = True
        if self.b :
            pygame.mixer.music.play(1,-1)
            pygame.mixer.music.pause()
            self.a.set("Play")
            self.finish=False

    def nextButton(self):
        next = Button(text="Next", command=self.next)
        next.pack(side=LEFT)

    def next(self):
        self.b = pygame.mixer.music.get_busy()
        if self.b:
            pygame.mixer.music.stop()
            self.playMusic()
        
    def createText(self):
        text = Label(textvariable=self.name, fg="blue", font="Verdana 10 bold")
        text.pack()

    def createStopButton(self):
        button = Button(text="Stop", command=self.stopMusic)
        button.pack(side=LEFT)

    def createOpen(self):
        button = Button(text="Open", command=self.openFile)
        button.pack(side=LEFT)

    def createPlayButton(self):
        button = Button(textvariable=self.a, command=self.playMusic)
        button.pack(side=LEFT)

    def openFile(self):
        fileType = [('Mp3 file', '*.mp3'), ('All files', '*')]
        openFile = filedialog.Open(self, filetypes=fileType)
        fileType = [('Mp3 file', '*.mp3'), ('All files', '*')]
        openFile = filedialog.askopenfilenames(filetypes=fileType)
        if openFile != "":
            for i in openFile:
                location = i
                name = os.path.basename(location)
                self.fileInisialitation(name, location)

    def volume(self, value):
        v = float(value)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(v)

    def slider(self):
        w1 = Scale(from_=0.00, to=1.0, resolution=0.01, command=self.volume, orient=HORIZONTAL, length=300, label='Volume :', showvalue=0)
        w1.pack()
        w1.set(0.50)
    def textColumn(self):
        self.T = Text(height=12, width=30)
        self.scrollBar()
        self.T.configure(state=DISABLED)
    def setColumn(self, nilai):
        self.T.config(state=NORMAL)
        self.T.delete('1.0', END)
        self.T.insert(END, nilai)
        self.T.configure(state=DISABLED)
    def scrollBar(self):
        S = Scrollbar()
        S.pack(side=RIGHT, fill=Y)
        self.T.pack(fill=X)
        S.config(command=self.T.yview)
        self.T.config(yscrollcommand=S.set)
    def getPosition(self):
        pygame.init()
        pygame.mixer.init()
        position = pygame.mixer.music.get_pos()
        if position == -1 and self.finish and self.playAgain:
            self.playMusic()
        self.b = pygame.mixer.music.get_busy()
        if len(self.fileContainer) == 0 and self.b == False and self.onStop == False:
            self.name.set("Pemutaran Selesai")
            self.a.set("Play")
            for i in self.fileAlreadyPlaying:
                self.fileContainer.append(i)
            for i in self.nameAlreadyPlaying:
                self.nameContainer.append(i)
            self.nameAlreadyPlaying = []
            self.fileAlreadyPlaying = []
            self.refreshColumn()
            self.playAgain = False
        elif (len(self.fileContainer) > 0 or self.b) and self.playAgain:
            self.timer = self.parent.after(1000, self.getPosition)
    def deleteColumn(self):
        self.kH = Text(width=3, height=1)
        self.kH.pack()
    def deleteButton(self):
        delete = Button(text="Hapus", command=self.delete)
        delete.pack()
    def delete(self):
        try:
            for i in range(len(self.fileContainer)):
                if i+1 == int(self.kH.get("1.0", END)):
                    self.fileContainer.pop(i)
                    name = self.nameContainer.pop(i)
            self.refreshColumn()
            self.name.set("Berhasil menghapus->"+name)
        except:
            self.name.set("Gagal menghapus file")
    
root = Tk()
musicPlayer(root)
mainloop()
pygame.quit()