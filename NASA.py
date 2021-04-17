from tkinter import Tk, Label, Radiobutton, Button, StringVar, Entry, Scale, IntVar, END, W, E, HORIZONTAL, LEFT, Frame, SUNKEN

from Wizard import Step
import random

class NASA(Step):
    def __init__(self, parent, data, stepname):
        super().__init__(parent, data, stepname)
        
        lbl1 = Label(self, text='Click on each scale at the point that best indicates your experience of the task')
        lbl1.grid(row=1,column=1)

        lbl2 = Label(self, text="(1=extremely low,5=extremely high)")
        lbl2.grid(row=2,column=1)
        ###########################
        lbl3=Label(self,text='Mental demand: How much mental and perceptual activity was required?')
        lbl3.grid(row=3,column=1)
        mentalscale = Scale(self, from_=1, to=10, length=200, tickinterval=1, orient=HORIZONTAL, command=self.updatemental)
        mentalscale.set(5)
        mentalscale.grid(row=3,column=2)

        self.data[self.stepname]["mental demand weight"] = mentalscale.get()
        ###########
        lbl4=Label(self,text='Physical demand: How much physical activity was required?')
        lbl4.grid(row=4,column=1)
        physicalscale = Scale(self, from_=1, to=10, length=200, tickinterval=1, orient=HORIZONTAL, command=self.updatephysical)
        physicalscale.set(5)
        physicalscale.grid(row=4,column=2)

        self.data[self.stepname]["physical demand weight"] = physicalscale.get()
        ###########
        ###########
        lbl5=Label(self,text='Temporal demand: How much time pressure did you feel due to the rate of pace at which the tasks or task elements occurred?')
        lbl5.grid(row=5,column=1)
        temporalscale = Scale(self, from_=1, to=10, length=200, tickinterval=1, orient=HORIZONTAL, command=self.updatetemporal)
        temporalscale.set(5)
        temporalscale.grid(row=5,column=2)

        self.data[self.stepname]["temporal demand weight"] = temporalscale.get()
        ###########
        ###########
        lbl6=Label(self,text='Performance: How successful do you think you were in accomplishing the goals?')
        lbl6.grid(row=6,column=1)
        perforscale = Scale(self, from_=1, to=10, length=200, tickinterval=1, orient=HORIZONTAL, command=self.updateperformance)
        perforscale.set(5)
        perforscale.grid(row=6,column=2)

        self.data[self.stepname]["performance weight"] = perforscale.get()
        ###########
                ###########
        lbl7=Label(self,text='Effort: How hard did you have to work (mentally and physically) to accomplish your level of performance?')
        lbl7.grid(row=7,column=1)
        effortscale = Scale(self, from_=1, to=10, length=200, tickinterval=1, orient=HORIZONTAL, command=self.updateeffort)
        effortscale.set(5)
        effortscale.grid(row=7,column=2)

        self.data[self.stepname]["effort weight"] = effortscale.get()
        ###########
                ###########
        lbl8=Label(self,text='Frustration: How insecure, discouraged, irritated, stressed,and annoyed were you?')
        lbl8.grid(row=8,column=1)
        frustrationscale = Scale(self, from_=1, to=10, length=200, tickinterval=1, orient=HORIZONTAL, command=self.updatefrustration)
        frustrationscale.set(5)
        frustrationscale.grid(row=8,column=2)

        self.data[self.stepname]["frustration weight"] = frustrationscale.get()
        ###########

        self.data[self.stepname]["choose mental times"] = 0
        self.data[self.stepname]["choose physical times"] = 0
        self.data[self.stepname]["choose temporal times"] = 0
        self.data[self.stepname]["choose performance times"] = 0
        self.data[self.stepname]["choose effort times"] = 0
        self.data[self.stepname]["choose frustration times"] = 0

            
        
        
        
        

    def updatemental(self, event):
        #print(event)
        self.data[self.stepname]["mental demand weight"] = event

    def updatephysical(self, event):
        #print(event)
        self.data[self.stepname]["physical demand weight"] = event
        
    def updatetemporal(self, event):
        #print(event)
        self.data[self.stepname]["temporal demand weight"] = event
        
    def updateperformance(self, event):
        #print(event)
        self.data[self.stepname]["performance weight"] = event
    def updateeffort(self, event):
        #print(event)
        self.data[self.stepname]["effort weight"] = event
    def updatefrustration(self, event):
        #print(event)
        self.data[self.stepname]["frustration weight"] = event
        
        
class comparequestions(Step):
    def __init__(self, parent, data, stepname,twoquestions):
        super().__init__(parent, data, stepname)
        L2=Label(self,text='Click on the factor that represents the more important contributor to workload for the task').grid(row=1)
        self.question1=twoquestions[0]
        self.question2=twoquestions[1]
        self.v = IntVar()
        Radiobutton(self, text=str(self.question1),variable=self.v, value=1,command=self.updatequestion1).grid(row=2,column=1,sticky=W)
        Radiobutton(self, text=str(self.question2),variable=self.v, value=2,command=self.updatequestion2).grid(row=2,column=2,sticky=W)
    def updatequestion1(self):
        self.data[self.stepname]['choose '+str(self.question1)+' times'] = self.data[self.stepname]['choose '+str(self.question1)+' times'] +1
    def updatequestion2(self):          
        self.data[self.stepname]['choose '+str(self.question2)+' times'] = self.data[self.stepname]['choose '+str(self.question2)+' times'] +1
            
                