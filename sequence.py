from tkinter import *
from playsoundasync import playsoundasync
from Wizard import Wizard
#from LikertStep import LikertStep
from choices import Demographic
#from choices import fourchoices
#from choices import sports
from Wizard import Step
from PIL import ImageTk, Image
import random

class clicky(Step):
    def __init__(self, parent,data,stepname,matchsequence):
        super().__init__(parent,data, stepname)
        self.matchsequence=matchsequence
        # load an image
        # be sure to store ref to image: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        self.soccer = ImageTk.PhotoImage(Image.open("pics/soccer_ball.png").resize((200,200),Image.ANTIALIAS))
        self.football = ImageTk.PhotoImage(Image.open("pics/football.png").resize((200,200),Image.ANTIALIAS))
        self.compass=ImageTk.PhotoImage(Image.open("pics/compass.png").resize((200,200),Image.ANTIALIAS))
        self.darthvader=ImageTk.PhotoImage(Image.open("pics/darthvader.jpg").resize((200,200),Image.ANTIALIAS))

        self.start = Button(self, text="Click to Start The Game!", font="Helvetica 16 bold italic",command=self.startgame)
        self.start.grid(row=1,column=2)
        
        self.soccerlabel = Button(self, image=self.soccer,command=self.clickbutton0)
        self.soccerlabel.grid(row=2,column=2)

        self.footballlabel = Button(self, image=self.football,command=self.clickbutton1)
        self.footballlabel.grid(row=3,column=1)
        
        self.compasslabel=Button(self,image=self.compass,command=self.clickbutton2)
        self.compasslabel.grid(row=4,column=2)
        
        self.darthlabel=Button(self,image=self.darthvader,command=self.clickbutton3)
        self.darthlabel.grid(row=3,column=3)
        self.info=Label(self)
        self.info.grid(row=3,column=2)
        self.target_list = []
        
        ## 0 means soccer, 1 means football, 2 means compass, 3 means darth varder
        btn_list = [(lambda:self.buttonpresssoccer(None),lambda:self.buttonreleasesoccer(None)), (lambda:self.buttonpressfootball(None),lambda:self.buttonreleasefootball(None))
                    ,(lambda:self.buttonpresscompass(None),lambda:self.buttonreleasecompass(None)),(lambda:self.buttonpressdarth(None),lambda:self.buttonreleasedarth(None))]
        
        self.matchtrial=1
        self.info.config(text="Round with "+str(self.matchsequence)+' sequences',font="Helvetica 14 bold italic",fg="black")
        
        for self.seq_len in [self.matchsequence]:
            self.data['Simon Game']['block with'+str(self.seq_len)+'sequences']={}
            for j in range(1,6):
                self.data['Simon Game']['block with'+str(self.seq_len)+'sequences'][str(j)+' trial right sequence']=[]
                self.data['Simon Game']['block with'+str(self.seq_len)+'sequences'][str(j)+' trial user sequence']=[]
                self.target_list.append((1500, self.labelbegin))
                for i in range(self.seq_len):
                    target_btn_index = random.randint(0, len(btn_list)-1)

                    btn_down = btn_list[target_btn_index][0]
                    btn_up = btn_list[target_btn_index][1]
                    self.data['Simon Game']['block with'+str(self.seq_len)+'sequences'][str(j)+' trial right sequence'].append(target_btn_index)
                    tup_down = (1000, btn_down)
                    tup_up = (500, btn_up)
                    self.target_list.append(tup_down)
                    self.target_list.append(tup_up)                   
                self.target_list.append((10, lambda:self.labelend()))
                self.target_list.append((9500, lambda: self.trialplus()))
                self.target_list.append((10, self.labelbegin))
                
                

        self.schedule = []
        
        

    def startgame(self):
        self.schedule=self.target_list

        self.doanim()
