import tkinter as tk
from tkinter import *
from Wizard import Step
import tkinter.font as font
import datetime

class Demographic(Step):
    def __init__(self, parent, data, stepname):
        super().__init__(parent, data, stepname)
        timestamp=datetime.datetime.now() ###get the time at the beginning of the session
        timestamp=timestamp.strftime("%Y-%m-%d %H:%M:%S")
        self.data['starttime']=timestamp
        L1=Label(self,text='Name').grid(row=0,sticky=W)
        
        #########
        self.name=StringVar()
        
        vcmd=(self.register(self.updatename),'%P')
        e=Entry(self,textvariable=self.name,validate='key',validatecommand=vcmd).grid(row=0,column=1)

        ########
        L2=Label(self,text='Gender').grid(row=1,sticky=W)

        self.gender=StringVar()
        self.gender.set('Male')
        Radiobutton(self, text="Male", variable=self.gender, value='Male',command=self.updategender).grid(row=1,column=1,sticky=W)
        Radiobutton(self, text="Female", variable=self.gender, value='Female',command=self.updategender).grid(row=1,column=2,sticky=W)
        ######

        ########
        L3=Label(self,text='Participant ID').grid(row=3,sticky=W)
        self.participantID=IntVar()
        vcmd2=(self.register(self.updatepID),'%P')
        e=Entry(self,textvariable=self.participantID,validate='key',validatecommand=vcmd2).grid(row=3,column=1)
       
        L4=Label(self,text='Session ID').grid(row=4,sticky=W)
        self.sessionID=IntVar()
        vcmd3=(self.register(self.updatesessionID),'%P')
        e=Entry(self,textvariable=self.sessionID,validate='key',validatecommand=vcmd3).grid(row=4,column=1)
        #################
#        L5=Label(self,text='Like turtles').grid(row=4,sticky=W)
#        self.likegrade=IntVar()
#        slider1 = Scale(self, from_=0, to=100,orient=HORIZONTAL,variable=self.likegrade,command=self.updateValue).grid(row=4,column=1)
#        L5=Label(self,text='Everything is fine?').grid(row=5,sticky=W)
#        self.finegrade=IntVar()
#        slider2 = Scale(self, from_=0, to=100,orient=HORIZONTAL,variable=self.finegrade).grid(row=5,column=1)
        ###########

        ############
#        quitbutton=Button(self,text='quit',fg='red',command=quit).grid(row=6)
        
        
        #printbutton=tk.Button(self,text="Update",fg='red',command=self.updateValue).grid(row=6,column=1,rowspan=3)
        
        self.data["demographics"]["gender"] =self.gender.get()

        
      
    def show_result(self):
        
        print(self.gender.get())
        print('age is',self.age.get())
        print('preferred meal:',self.meal.get())

#        print('Like Turtle',self.likegrade.get())
#        print('How fine',self.finegrade.get())
    def updategender(self):
        self.data["demographics"]["gender"] =self.gender.get()
    def updatepID(self,text):
        self.data[self.stepname]['Participant ID']=text
        return True
    def updatesessionID(self,text):
        self.data[self.stepname]['Session ID']=text 
        return True
    def updatename(self,new_text):
        self.data[self.stepname]['Name']=new_text
        return True
    
class sports(Step):
    def __init__(self, parent, data, stepname):
        super().__init__(parent, data, stepname)
        self.sports=[]
        L1=Label(self,text='Choose the sports you would like to watch').grid(row=0,columnspan=4,sticky=W)
        
        Checkbutton(self, text="basketball",command=self.updatebasketball).grid(row=1, sticky=W)
       
        Checkbutton(self, text="football",command=self.updatefootball).grid(row=2, sticky=W)
        Checkbutton(self, text="baseball",command=self.updatebaseball).grid(row=3, sticky=W)
        Checkbutton(self, text="pingpang",command=self.updatepingpong).grid(row=4, sticky=W)
        

        
        ######
    def updatebasketball(self):
        self.sports.append('basketball')
        self.data[self.stepname] =self.sports
    def updatefootball(self):
        self.sports.append('football')
        self.data[self.stepname] =self.sports
    def updatebaseball(self):
        self.sports.append('baseball')
        self.data[self.stepname] =self.sports
    def updatepingpong(self):
        self.sports.append('pingpang')
        self.data[self.stepname] =self.sports
        
        
        
class fourchoices(Step):
    def __init__(self, parent, data, stepname):
        super().__init__(parent, data, stepname)

        L2=Label(self,text='In which year did Georgia Tech come into being').grid(row=1,columnspan=4,sticky=W)
        self.year=StringVar()
        self.year.set('1850')
        self.data[self.stepname]["year"] =self.year.get()
        Radiobutton(self, text="1850", variable=self.year, value='1850',command=self.updateyear).grid(row=2,column=1,sticky=W)
        Radiobutton(self, text="1875", variable=self.year, value='1875',command=self.updateyear).grid(row=2,column=2,sticky=W)        
        Radiobutton(self, text="1885", variable=self.year, value='1885',command=self.updateyear).grid(row=2,column=3,sticky=W)
        Radiobutton(self, text="1889", variable=self.year, value='1889',command=self.updateyear).grid(row=2,column=4,sticky=W)
    def updateyear(self):
        self.data[self.stepname]["year"] =self.year.get()