#[(lambda:self.buttonpresssoccer(None),lambda:self.buttonreleasesoccer(None)), (lambda:self.buttonpressfootball(None),lambda:self.buttonreleasefootball(None))
#,(lambda:self.buttonpresscompass(None),lambda:self.buttonreleasecompass(None)),(lambda:self.buttonpressdarth(None),lambda:self.buttonreleasedarth(None))]
#
    def trialplus(self):
        if len(self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial user sequence'])<self.matchsequence:
           self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial user sequence'].append('failed')
           self.info.config(text="Failed",font="Helvetica 16 bold italic",fg="red")
           
           
        self.matchtrial=self.matchtrial+1
        if self.matchtrial==6:
           self.info.config(text="Game Over, press next",font="Helvetica 14 bold italic",fg="black")
           self.target_list = []
           
 
           
#           self.info.config(text="Round with "+str(self.matchsequence)+' sequences',font="Helvetica 14 bold italic",fg="black")

                  
        
    def clickbutton0(self):
        self.after(10,lambda:self.buttonpresssoccer(None))
        self.after(500,lambda:self.buttonreleasesoccer(None))
        self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial user sequence'].append(0)
        self.checkmatch()
        
    def checkmatch(self):
        if len(self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial user sequence'])==self.matchsequence:
            if self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial user sequence']==self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial right sequence']:
               self.info.config(text="Success!",font="Helvetica 16 bold italic",fg="green")
               self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial user sequence'].append('succeed')
               #self.matchtrial=self.matchtrial+1
            else:
                self.info.config(text="Failed!",font="Helvetica 16 bold italic",fg="red")
                self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial user sequence'].append('failed')   
#        if self.matchtrial==6:
#           self.matchsequence=self.matchsequence+1000
#           self.info.config(text="Game Over, press next",font="Helvetica 14 bold italic",fg="black")
#           if len(self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial user sequence'])!=self.matchsequence:
#               self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial user sequence'].append('failed')
#           self.target_list = []
##           self.info.config(text="Round with "+str(self.matchsequence)+' sequences',font="Helvetica 14 bold italic",fg="black")
#        if self.matchsequence>20:
#           self.info.config(text="Game Over!",font="Helvetica 16 bold italic",fg="red")
           
        
        
    def clickbutton1(self):
        self.after(10,lambda:self.buttonpressfootball(None))
        self.after(500,lambda:self.buttonreleasefootball(None))
        self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial user sequence'].append(1)
        self.checkmatch()
        
    def clickbutton2(self):
        self.after(10,lambda:self.buttonpresscompass(None))
        self.after(500,lambda:self.buttonreleasecompass(None))
        self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial user sequence'].append(2)
        self.checkmatch()
        
    def clickbutton3(self):
        self.after(10,lambda:self.buttonpressdarth(None))
        self.after(500,lambda:self.buttonreleasedarth(None))
        self.data['Simon Game']['block with'+str(self.matchsequence)+'sequences'][str(self.matchtrial)+' trial user sequence'].append(3)
        self.checkmatch()

    def doanim(self):

        if len(self.schedule) <= 0:
            return

        self.sched_item = 0

        s = self.schedule[self.sched_item]
        #run the function stored in the schedule
        self.after(s[0], self.doanim_helper)


    def doanim_helper(self):

        s = self.schedule[self.sched_item]
        # run the function stored in the schedule
        s[1]()

        self.sched_item += 1

        if self.sched_item >= len(self.schedule):
            self.after(1000, self.quit)
        else:
            s = self.schedule[self.sched_item]
            self.after(s[0], self.doanim_helper)


    def labelbegin(self):
        self.start.config(text="Animation is playing "+str(self.matchtrial)+'st trial', fg="green")

    def labelend(self):
        self.start.config(text="Repeat the sequences in 10s", fg="red")
        

    def buttonpresssoccer_demo(self):
        self.buttonpresssoccer()

    def buttonpresssoccer(self,event):
        self.soccerlabel.config(bg="red")
        playsoundasync('audio/beep.wav')

    def buttonreleasesoccer(self, event):
        self.soccerlabel.config(bg="white")

    def buttonpressfootball(self, event):
        self.footballlabel.config(bg="yellow")
        playsoundasync('audio/bleep.wav')


    def buttonreleasefootball(self, event):
        self.footballlabel.config(bg="white")
        
    def buttonpresscompass(self,event):
        self.compasslabel.config(bg="red")
        playsoundasync('audio/cowboy.wav')
    def buttonreleasecompass(self,event):
        self.compasslabel.config(bg="white")
    def buttonpressdarth(self,event):
        self.darthlabel.config(bg="red")
        playsoundasync('audio/punch.wav')
    def buttonreleasedarth(self,event):
        self.darthlabel.config(bg="white")
      



#if __name__ == "__main__":
#    root = Tk()
#
#    my_gui = clicky(root)
#    my_gui.pack()
#
#    root.mainloop()
